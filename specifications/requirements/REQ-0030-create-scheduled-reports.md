---
id: REQ-0030
title: Create scheduled reports
kind: requirement
status: proposed
parent: REQ-0029
type: functional
priority: medium
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0030 Create scheduled reports

## Statement
The system shall validate and create scheduled dashboard reports with a target dashboard, reporting period, repeat cycle, start time, optional active dates, and user or user-group subscriptions.

## Rationale
Teams need recurring delivery of dashboard content to explicit recipients.

## User story

## Acceptance criteria
- Scheduled report creation validates the dashboard, schedule fields, optional weekly repeat days, and a non-empty subscriptions list.
- Successful requests convert the schedule and subscriptions into report, user, and user-group payloads and create the report through the API.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerScheduledReportCreate.php:49` — return ['object', 'api_uniq' => $api_uniq, 'fields' => [
- `ui/app/controllers/CControllerScheduledReportCreate.php:74` — 'subscriptions' => ['objects', 'required', 'not_empty', 'fields' => [
- `ui/app/controllers/CControllerScheduledReportCreate.php:107` — $report['start_time'] = ($this->getInput('hours') * SEC_PER_HOUR) + ($this->getInput('minutes') * SEC_PER_MIN);
- `ui/app/controllers/CControllerScheduledReportCreate.php:135` — $result = API::Report()->create($report);

## Discussion

## Attachments
