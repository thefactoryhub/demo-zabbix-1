---
id: REQ-0003
title: Authenticate form logins and redirect users
kind: requirement
status: proposed
parent: REQ-0002
type: functional
priority: critical
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0003 Authenticate form logins and redirect users

## Statement
The system shall authenticate interactive users from the login form, store the authenticated session id, and redirect successful non-MFA logins to the requested URL, saved redirect URL, or first permitted menu entry.

## Rationale
Users need a working primary login flow that lands them in the application after authentication.

## User story

## Acceptance criteria
- When `enter` is submitted with valid credentials, the session stores the authenticated `sessionid`.
- When MFA is not required, a successful login redirects to the first available target from request, saved redirect, or menu default.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/index.php:71` — if (hasRequest('enter') && CWebUser::login(getRequest('name', ZBX_GUEST_USER), getRequest('password', ''))) {
- `ui/index.php:72` — CSessionHelper::set('sessionid', CWebUser::$data['sessionid']);
- `ui/index.php:106` — $redirect = array_filter([$request, $redirect['url'], CMenuHelper::getFirstUrl()]);
- `ui/index.php:112` — $response->redirect();

## Discussion

## Attachments
