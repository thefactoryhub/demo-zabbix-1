---
id: TC-1001
title: Multi-repo disposable excludes declared madeup/sub submodule
kind: test_case
status: ready
level: system
type: functional
priority: high
automation: automated
requirements: []
---

# TC-1001 Multi-repo disposable excludes declared madeup/sub submodule

## Objective
Verify that the disposable multi-repo marker task does not traverse or modify files under the declared secondary submodule path `madeup/sub`.

## Preconditions
The repository contains `madeup/.gitmodules` that declares submodule `sub` under `madeup/sub`.

## Test data
Sentinel file: `madeup/sub/sub.txt`.

## Steps
| # | Action | Expected result |
| --- | --- | --- |
| 1 | Record the current content of `madeup/sub/sub.txt` into test output (or keep it unchanged). | Baseline content is known. |
| 2 | Run `python3 .ploqa/disposable_multi_repo_marker.py --workspace-json .ploqa/workspace.json` (happy path). | Command exits successfully. |
| 3 | Read `madeup/sub/sub.txt`. | Content is unchanged. |

## Postconditions
Files under `madeup/sub` remain unchanged.

## Notes
TC-1001.

## Discussion

## Attachments

