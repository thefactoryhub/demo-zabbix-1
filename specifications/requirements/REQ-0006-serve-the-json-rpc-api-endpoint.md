---
id: REQ-0006
title: Serve the JSON-RPC API endpoint
kind: requirement
status: proposed
parent: REQ-0005
type: interface
priority: high
review_status: new
created_by: admin@example.com
created_at: 2026-10-07T23:10:37Z
---

# REQ-0006 Serve the JSON-RPC API endpoint

## Statement
The system shall expose a JSON-RPC API endpoint that accepts supported JSON content types, rejects unsupported content types with HTTP 412, executes requests in API mode, and returns JSON responses.

## Rationale
Automations and external integrations need a stable machine-facing API surface.

## User story

## Acceptance criteria
- Requests with `Content-Type` outside the allowed JSON list receive HTTP 412 and are not executed.
- Accepted requests run through `CJsonRpc` in API mode and return `application/json` output.

## Notes
Proposed by an agent (job a848142f).

Evidence in the code:
- `ui/api_jsonrpc.php:29` — $allowed_content = [
- `ui/api_jsonrpc.php:39` — if (!isset($allowed_content[$content_type])) {
- `ui/api_jsonrpc.php:46` — header('Content-Type: application/json');
- `ui/api_jsonrpc.php:57` — $jsonRpc = new CJsonRpc($apiClient, $data);

## Discussion

## Attachments
