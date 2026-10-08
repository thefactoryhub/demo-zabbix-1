---
id: REQ-0031
title: Cross-repository disposable marker writes
kind: requirement
status: implemented
type: functional
priority: high
verification_method: test
tags: [disposable, multi_repo]
created_by: admin@example.com
created_at: 2026-10-08T21:15:00Z
---

# REQ-0031 Cross-repository disposable marker writes

## Statement
The disposable multi-repository harness shall resolve the primary repository `demo-zabbix-1` and secondary repository `madeup` from `.ploqa/workspace.json`, write the exact marker text `Multi repo disposable run default-workflow-e2e-ws-08 issue 01` to `disposable-e2e/default-workflow-e2e-ws-08/primary-01.txt` in the primary repository and `disposable-e2e/default-workflow-e2e-ws-08/madeup-01.txt` in the secondary repository, and leave the declared `madeup/sub` submodule untouched.

## Rationale
Disposable workspace validation needs a single task that proves repository resolution, cross-repository writes, and submodule exclusion all work together.

## User story
As a workspace harness author, I want one disposable task to write the same marker into both writable repositories without touching the submodule, so that the workspace layout is exercised safely.

## Acceptance criteria
- The task reads repository locations from `.ploqa/workspace.json`.
- The task writes the exact marker text to the primary repository target file.
- The task writes the exact marker text to the secondary repository target file.
- The task does not modify files under `madeup/sub`.
- The task fails clearly when either repository target cannot be resolved.

## Notes
Implemented by `.ploqa/disposable_multi_repo_marker.py`, `demo-zabbix-1/disposable_multi_repo_marker.py`, and `demo-zabbix-1/tests/disposable_multi_repo_marker`.

Evidence in the code:
- `.ploqa/disposable_multi_repo_marker.py` — resolves repositories from workspace metadata and writes both target files.
- `demo-zabbix-1/disposable_multi_repo_marker.py:19` — marker intent for primary and secondary writes.
- `demo-zabbix-1/tests/disposable_multi_repo_marker` — verifies the target files and confirms `madeup/sub` stays unchanged.

## Discussion

## Attachments
