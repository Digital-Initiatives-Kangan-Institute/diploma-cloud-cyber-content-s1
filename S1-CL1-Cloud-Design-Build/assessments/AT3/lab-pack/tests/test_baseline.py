"""Structural test of the AT3 baseline template — runs with NO AWS account.

Asserts the invariants that make this a valid *non-HA baseline* (the thing AT3 hardens) and
that it honours the AWS Academy constraints. Parses the template with cfn-lint's decoder so
the CloudFormation intrinsic tags (!Ref, !GetAtt, !Sub, !Select) load correctly.

Run from the lab-pack folder:  python -m pytest
"""
from pathlib import Path

from cfnlint.decode import cfn_yaml

TEMPLATE = Path(__file__).resolve().parent.parent / "baseline.yaml"


def _load():
    loaded = cfn_yaml.load(str(TEMPLATE))
    template = loaded[0] if isinstance(loaded, tuple) else loaded
    return template


def _of_type(template, resource_type):
    return {k: v for k, v in template["Resources"].items() if v.get("Type") == resource_type}


def test_template_decodes():
    t = _load()
    assert "Resources" in t and t["Resources"]


def test_rds_is_single_az():
    # The baseline DB is Single-AZ; enabling Multi-AZ is the AT3 hardening step.
    for name, db in _of_type(_load(), "AWS::RDS::DBInstance").items():
        assert db["Properties"].get("MultiAZ") is False, f"{name} must be Single-AZ in the baseline"


def test_compute_is_single_az():
    # The ASG runs in ONE subnet/AZ; spreading it across AZs is the AT3 hardening step.
    asgs = _of_type(_load(), "AWS::AutoScaling::AutoScalingGroup")
    assert asgs, "no Auto Scaling group"
    for name, asg in asgs.items():
        zones = asg["Properties"]["VPCZoneIdentifier"]
        assert len(zones) == 1, f"{name} must span ONE subnet in the baseline (AT3 spreads it)"


def test_no_iam_resources_created():
    # AWS Academy Learner Lab forbids creating IAM — the template must use the pre-provisioned role.
    iam = {"AWS::IAM::Role", "AWS::IAM::User", "AWS::IAM::Group", "AWS::IAM::Policy",
           "AWS::IAM::ManagedPolicy", "AWS::IAM::InstanceProfile"}
    found = [k for k, v in _load()["Resources"].items() if v.get("Type") in iam]
    assert not found, f"Academy forbids creating IAM resources; found {found}"


def test_instance_profile_is_optional():
    # Instance-profile names vary by lab product (and may not exist), so the baseline attaches
    # one only if a name is supplied — it deploys with none by default.
    t = _load()
    assert t["Parameters"]["InstanceProfileName"].get("Default", "") == "", "profile must default to blank"
    assert "HasInstanceProfile" in t.get("Conditions", {}), "expected the HasInstanceProfile condition"


def test_ami_resolved_via_ssm_parameter():
    # No hardcoded AMI to go stale — resolved from an SSM public parameter.
    ami = _load()["Parameters"]["WindowsAmiId"]
    assert ami["Type"] == "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>"


def test_expected_outputs_present():
    outputs = _load()["Outputs"]
    for key in ("AlbDnsName", "RdsEndpoint", "AttachmentsBucketName", "BackupsBucketName"):
        assert key in outputs, f"missing output: {key}"


def test_buckets_block_public_access():
    buckets = _of_type(_load(), "AWS::S3::Bucket")
    assert buckets, "no S3 buckets"
    for name, bucket in buckets.items():
        pab = bucket["Properties"]["PublicAccessBlockConfiguration"]
        for flag in ("BlockPublicAcls", "BlockPublicPolicy", "IgnorePublicAcls", "RestrictPublicBuckets"):
            assert pab[flag] is True, f"{name}.{flag} must be true"
