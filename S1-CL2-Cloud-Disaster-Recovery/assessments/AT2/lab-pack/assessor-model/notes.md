# Assessor notes — AT2 lab pack

Internal. Not distributed to students.

## The troubleshooting fault (`predefined/foundation-stack-broken.yaml`)

One deliberate, fixable error for the troubleshooting criterion (ICTCLD505 PC 2.6 / 3.7;
ICTCLD503 PC 3.4):

- **Fault:** the `BacklogAlarm.Threshold` references `!Ref BacklogThreshold`, but the
  parameter is named `AlarmBacklogThreshold`.
- **How it surfaces:** `cfn-lint` reports `E1020 'BacklogThreshold' is not one of [...]`; a
  live deploy fails validation for the same reason. (A secondary `W2001 Parameter
  AlarmBacklogThreshold not used` also appears — a symptom of the same typo.)
- **Fix:** change `!Ref BacklogThreshold` → `!Ref AlarmBacklogThreshold`. After the fix the
  template lints clean and deploys.

A satisfactory troubleshooting response identifies the error (ideally by running `cfn-lint`
first), explains it, applies the fix, and re-validates.

## Marking the student's own template (vs `assessor-model/audit-service.yaml`)

`audit-service.yaml` is the model answer for ICTCLD505 element 3 (the student's *own*
template). A satisfactory student template should:

- Provision a **related set of resources** as one stack: an event store (DynamoDB), a queue
  (SQS), the writer function (Lambda), the ingress (HTTP API), the event-source mapping, and
  a monitoring alarm. (Provisioning a subset wired to the foundation stack via cross-stack
  imports is also acceptable.)
- Be **parameterised for reuse** (`PE 2`, `KE 8`): at minimum `EnvName` (so dev/prod deploy
  from one template) and the `LabRoleArn` (so it's portable across lab accounts). Region reuse
  is demonstrated by deploying the same template with `--region`.
- Reference the **pre-provisioned `LabRole`** for the Lambda execution role and the API
  integration credentials (the lab does not allow creating IAM roles).
- **Update/redeploy and remove cleanly** (`PC 3.3`, `3.6`), and the student should have
  **troubleshot** at least one error (`PC 3.7`) — captured in their Deployment Report §6.6.

The exact resource names, the queue/visibility settings, the alarm threshold, and the choice
of HTTP API vs REST API can all vary — mark the *competency* (a parameterised, related,
deployable stack), not an exact match to this model.

## Handler note

`assessor-model/audit-service.yaml` inlines a copy of `microservice/handler.py` (as
`index.py`) so the stack is self-contained in the lab (no S3 packaging). If you change
`handler.py`, update the inlined copy. The canonical, tested logic is `handler.py` — the test
in `tests/test_handler.py` runs against it.

## Lab constraints baked in

- Region `us-west-2` (Academy stand-in for `ap-south-1`); region is the deploy target.
- `LabRole` ARN passed as a parameter (no IAM-role creation in the Learner Lab).
- All services are serverless/managed and in the Foundation Services set.
- See the README's "Verify in a live lab" section for what still needs a live-session check.
