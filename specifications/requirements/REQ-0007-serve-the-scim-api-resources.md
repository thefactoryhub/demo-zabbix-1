---
id: REQ-0007
title: Serve the SCIM API resources
kind: requirement
status: proposed
parent: REQ-0005
type: interface
priority: medium
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0007 Serve the SCIM API resources

## Statement
The system shall expose a SCIM API endpoint that routes `users`, `groups`, and `serviceproviderconfig` resources through the SCIM client and service factory.

## Rationale
Identity integrations need standardized provisioning endpoints.

## User story

## Acceptance criteria
- The SCIM endpoint initializes the application in API mode and executes requests through the SCIM handler.
- The service factory registers handlers for `users`, `groups`, and `serviceproviderconfig`.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/api_scim.php:32` — APP::getInstance()->run(APP::EXEC_MODE_API);
- `ui/api_scim.php:35` — $client->setServiceFactory(new CRegistryFactory([
- `ui/api_scim.php:36` — 'users' => User::class,
- `ui/api_scim.php:42` — $response = $scim->execute($client, $request);

## Discussion

## Attachments
