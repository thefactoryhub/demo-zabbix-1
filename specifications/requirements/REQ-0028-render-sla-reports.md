---
id: REQ-0028
title: Render SLA reports
kind: requirement
status: proposed
parent: REQ-0026
type: functional
priority: medium
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0028 Render SLA reports

## Statement
The system shall validate and persist SLA report filters, resolve the selected enabled SLA and optional service, validate the requested date range, and fetch paged SLI data for the resulting service set.

## Rationale
Service owners need SLA visibility scoped by service and reporting period.

## User story

## Acceptance criteria
- SLA report filter selections are stored in the user profile and invalid SLA or service references are cleared.
- When a valid enabled SLA and date range are present, the controller loads services, paginates them, and requests SLI data for the selected period.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerSlaReportList.php:56` — if ($this->hasInput('filter_set')) {
- `ui/app/controllers/CControllerSlaReportList.php:80` — $slas = API::Sla()->get([
- `ui/app/controllers/CControllerSlaReportList.php:172` — if ($period_from !== null && $period_to !== null && $period_to <= $period_from) {
- `ui/app/controllers/CControllerSlaReportList.php:220` — $data['sli'] = API::Sla()->getSli($options);

## Discussion

## Attachments
