"""YAT audit-log microservice — SQS-triggered writer Lambda.

Reads access-event messages from the SQS queue and appends each as an immutable
audit record to the DynamoDB table. Idempotent: event_id is the partition key and a
conditional put means a re-delivered message is skipped rather than duplicated.

Data flow:  HTTP API  ->  SQS  ->  (this Lambda)  ->  DynamoDB

Runtime: python3.12 (boto3 is provided by the Lambda runtime — no dependencies to package).
Environment:
    AUDIT_TABLE   the DynamoDB table name (set by the CloudFormation stack).
"""
import json
import os

import boto3
from botocore.exceptions import ClientError

VALID_COHORTS = {"AU", "IN"}
VALID_EVENT_TYPES = {"login", "course_access", "assessment_view"}
REQUIRED_FIELDS = ("event_id", "occurred_at", "user_ref", "cohort", "event_type", "source_ip")


def _validate(record):
    """Return (ok, reason). Rejects anything that isn't a well-formed access event."""
    for field in REQUIRED_FIELDS:
        if not record.get(field):
            return False, f"missing required field: {field}"
    if record["cohort"] not in VALID_COHORTS:
        return False, f"invalid cohort: {record['cohort']}"
    if record["event_type"] not in VALID_EVENT_TYPES:
        return False, f"invalid event_type: {record['event_type']}"
    return True, ""


def handler(event, context=None):
    """SQS event handler. Returns a small summary (and logs it) for observability."""
    table = boto3.resource("dynamodb").Table(os.environ.get("AUDIT_TABLE", "yat-audit-log"))
    processed = skipped = rejected = 0

    for message in event.get("Records", []):
        try:
            body = json.loads(message["body"])
        except (KeyError, json.JSONDecodeError):
            rejected += 1
            print("reject: message body is not valid JSON")
            continue

        ok, reason = _validate(body)
        if not ok:
            rejected += 1
            print(f"reject: {reason}")
            continue

        item = {field: body[field] for field in REQUIRED_FIELDS}
        try:
            table.put_item(Item=item, ConditionExpression="attribute_not_exists(event_id)")
            processed += 1
        except ClientError as exc:
            if exc.response["Error"]["Code"] == "ConditionalCheckFailedException":
                skipped += 1  # already written — idempotent re-delivery
            else:
                raise  # a real failure: let SQS retry / send to the DLQ

    summary = {"processed": processed, "skipped": skipped, "rejected": rejected}
    print(json.dumps(summary))
    return summary
