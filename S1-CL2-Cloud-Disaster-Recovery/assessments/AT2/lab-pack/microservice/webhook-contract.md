# Audit-log webhook contract

The single integration point between the LMS (the event producer) and the audit-log
microservice. The LMS knows only this contract; everything behind it can change
independently. The same generic contract is reused by the Accounting practice project —
only the payload values differ.

## Endpoint

```
POST  {ApiEndpoint}        # e.g. https://abc123.execute-api.us-west-2.amazonaws.com/events
Content-Type: application/json
```

`{ApiEndpoint}` is an Output of the deployed stack.

## Request body

```json
{
  "event_id":    "3f9a1c2e-...",        // unique id for the event (UUID) — the idempotency key
  "occurred_at": "2026-06-07T01:23:45Z", // ISO-8601 UTC timestamp
  "user_ref":    "u-48217",              // opaque user reference (not the user's name)
  "cohort":      "IN",                   // "AU" or "IN"  (IN = the India cohort, residency-bound)
  "event_type":  "login",                // "login" | "course_access" | "assessment_view"
  "source_ip":   "203.0.113.7"           // the client IP the event came from
}
```

All six fields are required. `cohort` and `event_type` must be one of the allowed values.

## Response

| Code | Meaning |
|---|---|
| `200` | Accepted and queued for writing (HTTP API → SQS returns the SQS SendMessage result). |
| `400` | Malformed request (rejected by the API). |

The write to the audit store happens asynchronously: the API enqueues the event, and the
writer Lambda appends it to DynamoDB. A re-sent event with the same `event_id` is **not**
duplicated (idempotent write).

## Notes for the build

- The India-cohort (`"cohort": "IN"`) events are the ones the data-residency requirement
  keeps in the India region — the whole stack is deployed there (`us-west-2` in the lab,
  `ap-south-1` in production).
- Signing: a production deployment would sign the request (e.g. an HMAC header the API
  validates). For the lab the API accepts the JSON directly; signing is noted as an
  extension, not required for a Satisfactory outcome.
