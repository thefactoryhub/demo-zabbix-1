---
id: REQ-0024
title: Test media types before use
kind: requirement
status: proposed
parent: REQ-0022
type: functional
priority: medium
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0024 Test media types before use

## Statement
The system shall validate and test enabled media types, transform type-specific parameters for execution, and return success or failure details including parsed webhook responses and debug logs when available.

## Rationale
Administrators need to verify delivery channel configuration before relying on it in actions and reports.

## User story

## Acceptance criteria
- Disabled or inaccessible media types are rejected before any test is executed.
- For supported media types, the controller builds the type-specific payload, sends a test request through the server, and returns success, error, debug, and webhook-response data as applicable.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerMediatypeTestSend.php:91` — $mediatypes = API::MediaType()->get([
- `ui/app/controllers/CControllerMediatypeTestSend.php:104` — if ($this->mediatype['status'] != MEDIA_STATUS_ACTIVE) {
- `ui/app/controllers/CControllerMediatypeTestSend.php:118` — if ($params['type'] == MEDIA_TYPE_EXEC) {
- `ui/app/controllers/CControllerMediatypeTestSend.php:133` — $result = $server->testMediaType($params, CSessionHelper::getId());

## Discussion

## Attachments
