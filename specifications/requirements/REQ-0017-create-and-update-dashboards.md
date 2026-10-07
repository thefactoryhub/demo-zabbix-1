---
id: REQ-0017
title: Create and update dashboards
kind: requirement
status: proposed
parent: REQ-0016
type: functional
priority: high
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0017 Create and update dashboards

## Statement
The system shall validate dashboard sharing and page/widget structure and then create or update dashboards composed of pages and widgets, including preserving inaccessible existing widgets during updates.

## Rationale
Dashboards are a primary visualization surface and must persist structured layout data safely.

## User story

## Acceptance criteria
- Dashboard requests are rejected when sharing data or page/widget validation fails.
- Successful requests assemble dashboard pages and widgets into API payloads and call either `dashboard.create` or `dashboard.update`.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerDashboardUpdate.php:56` — $sharing_errors = $this->validateSharing();
- `ui/app/controllers/CControllerDashboardUpdate.php:60` — ] = CDashboardHelper::validateDashboardPages($this->getInput('pages', []));
- `ui/app/controllers/CControllerDashboardUpdate.php:152` — if ($widget['type'] !== ZBX_WIDGET_INACCESSIBLE) {
- `ui/app/controllers/CControllerDashboardUpdate.php:202` — $result = $this->db_dashboard !== null && !$this->hasInput('clone')

## Discussion

## Attachments
