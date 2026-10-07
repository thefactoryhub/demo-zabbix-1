---
id: REQ-0010
title: Create monitored hosts
kind: requirement
status: proposed
parent: REQ-0009
type: functional
priority: critical
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0010 Create monitored hosts

## Statement
The system shall validate and create hosts with monitoring status, host groups, interfaces, monitoring target, tags, templates, macros, inventory settings, TLS settings, and optional value maps.

## Rationale
Host creation is the basis for onboarding monitored assets.

## User story

## Acceptance criteria
- Host creation validates host identity and interface fields before calling the host API.
- On success, the controller creates the host and then creates any supplied value maps for the new host.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/app/controllers/CControllerHostCreate.php:37` — return ['object', 'api_uniq' => $api_uniq, 'fields' => [
- `ui/app/controllers/CControllerHostCreate.php:315` — $host = [
- `ui/app/controllers/CControllerHostCreate.php:367` — $result = API::Host()->create($host);
- `ui/app/controllers/CControllerHostCreate.php:451` — if ($valuemaps && !API::ValueMap()->create($valuemaps)) {

## Discussion

## Attachments
