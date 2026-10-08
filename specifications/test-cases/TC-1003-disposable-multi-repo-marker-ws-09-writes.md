---
id: TC-1003
title: Multi-repo disposable writes ws-09 marker files (primary + secondary)
kind: test_case
status: ready
level: system
type: functional
priority: high
automation: automated
requirements: [REQ-0032]
---

# TC-1003 Multi-repo disposable writes ws-09 marker files (primary + secondary)

## Objective
Verify that the disposable multi-repo marker task writes the ws-09 marker text into the primary repo target file and the secondary repo target file from `.ploqa/workspace.json`.

## Preconditions
The repository contains `.ploqa/workspace.json` declaring primary repo `demo-zabbix-1` and secondary repo `madeup`.

## Test data
Marker text: `Multi repo disposable run default-workflow-e2e-ws-09 issue 01`.

## Steps
| # | Action | Expected result |
| --- | --- | --- |
| 1 | Remove any existing `demo-zabbix-1/disposable-e2e/default-workflow-e2e-ws-09/primary-01.txt` and `madeup/disposable-e2e/default-workflow-e2e-ws-09/madeup-01.txt`. | Files do not exist (or are empty). |
| 2 | Run `python3 .ploqa/disposable_multi_repo_marker.py --workspace-json .ploqa/workspace.json`. | Command exits successfully. |
| 3 | Read `demo-zabbix-1/disposable-e2e/default-workflow-e2e-ws-09/primary-01.txt`. | Content equals `Multi repo disposable run default-workflow-e2e-ws-09 issue 01`. |
| 4 | Read `madeup/disposable-e2e/default-workflow-e2e-ws-09/madeup-01.txt`. | Content equals `Multi repo disposable run default-workflow-e2e-ws-09 issue 01`. |

## Postconditions
Marker files exist with the exact expected content.

## Notes
TC-1003.

## Discussion

## Attachments
