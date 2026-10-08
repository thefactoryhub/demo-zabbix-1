---
id: TC-1002
title: Multi-repo disposable fails explicitly when secondary cannot be resolved
kind: test_case
status: ready
level: system
type: functional
priority: high
automation: automated
requirements: []
---

# TC-1002 Multi-repo disposable fails explicitly when secondary cannot be resolved

## Objective
Verify the disposable multi-repo marker task errors clearly if the secondary repository cannot be resolved from `.ploqa/workspace.json`.

## Preconditions
The repository contains `.ploqa/workspace.json` but it is possible to run the task against a modified workspace.json.

## Test data
Workspace variant without repository named `madeup`.

## Steps
| # | Action | Expected result |
| --- | --- | --- |
| 1 | Create a temporary workspace.json that omits the secondary repo entry `madeup`. | Temporary file created. |
| 2 | Run `python3 .ploqa/disposable_multi_repo_marker.py --workspace-json <temp path>`. | Command fails with a clear error message about missing secondary repo resolution. |

## Postconditions
No marker files are written.

## Notes
TC-1002.

## Discussion

## Attachments

