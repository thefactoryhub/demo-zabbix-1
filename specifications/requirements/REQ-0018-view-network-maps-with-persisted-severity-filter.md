---
id: REQ-0018
title: View network maps with persisted severity filter
kind: requirement
status: proposed
parent: REQ-0016
type: functional
priority: medium
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0018 View network maps with persisted severity filter

## Statement
The system shall open a network map by name, explicit map id, or the user's saved map selection, and persist a per-map severity filter in the user profile.

## Rationale
Users need map navigation that remembers the selected map and filtering threshold.

## User story

## Acceptance criteria
- If no map is specified, the controller uses the saved map id; if no accessible map exists it redirects to the map list.
- When a severity filter is supplied or saved, the response includes the active severity value, severity choices, and map editability information.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerMapView.php:49` — if ($this->hasInput('mapname')) {
- `ui/app/controllers/CControllerMapView.php:59` — $options['sysmapids'] = [CProfile::get('web.maps.sysmapid', 0)];
- `ui/app/controllers/CControllerMapView.php:86` — CProfile::update('web.maps.sysmapid', $this->sysmapid, PROFILE_TYPE_ID);
- `ui/app/controllers/CControllerMapView.php:100` — CProfile::update('web.maps.severity_min', $severity_min, PROFILE_TYPE_INT, $this->sysmapid);

## Discussion

## Attachments
