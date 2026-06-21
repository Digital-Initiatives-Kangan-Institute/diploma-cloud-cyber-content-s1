"""Structural tests of the AT3 Ledgerline lab-pack templates - run with NO AWS account.

Asserts the invariants that make this a valid existing-state baseline + a valid improvement
change-set, honouring the AWS Academy constraints and - critically - that the DATABASE is never
Multi-AZ (Ledgerline does not support it; reliability is via backup/restore, not failover).

Templates are parsed with cfn-lint's decoder so the intrinsic tags (!Ref, !GetAtt, !Sub, !Select,
!If, !GetAZs) load correctly.

Run from the lab-pack folder:  python -m pytest
"""
from pathlib import Path

from cfnlint.decode import cfn_yaml

LAB = Path(__file__).resolve().parent.parent
BASELINE = LAB / "baseline.yaml"
IMPROVED = LAB / "improved.yaml"
INDIA = LAB / "india-residency.yaml"
ALL_TEMPLATES = [BASELINE, IMPROVED, INDIA]


def _load(path):
    loaded = cfn_yaml.load(str(path))
    return loaded[0] if isinstance(loaded, tuple) else loaded


def _of_type(template, resource_type):
    return {k: v for k, v in template["Resources"].items() if v.get("Type") == resource_type}


# ---- decode / structure ----

def test_all_templates_decode():
    for path in ALL_TEMPLATES:
        t = _load(path)
        assert "Resources" in t and t["Resources"], f"{path.name} has no resources"


# ---- the central invariant: the database is NEVER Multi-AZ ----

def test_rds_is_single_az_in_both_templates():
    # Ledgerline does not support a Multi-AZ database - it must stay single-instance in BOTH the
    # baseline AND the improved (change-set) template. This is the whole point of the design.
    for path in (BASELINE, IMPROVED):
        for name, db in _of_type(_load(path), "AWS::RDS::DBInstance").items():
            assert db["Properties"].get("MultiAZ") is False, \
                f"{path.name}:{name} must NOT be Multi-AZ (Ledgerline constraint)"


def test_rds_is_sql_server():
    for path in (BASELINE, IMPROVED):
        dbs = _of_type(_load(path), "AWS::RDS::DBInstance")
        assert dbs, f"{path.name} has no RDS instance"
        for name, db in dbs.items():
            engine = db["Properties"]["Engine"]
            # Engine is a !Ref to a parameter defaulting to a sqlserver-* edition; check the default.
            t = _load(path)
            default = t["Parameters"]["DBEngine"]["Default"]
            assert default.startswith("sqlserver"), f"{path.name} DBEngine default must be SQL Server"


def test_rds_encrypted_and_empty():
    # Encrypted at rest, and no DBName (SQL Server: the instance comes up with no user database).
    for path in (BASELINE, IMPROVED):
        for name, db in _of_type(_load(path), "AWS::RDS::DBInstance").items():
            assert db["Properties"].get("StorageEncrypted") is True, f"{path.name}:{name} must be encrypted"
            assert "DBName" not in db["Properties"], f"{path.name}:{name} must have no DBName (empty)"


# ---- compute: single-AZ baseline -> 2-AZ improved ----

def test_baseline_compute_is_single_az():
    asgs = _of_type(_load(BASELINE), "AWS::AutoScaling::AutoScalingGroup")
    assert asgs, "baseline has no Auto Scaling group"
    for name, asg in asgs.items():
        zones = asg["Properties"]["VPCZoneIdentifier"]
        assert len(zones) == 1, f"baseline {name} must span ONE subnet (the improvement spreads it)"


def test_improved_compute_is_multi_az():
    asgs = _of_type(_load(IMPROVED), "AWS::AutoScaling::AutoScalingGroup")
    assert asgs, "improved has no Auto Scaling group"
    for name, asg in asgs.items():
        zones = asg["Properties"]["VPCZoneIdentifier"]
        assert len(zones) == 2, f"improved {name} must span TWO subnets (application-tier Multi-AZ)"


def test_improved_does_not_modify_db():
    # The AWS Academy lab role cannot rds:ModifyDBInstance, and the legacy DB tier is not restructured
    # by the improvement, so the Database resource MUST be identical in baseline and improved (the
    # change-set produces NO diff on the DB). DR improvements (wider retention, cross-Region copy) are
    # out-of-band steps, not CFN changes.
    base_db = next(iter(_of_type(_load(BASELINE), "AWS::RDS::DBInstance").values()))
    imp_db = next(iter(_of_type(_load(IMPROVED), "AWS::RDS::DBInstance").values()))
    assert imp_db["Properties"] == base_db["Properties"], \
        "improved.yaml must NOT modify the Database (sandbox denies rds:ModifyDBInstance)"


# ---- internal ALB (internal-only system, no public ingress) ----

def test_alb_is_internal():
    for path in (BASELINE, IMPROVED):
        albs = _of_type(_load(path), "AWS::ElasticLoadBalancingV2::LoadBalancer")
        assert albs, f"{path.name} has no load balancer"
        for name, alb in albs.items():
            assert alb["Properties"]["Scheme"] == "internal", f"{path.name}:{name} must be an internal ALB"


# ---- AWS Academy constraints ----

def test_no_iam_resources_created():
    iam = {"AWS::IAM::Role", "AWS::IAM::User", "AWS::IAM::Group", "AWS::IAM::Policy",
           "AWS::IAM::ManagedPolicy", "AWS::IAM::InstanceProfile"}
    for path in ALL_TEMPLATES:
        found = [k for k, v in _load(path)["Resources"].items() if v.get("Type") in iam]
        assert not found, f"{path.name}: Academy forbids creating IAM; found {found}"


def test_instance_profile_is_optional():
    for path in (BASELINE, IMPROVED):
        t = _load(path)
        assert t["Parameters"]["InstanceProfileName"].get("Default", "") == "", \
            f"{path.name}: instance profile must default to blank"
        assert "HasInstanceProfile" in t.get("Conditions", {}), f"{path.name}: expected HasInstanceProfile"


def test_ami_resolved_via_ssm_parameter():
    for path in (BASELINE, IMPROVED):
        ami = _load(path)["Parameters"]["WindowsAmiId"]
        assert ami["Type"] == "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>", \
            f"{path.name}: AMI must come from an SSM public parameter"


def test_buckets_block_public_access():
    for path in ALL_TEMPLATES:
        buckets = _of_type(_load(path), "AWS::S3::Bucket")
        assert buckets, f"{path.name} has no S3 buckets"
        for name, bucket in buckets.items():
            pab = bucket["Properties"]["PublicAccessBlockConfiguration"]
            for flag in ("BlockPublicAcls", "BlockPublicPolicy", "IgnorePublicAcls", "RestrictPublicBuckets"):
                assert pab[flag] is True, f"{path.name}:{name}.{flag} must be true"


# ---- India residency slice ----

def test_india_slice_has_certin_and_books_buckets():
    buckets = _of_type(_load(INDIA), "AWS::S3::Bucket")
    assert len(buckets) == 2, "india-residency must hold exactly the CERT-In logs + books buckets"


def test_certin_retention_at_least_180_days():
    t = _load(INDIA)
    certin = t["Resources"]["CertInLogsBucket"]["Properties"]["LifecycleConfiguration"]["Rules"]
    expiry = next(r["ExpirationInDays"] for r in certin if "ExpirationInDays" in r)
    assert expiry >= 180, "CERT-In logs must be retained at least 180 days"


# ---- pure ASCII (a non-ASCII char in an RDS description fails the live deploy; cfn-lint misses it) ----

def test_templates_are_pure_ascii():
    for path in ALL_TEMPLATES:
        raw = path.read_bytes()
        try:
            raw.decode("ascii")
        except UnicodeDecodeError as exc:
            raise AssertionError(f"{path.name} contains a non-ASCII byte at offset {exc.start}") from exc
