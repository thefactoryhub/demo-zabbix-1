---
kind: test_spec_check
issue: DISPOSABLE-MULTI-REPO-01
issue_id: 61b89a1e-a0e5-4e7b-b4e9-856106e67493
issue_title: "Cross-repository marker #01"
run_id: 2026-10-08T20-59-55-216916-00-00
step_key: TEST_SPEC_CHECK
created_at: 2026-10-08T22:18:52Z
base_commit: d91aa0458f163b69d39747e23fc19df970b512a2
branch: auto/01-cross-repository-marker-01-61b89a
agent_log: /workspace/generated_apps/52434c32-cf43-476e-aee8-2680084f7b6a/.ploqa/logs/backlog/61b89a1e-a0e5-4e7b-b4e9-856106e67493/custom-disposable-multi-repo-01-test-spec-check-1791497890.log
model: gpt-5.4-mini
requirements_touched: [REQ-0031]
test_cases_touched: [TC-1000, TC-1001, TC-1002]
test_run: TR-0002
summary: Linked the disposable multi-repo test cases to REQ-0031, kept the implementation markers in code, and recorded the branch learnings after validating the specs and running the Perl marker test successfully.
---

# Test specification check for DISPOSABLE-MULTI-REPO-01 (run 2026-10-08T20-59-55-216916-00-00)

## Summary
Linked the disposable multi-repo test cases to REQ-0031, kept the implementation markers in code, and recorded the branch learnings after validating the specs and running the Perl marker test successfully.

## Test cases
| ID | Title | Disposition | Result | Motivation |
| --- | --- | --- | --- | --- |
| TC-1000 | Multi-repo disposable writes marker files (primary + secondary) | updated | ok | Covers the primary and secondary marker writes for the disposable multi-repo task. |
| TC-1001 | Multi-repo disposable excludes declared madeup/sub submodule | updated | ok | Covers the submodule exclusion behavior for `madeup/sub` in the disposable task. |
| TC-1002 | Multi-repo disposable fails explicitly when repository resolution fails | updated | ok | Covers the explicit failure paths when repository resolution or target directories are missing. |

## Changes
### TC-1000

```diff
--- a/specifications/test-cases/TC-1000-disposable-multi-repo-marker-writes.md
+++ b/specifications/test-cases/TC-1000-disposable-multi-repo-marker-writes.md
@@ -7,7 +7,7 @@
 type: functional
 priority: high
 automation: automated
-requirements: []
+requirements: [REQ-0031]
 ---
 
 # TC-1000 Multi-repo disposable writes marker files (primary + secondary)
@@ -38,4 +38,3 @@
 ## Discussion
 
 ## Attachments
-
```

### TC-1001

```diff
--- a/specifications/test-cases/TC-1001-disposable-multi-repo-submodule-excluded.md
+++ b/specifications/test-cases/TC-1001-disposable-multi-repo-submodule-excluded.md
@@ -7,7 +7,7 @@
 type: functional
 priority: high
 automation: automated
-requirements: []
+requirements: [REQ-0031]
 ---
 
 # TC-1001 Multi-repo disposable excludes declared madeup/sub submodule
@@ -37,4 +37,3 @@
 ## Discussion
 
 ## Attachments
-
```

### TC-1002

```diff
--- a/specifications/test-cases/TC-1002-disposable-multi-repo-failure-path.md
+++ b/specifications/test-cases/TC-1002-disposable-multi-repo-failure-path.md
@@ -1,34 +1,35 @@
 ---
 id: TC-1002
-title: Multi-repo disposable fails explicitly when secondary cannot be resolved
+title: Multi-repo disposable fails explicitly when repository resolution fails
 kind: test_case
 status: ready
 level: system
 type: functional
 priority: high
 automation: automated
-requirements: []
+requirements: [REQ-0031]
 ---
 
-# TC-1002 Multi-repo disposable fails explicitly when secondary cannot be resolved
+# TC-1002 Multi-repo disposable fails explicitly when repository resolution fails
 
 ## Objective
-Verify the disposable multi-repo marker task errors clearly if the secondary repository cannot be resolved from `.ploqa/workspace.json`.
+Verify that the disposable multi-repo marker task fails clearly when either repository target cannot be resolved from `.ploqa/workspace.json`.
 
 ## Preconditions
-The repository contains `.ploqa/workspace.json` but it is possible to run the task against a modified workspace.json.
+A modified workspace fixture omits the primary or secondary repository entry.
 
 ## Test data
-Workspace variant without repository named `madeup`.
+Temporary workspace JSON with missing repository entries.
 
 ## Steps
 | # | Action | Expected result |
 | --- | --- | --- |
-| 1 | Create a temporary workspace.json that omits the secondary repo entry `madeup`. | Temporary file created. |
-| 2 | Run `python3 .ploqa/disposable_multi_repo_marker.py --workspace-json <temp path>`. | Command fails with a clear error message about missing secondary repo resolution. |
+| 1 | Run the test harness mode that removes the secondary repository entry. | The command fails with an explicit resolution error. |
+| 2 | Run the test harness mode that removes the primary repository entry. | The command fails with an explicit resolution error. |
+| 3 | Run the test harness mode that removes the target directory for either repository. | The command fails with a clear missing-directory error. |
 
 ## Postconditions
-No marker files are written.
+The implementation leaves no partial marker writes behind on failure.
 
 ## Notes
 TC-1002.
@@ -36,4 +37,3 @@
 ## Discussion
 
 ## Attachments
-
```

## Untouched
0 test cases were not touched by this run.
