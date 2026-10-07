---
id: REQ-0011
title: Queue immediate item execution
kind: requirement
status: proposed
parent: REQ-0009
type: functional
priority: high
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0011 Queue immediate item execution

## Statement
The system shall queue immediate check tasks only for permitted active items or discovery rules on monitored hosts, resolving dependent items to executable master items before task creation.

## Rationale
Operators need an on-demand way to refresh supported checks without violating item constraints.

## User story

## Acceptance criteria
- Items or rules that are unreadable, unsupported by type, or not monitored are excluded and reported as errors.
- Valid top-level item ids are sent to `task.create` as `ZBX_TM_TASK_CHECK_NOW` requests.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerItemExecuteNow.php:82` — $items = CArrayHelper::renameObjectsKeys(API::Item()->get([
- `ui/app/controllers/CControllerItemExecuteNow.php:126` — if ($item['status'] != ITEM_STATUS_ACTIVE || $item['hosts'][0]['status'] != HOST_STATUS_MONITORED) {
- `ui/app/controllers/CControllerItemExecuteNow.php:142` — if ($item['type'] == ITEM_TYPE_DEPENDENT) {
- `ui/app/controllers/CControllerItemExecuteNow.php:226` — $result = (bool) API::Task()->create($create_tasks);

## Discussion

## Attachments
