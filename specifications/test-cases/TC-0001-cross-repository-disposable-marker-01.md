---
id: TC-0001
title: Cross-repository disposable marker #01
kind: test_case
status: ready
level: system
type: functional
priority: high
automation: automated
requirements: [REQ-0031]
---

# TC-0001 Cross-repository disposable marker #01

## Objective
Verify the disposable multi-repository harness writes the exact marker text to the primary and secondary repositories and does not modify the declared `madeup/sub` submodule boundary.

## Preconditions
- The workspace layout is defined in `.ploqa/workspace.json`.
- Disposable marker run script `.ploqa/disposable_multi_repo_marker_run.py` is available.

## Test data

## Steps
| # | Action | Expected result |
| --- | --- | --- |
| 1 | Run the disposable marker writer script `.ploqa/disposable_multi_repo_marker_run.py` | Exit code is 0 and both expected marker files are created/updated with the exact text. |
| 2 | Run the verifier `.ploqa/verify_disposable_multi_repo_marker.py` | Exit code is 0 (markers correct; no changes under `madeup/sub`; no forbidden command invocations). |

## Postconditions
- `demo-zabbix-1/disposable-e2e/default-workflow-e2e-ws-07/primary-01.txt` contains `Multi repo disposable run default-workflow-e2e-ws-07 issue 01`.
- `madeup/disposable-e2e/default-workflow-e2e-ws-07/madeup-01.txt` contains the same marker text.
- No files under `madeup/sub` are modified.

## Notes

## Discussion

## Attachments

