---
id: REQ-0032
title: Cross-repository disposable marker writes for ws-09
kind: requirement
status: implemented
type: functional
priority: high
verification_method: test
tags: [disposable, multi_repo]
created_by: admin@example.com
created_at: 2026-10-08T23:16:34Z
---

# REQ-0032 Cross-repository disposable marker writes for ws-09

## Statement
The disposable multi-repository harness shall resolve the primary repository `demo-zabbix-1` and secondary repository `madeup` from `.ploqa/workspace.json`, write the exact marker text `Multi repo disposable run default-workflow-e2e-ws-09 issue 01` to `disposable-e2e/default-workflow-e2e-ws-09/primary-01.txt` in the primary repository and `disposable-e2e/default-workflow-e2e-ws-09/madeup-01.txt` in the secondary repository, and leave the declared `madeup/sub` submodule untouched.

## Rationale
Disposable workspace validation needs a single task that proves repository resolution, cross-repository writes, and submodule exclusion all work together for the ws-09 disposable variant.

## User story
As a workspace harness author, I want one disposable task to write the same marker into both writable repositories without touching the submodule, so that the workspace layout is exercised safely.

## Acceptance criteria
- The task reads repository locations from `.ploqa/workspace.json`.
- The task writes the exact marker text to the primary repository target file.
- The task writes the exact marker text to the secondary repository target file.
- The task does not modify files under `madeup/sub`.
- The task fails clearly when either repository target cannot be resolved.

## Notes
Implemented by `demo-zabbix-1/disposable_multi_repo_marker.py` and `demo-zabbix-1/tests/disposable_multi_repo_marker`.

Evidence in the code:
- `demo-zabbix-1/disposable_multi_repo_marker.py` — resolves repositories from workspace metadata and writes both target files.
- `demo-zabbix-1/tests/disposable_multi_repo_marker` — verifies the ws-09 target files and confirms `madeup/sub` stays unchanged.

## Discussion

## Attachments
