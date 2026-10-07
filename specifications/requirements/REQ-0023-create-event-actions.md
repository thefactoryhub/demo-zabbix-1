---
id: REQ-0023
title: Create event actions
kind: requirement
status: proposed
parent: REQ-0022
type: functional
priority: high
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0023 Create event actions

## Statement
The system shall create actions for trigger, discovery, autoregistration, internal, and service event sources by normalizing action filters and operation payloads for the selected source before calling the action API.

## Rationale
Operational automation depends on consistent action definitions across event sources.

## User story

## Acceptance criteria
- Action creation validates the allowed event source, action identity, conditions, operations, and source-specific flags.
- Before API creation, the controller removes or reshapes operation fields that do not apply to the selected event source.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerActionCreate.php:25` — 'eventsource' => required|db actions.eventsource|in '.implode(',', [
- `ui/app/controllers/CControllerActionCreate.php:100` — if ($filter['conditions']) {
- `ui/app/controllers/CControllerActionCreate.php:129` — foreach (['operations', 'recovery_operations', 'update_operations'] as $operation_group) {
- `ui/app/controllers/CControllerActionCreate.php:250` — $result = API::Action()->create($action);

## Discussion

## Attachments
