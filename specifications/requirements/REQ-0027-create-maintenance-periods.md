---
id: REQ-0027
title: Create maintenance periods
kind: requirement
status: proposed
parent: REQ-0026
type: functional
priority: high
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0027 Create maintenance periods

## Statement
The system shall validate and create maintenance periods with active dates, one or more time periods, selected host groups or hosts or triggers, and optional event-name and tag filters.

## Rationale
Operators need a structured way to declare planned maintenance coverage and filtering.

## User story

## Acceptance criteria
- Maintenance creation rejects requests without required dates, time periods, or any selected target.
- Successful requests transform the submitted targets and time periods and create the maintenance period through the API.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerMaintenanceCreate.php:39` — 'timeperiods' => ['objects', 'required', 'not_empty',
- `ui/app/controllers/CControllerMaintenanceCreate.php:82` — ['array', 'required', 'not_empty', 'field' => ['db maintenances_groups.groupid'],
- `ui/app/controllers/CControllerMaintenanceCreate.php:148` — $maintenance = [
- `ui/app/controllers/CControllerMaintenanceCreate.php:161` — $result = API::Maintenance()->create($maintenance);

## Discussion

## Attachments
