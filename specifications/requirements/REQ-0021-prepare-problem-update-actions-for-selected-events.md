---
id: REQ-0021
title: Prepare problem update actions for selected events
kind: requirement
status: proposed
parent: REQ-0020
type: functional
priority: high
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0021 Prepare problem update actions for selected events

## Statement
The system shall prepare the problem update dialog for selected trigger events, exposing acknowledgements, comments, severity changes, close, suppress, unsuppress, and rank-change actions only when the selected events and user permissions allow them.

## Rationale
Incident operators need the UI to reflect what updates are actually allowed for the current problem set.

## User story

## Acceptance criteria
- The dialog only accepts trigger event ids and checks that every selected event exists and that the user has at least one problem-update permission.
- The response computes flags such as closable, suppressible, unsuppressible, and rank-change eligibility from event state, suppression data, trigger editability, and permissions.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerAcknowledgeEdit.php:25` — 'eventids' => required|array_db acknowledges.eventid',
- `ui/app/controllers/CControllerAcknowledgeEdit.php:54` — if (!$this->checkAccess(CRoleHelper::ACTIONS_ACKNOWLEDGE_PROBLEMS)
- `ui/app/controllers/CControllerAcknowledgeEdit.php:104` — $events = API::Event()->get([
- `ui/app/controllers/CControllerAcknowledgeEdit.php:183` — if ($event['r_eventid'] != 0 || $event['value'] == TRIGGER_VALUE_FALSE) {

## Discussion

## Attachments
