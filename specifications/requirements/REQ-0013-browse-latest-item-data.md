---
id: REQ-0013
title: Browse latest item data
kind: requirement
status: proposed
parent: REQ-0012
type: functional
priority: high
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0013 Browse latest item data

## Statement
The system shall display the Latest data view with validated filters, persisted tab-filter state, subfilters, sorting, paging, and a per-user refresh interval.

## Rationale
Operators need a navigable current-value view for monitored items.

## User story

## Acceptance criteria
- The Latest data controller validates group, host, tag, state, sort, page, and subfilter inputs before rendering.
- The rendered response includes persisted filter tabs, paged items, active subfilters, and the user's refresh interval.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerLatestView.php:27` — $fields = [
- `ui/app/controllers/CControllerLatestView.php:123` — $profile = (new CTabFilterProfile('web.monitoring.latest', static::FILTER_FIELDS_DEFAULT))->read();
- `ui/app/controllers/CControllerLatestView.php:177` — $paging = CPagerHelper::paginate($this->getInput('page', 1), $prepared_data['items'], ZBX_SORT_UP, $view_url);
- `ui/app/controllers/CControllerLatestView.php:193` — 'refresh_interval' => CWebUser::getRefresh() * 1000,

## Discussion

## Attachments
