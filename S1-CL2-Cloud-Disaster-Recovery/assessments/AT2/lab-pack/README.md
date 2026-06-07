# S1-CL2 AT2 — Audit-log microservice lab pack

The runnable artefacts for AT2 (DR Implementation): a serverless **audit-log microservice**
(HTTP API → SQS → Lambda → DynamoDB) provisioned with **infrastructure-as-code**, plus a
**local validation harness** that lints the templates and runs the handler **without an AWS
account**.

```
lab-pack/
  README.md                 ← you are here
  requirements.txt          ← local-validation deps (venv); NOT needed to deploy in the lab
  predefined/               ← SUPPLIED to students — templates they OPERATE (ICTCLD505 el 1-2)
    foundation-stack.yaml         deploy → update a parameter → delete
    foundation-stack-broken.yaml  one deliberate error to find + fix (troubleshooting)
  microservice/             ← SUPPLIED to students — the pre-prepared code (503 AC 4)
    handler.py                    the SQS-triggered DynamoDB writer
    webhook-contract.md           the POST /events payload contract
  assessor-model/           ← ASSESSOR-ONLY — the model "author your own template" answer
    audit-service.yaml            full microservice (ICTCLD505 el 3)
    notes.md                      the deliberate fault + fix; marking notes
  tests/
    test_handler.py               runs handler.py against an in-test DynamoDB fake
```

> **Region / role for the whole pack:** deploy everything to **`us-west-2`** (the AWS Academy
> stand-in for the India region `ap-south-1`). In the **AWS Academy Learner Lab you cannot
> create IAM roles**, so the microservice template takes the pre-provisioned **`LabRole`** ARN
> as a parameter rather than creating a role.

---

## A. Local validation (no AWS account)

Catches template and code errors before anything touches the lab. Run once to set up the venv:

```bash
cd lab-pack
python -m venv .venv
# Windows:
.venv/Scripts/python -m pip install -r requirements.txt
# macOS / Linux:
.venv/bin/python -m pip install -r requirements.txt
```

Then validate:

```bash
# 1) Lint the templates (the two good ones should be clean):
.venv/Scripts/cfn-lint predefined/foundation-stack.yaml assessor-model/audit-service.yaml

# 2) Confirm the broken template is caught (this SHOULD report an error — that's the point):
.venv/Scripts/cfn-lint predefined/foundation-stack-broken.yaml

# 3) Run the handler test (validation, idempotency, batch counting):
.venv/Scripts/python -m pytest -q
```

Expected: steps 1 and 3 pass (exit 0); step 2 reports `E1020 'BacklogThreshold' is not one of …`
(exit non-zero). On macOS/Linux use `.venv/bin/cfn-lint` and `.venv/bin/python`.

`moto` is deliberately **not** a dependency (its deeply-nested package paths break Windows'
260-char `MAX_PATH` inside this repo) — the test uses a small in-file DynamoDB fake instead, so
it installs and runs on any machine.

---

## B. Deploy to the AWS Academy lab

Run these from **CloudShell** in the lab console (easiest — the AWS CLI and your session
credentials are already there). Upload this `lab-pack/` folder, or paste the templates in.

### B1. Operate the predefined template (ICTCLD505 elements 1–2)

```bash
# Deploy:
aws cloudformation deploy --region us-west-2 \
  --stack-name yat-audit-foundation \
  --template-file predefined/foundation-stack.yaml \
  --parameter-overrides EnvName=dev

# Update a parameter (observe the change set / UPDATE_COMPLETE):
aws cloudformation deploy --region us-west-2 \
  --stack-name yat-audit-foundation \
  --template-file predefined/foundation-stack.yaml \
  --parameter-overrides AlarmBacklogThreshold=50

# Delete (clean teardown):
aws cloudformation delete-stack --region us-west-2 --stack-name yat-audit-foundation
```

Troubleshooting exercise: try `predefined/foundation-stack-broken.yaml`, read the error
(`cfn-lint` reports it instantly, or the deploy fails), fix the parameter name, redeploy.

### B2. Author / deploy the microservice (ICTCLD505 element 3 + ICTCLD503 element 3)

```bash
# Find the pre-provisioned LabRole ARN:
LAB_ROLE=$(aws iam get-role --role-name LabRole --query Role.Arn --output text)
echo "$LAB_ROLE"

# Deploy the microservice (table + queue + Lambda + HTTP API + alarm):
aws cloudformation deploy --region us-west-2 \
  --stack-name yat-audit-service \
  --template-file assessor-model/audit-service.yaml \
  --parameter-overrides EnvName=dev LabRoleArn="$LAB_ROLE"
# (If CloudFormation asks for capabilities, add: --capabilities CAPABILITY_IAM)

# Get the API endpoint:
ENDPOINT=$(aws cloudformation describe-stacks --region us-west-2 \
  --stack-name yat-audit-service \
  --query "Stacks[0].Outputs[?OutputKey=='ApiEndpoint'].OutputValue" --output text)
echo "$ENDPOINT"
```

### B3. Test it end to end

```bash
# Send a sample access event:
curl -X POST "$ENDPOINT" -H "Content-Type: application/json" -d '{
  "event_id":"test-001","occurred_at":"2026-06-07T01:23:45Z","user_ref":"u-1",
  "cohort":"IN","event_type":"login","source_ip":"203.0.113.7"}'

# Confirm it landed in the audit table (give it a second to flow through the queue):
aws dynamodb scan --region us-west-2 --table-name yat-audit-dev --query "Items"
```

Reuse / parameterisation evidence: redeploy the same template with `EnvName=prod` (and/or to
`us-east-1`) — one template, different configuration, no edits to the body.

### B4. Tear down

```bash
aws cloudformation delete-stack --region us-west-2 --stack-name yat-audit-service
aws cloudformation delete-stack --region us-west-2 --stack-name yat-audit-foundation
```

---

## ⚠️ Verify in a live lab before delivery

The artefacts are written to documented AWS Academy Learner Lab constraints (us-west-2,
`LabRole`, serverless services only) and pass local validation, but they have **not yet been
run in a live Academy session**. One verification pass is needed to confirm:

- the enrolled lab product exposes Lambda, DynamoDB, SQS, API Gateway (HTTP API), CloudWatch;
- `LabRole` can be passed to Lambda **and** used as the API Gateway → SQS integration
  credentials (trust + `sqs:SendMessage` / `dynamodb:PutItem`);
- the HTTP API → SQS `SendMessage` service integration deploys as written.

This resolves the cluster's open `[VERIFY]` on the exact lab product.
