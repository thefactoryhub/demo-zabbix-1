---
id: TC-1000
title: Multi-repo disposable writes marker files (primary + secondary)
kind: test_case
status: ready
level: system
type: functional
priority: high
automation: automated
requirements: [REQ-0031]
---

# TC-1000 Multi-repo disposable writes marker files (primary + secondary)

## Objective
Verify the disposable multi-repo marker task writes the exact marker string into the primary repo target and the secondary repo target, based on `.ploqa/workspace.json`.

## Preconditions
The repository contains `.ploqa/workspace.json` declaring primary repo `demo-zabbix-1` and secondary repo `madeup`.

## Test data
Marker text: `Multi repo disposable run default-workflow-e2e-ws-08 issue 01`.

## Steps
| # | Action | Expected result |
| --- | --- | --- |
| 1 | Remove any existing `demo-zabbix-1/disposable-e2e/default-workflow-e2e-ws-08/primary-01.txt` and `madeup/disposable-e2e/default-workflow-e2e-ws-08/madeup-01.txt`. | Files do not exist (or are empty). |
| 2 | Run `python3 .ploqa/disposable_multi_repo_marker.py --workspace-json .ploqa/workspace.json`. | Command exits successfully. |
| 3 | Read `demo-zabbix-1/disposable-e2e/default-workflow-e2e-ws-08/primary-01.txt`. | Content equals `Multi repo disposable run default-workflow-e2e-ws-08 issue 01`. |
| 4 | Read `madeup/disposable-e2e/default-workflow-e2e-ws-08/madeup-01.txt`. | Content equals `Multi repo disposable run default-workflow-e2e-ws-08 issue 01`. |

## Postconditions
Marker files exist with the exact expected content.

## Notes
TC-1000.

## Discussion

## Attachments
