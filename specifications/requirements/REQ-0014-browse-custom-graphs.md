---
id: REQ-0014
title: Browse custom graphs
kind: requirement
status: proposed
parent: REQ-0012
type: functional
priority: medium
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0014 Browse custom graphs

## Statement
The system shall display custom graphs for selected hosts and time ranges, persist graph filters and tag subfilters, and ignore host ids the user cannot read.

## Rationale
Users need filtered graph browsing over a chosen time window without exposing unreadable hosts.

## User story

## Acceptance criteria
- The controller validates time selector, host, graph-name, view mode, and tag subfilter inputs.
- When filters are applied, unreadable hosts are removed, graphs are subfiltered and paged, and chart payloads are returned for rendering.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerChartsView.php:27` — $fields = [
- `ui/app/controllers/CControllerChartsView.php:76` — CProfile::updateArray('web.charts.subfilter.tagnames', $this->getInput('subfilter_tagnames', []), PROFILE_TYPE_STR);
- `ui/app/controllers/CControllerChartsView.php:99` — if (count($data['filter_hostids']) != count($data['ms_hosts'])) {
- `ui/app/controllers/CControllerChartsView.php:137` — $data['charts'] = $this->getCharts($graphs);

## Discussion

## Attachments
