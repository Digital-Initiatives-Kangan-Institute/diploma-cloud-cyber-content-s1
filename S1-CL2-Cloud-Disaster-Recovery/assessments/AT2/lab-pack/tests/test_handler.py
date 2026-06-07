"""Local test of the audit-writer Lambda — runs with NO AWS account.

A small in-test fake stands in for the DynamoDB table (implementing just what the handler
uses: a conditional put_item, plus get_item/scan for assertions), so the handler's real
logic — validation, idempotency, batch counting — executes here, before it is ever
deployed to the AWS lab.

Run from the lab-pack folder (with the venv active or via its python):
    python -m pytest
"""
import json
import sys
from pathlib import Path

from botocore.exceptions import ClientError

# Import the handler from ../microservice
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "microservice"))
import handler  # noqa: E402


# ---- a minimal DynamoDB table fake (only what the handler calls) ----
class FakeTable:
    def __init__(self):
        self.items = {}

    def put_item(self, Item, ConditionExpression=None):
        key = Item["event_id"]
        if ConditionExpression == "attribute_not_exists(event_id)" and key in self.items:
            raise ClientError(
                {"Error": {"Code": "ConditionalCheckFailedException", "Message": "exists"}},
                "PutItem",
            )
        self.items[key] = Item

    def get_item(self, Key):
        item = self.items.get(Key["event_id"])
        return {"Item": item} if item else {}

    def scan(self):
        return {"Items": list(self.items.values()), "Count": len(self.items)}


class FakeResource:
    def __init__(self, table):
        self._table = table

    def Table(self, _name):
        return self._table


import pytest  # noqa: E402


@pytest.fixture
def table(monkeypatch):
    t = FakeTable()
    monkeypatch.setattr(handler.boto3, "resource", lambda _svc: FakeResource(t))
    return t


def _event(*bodies):
    return {"Records": [{"body": json.dumps(b)} for b in bodies]}


def _valid(**overrides):
    base = {
        "event_id": "e1", "occurred_at": "2026-06-07T00:00:00Z", "user_ref": "u1",
        "cohort": "IN", "event_type": "login", "source_ip": "1.2.3.4",
    }
    base.update(overrides)
    return base


def test_valid_event_is_written(table):
    assert handler.handler(_event(_valid())) == {"processed": 1, "skipped": 0, "rejected": 0}
    assert table.get_item(Key={"event_id": "e1"})["Item"]["cohort"] == "IN"


def test_duplicate_event_id_is_idempotent(table):
    handler.handler(_event(_valid(event_id="dup")))
    assert handler.handler(_event(_valid(event_id="dup"))) == {"processed": 0, "skipped": 1, "rejected": 0}
    assert table.scan()["Count"] == 1


def test_invalid_cohort_is_rejected(table):
    assert handler.handler(_event(_valid(event_id="bad", cohort="ZZ"))) == {"processed": 0, "skipped": 0, "rejected": 1}
    assert table.scan()["Count"] == 0


def test_missing_field_is_rejected(table):
    bad = _valid(event_id="nofield")
    del bad["source_ip"]
    assert handler.handler(_event(bad)) == {"processed": 0, "skipped": 0, "rejected": 1}


def test_malformed_json_is_rejected(table):
    assert handler.handler({"Records": [{"body": "{not json"}]}) == {"processed": 0, "skipped": 0, "rejected": 1}


def test_batch_mixed(table):
    result = handler.handler(_event(
        _valid(event_id="ok1"),
        _valid(event_id="ok2", cohort="AU"),
        _valid(event_id="bad", event_type="nope"),
    ))
    assert result == {"processed": 2, "skipped": 0, "rejected": 1}
    assert table.scan()["Count"] == 2
