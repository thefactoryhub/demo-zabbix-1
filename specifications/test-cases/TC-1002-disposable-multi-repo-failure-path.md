---
id: TC-1002
title: Multi-repo disposable fails explicitly when repository resolution fails
kind: test_case
status: ready
level: system
type: functional
priority: high
automation: automated
requirements: [REQ-0031]
---

# TC-1002 Multi-repo disposable fails explicitly when repository resolution fails

## Objective
Verify that the disposable multi-repo marker task fails clearly when either repository target cannot be resolved from `.ploqa/workspace.json`.

## Preconditions
A modified workspace fixture omits the primary or secondary repository entry.

## Test data
Temporary workspace JSON with missing repository entries.

## Steps
| # | Action | Expected result |
| --- | --- | --- |
| 1 | Run the test harness mode that removes the secondary repository entry. | The command fails with an explicit resolution error. |
| 2 | Run the test harness mode that removes the primary repository entry. | The command fails with an explicit resolution error. |
| 3 | Run the test harness mode that removes the target directory for either repository. | The command fails with a clear missing-directory error. |

## Postconditions
The implementation leaves no partial marker writes behind on failure.

## Notes
TC-1002.

## Discussion

## Attachments
