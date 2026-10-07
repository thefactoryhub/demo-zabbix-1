---
id: REQ-0004
title: Redirect MFA-enabled users into MFA confirmation
kind: requirement
status: proposed
parent: REQ-0002
type: functional
priority: high
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0004 Redirect MFA-enabled users into MFA confirmation

## Statement
The system shall divert successful logins for users with MFA configured to the MFA confirmation flow and preserve the requested destination for that flow.

## Rationale
Accounts configured for MFA must complete the additional verification step before full access is granted.

## User story

## Acceptance criteria
- If the authenticated user has an `mfaid`, the session stores `confirmid` and redirects to `index_mfa.php`.
- If the original request target is present, the MFA redirect includes it as the `request` argument.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/index.php:81` — if (CWebUser::$data['mfaid']) {
- `ui/index.php:82` — CSessionHelper::set('confirmid', CWebUser::$data['sessionid']);
- `ui/index.php:89` — $mfa_url = (new CUrl('index_mfa.php'));
- `ui/index.php:95` — redirect($mfa_url->toString());

## Discussion

## Attachments
