---
kind: test_spec_check
issue: DISPOSABLE-MULTI-REPO-01
issue_id: a64c5dcd-34fd-4f3e-a22e-6b9ab40fe3a8
issue_title: "Cross-repository marker #01"
run_id: 2026-10-08T23-16-34-343477-00-00
step_key: TEST_SPEC_CHECK
created_at: 2026-10-08T23:28:40Z
base_commit: 4ecb1e2a4012cd4675ca34e3ace0c24f2f00d411
branch: auto/01-cross-repository-marker-01-a64c5d
agent_log: /workspace/generated_apps/df13ca62-9449-4391-8707-f1003b95827d/.ploqa/logs/backlog/a64c5dcd-34fd-4f3e-a22e-6b9ab40fe3a8/custom-disposable-multi-repo-01-test-spec-check-1791502072.log
model: gpt-5.4-mini
requirements_touched: [REQ-0032]
test_cases_touched: [TC-1003, TC-1004, TC-1005]
test_run: TR-0003
summary: Added ws-09 test coverage for the cross-repository disposable marker flow by creating TC-1003/TC-1004/TC-1005, tying them to REQ-0032, and ensuring the implementation carries matching TC markers. Also recorded branch learnings in the requested backlog note.
---

# Test specification check for DISPOSABLE-MULTI-REPO-01 (run 2026-10-08T23-16-34-343477-00-00)

## Summary
Added ws-09 test coverage for the cross-repository disposable marker flow by creating TC-1003/TC-1004/TC-1005, tying them to REQ-0032, and ensuring the implementation carries matching TC markers. Also recorded branch learnings in the requested backlog note.

## Test cases
| ID | Title | Disposition | Result | Motivation |
| --- | --- | --- | --- | --- |
| TC-1003 | Multi-repo disposable writes ws-09 marker files (primary + secondary) | created | ok | Covers the ws-09 happy path for writing the primary and secondary marker files with the exact expected text. |
| TC-1004 | Multi-repo disposable excludes declared madeup/sub submodule for ws-09 | created | ok | Covers the ws-09 submodule exclusion behavior so `madeup/sub` stays untouched during the disposable run. |
| TC-1005 | Multi-repo disposable fails explicitly when ws-09 repository resolution fails | created | ok | Covers the ws-09 failure path so missing repository resolution or missing target directories fail explicitly and do not leave partial writes behind. |

## Changes
### TC-1003

```diff
--- /dev/null
+++ b/specifications/test-cases/TC-1003-disposable-multi-repo-marker-ws-09-writes.md
@@ -0,0 +1,40 @@
+---
+id: TC-1003
+title: Multi-repo disposable writes ws-09 marker files (primary + secondary)
+kind: test_case
+status: ready
+level: system
+type: functional
+priority: high
+automation: automated
+requirements: [REQ-0032]
+---
+
+# TC-1003 Multi-repo disposable writes ws-09 marker files (primary + secondary)
+
+## Objective
+Verify that the disposable multi-repo marker task writes the ws-09 marker text into the primary repo target file and the secondary repo target file from `.ploqa/workspace.json`.
+
+## Preconditions
+The repository contains `.ploqa/workspace.json` declaring primary repo `demo-zabbix-1` and secondary repo `madeup`.
+
+## Test data
+Marker text: `Multi repo disposable run default-workflow-e2e-ws-09 issue 01`.
+
+## Steps
+| # | Action | Expected result |
+| --- | --- | --- |
+| 1 | Remove any existing `demo-zabbix-1/disposable-e2e/default-workflow-e2e-ws-09/primary-01.txt` and `madeup/disposable-e2e/default-workflow-e2e-ws-09/madeup-01.txt`. | Files do not exist (or are empty). |
+| 2 | Run `python3 .ploqa/disposable_multi_repo_marker.py --workspace-json .ploqa/workspace.json`. | Command exits successfully. |
+| 3 | Read `demo-zabbix-1/disposable-e2e/default-workflow-e2e-ws-09/primary-01.txt`. | Content equals `Multi repo disposable run default-workflow-e2e-ws-09 issue 01`. |
+| 4 | Read `madeup/disposable-e2e/default-workflow-e2e-ws-09/madeup-01.txt`. | Content equals `Multi repo disposable run default-workflow-e2e-ws-09 issue 01`. |
+
+## Postconditions
+Marker files exist with the exact expected content.
+
+## Notes
+TC-1003.
+
+## Discussion
+
+## Attachments
```

### TC-1004

```diff
--- /dev/null
+++ b/specifications/test-cases/TC-1004-disposable-multi-repo-submodule-excluded-ws-09.md
@@ -0,0 +1,39 @@
+---
+id: TC-1004
+title: Multi-repo disposable excludes declared madeup/sub submodule for ws-09
+kind: test_case
+status: ready
+level: system
+type: functional
+priority: high
+automation: automated
+requirements: [REQ-0032]
+---
+
+# TC-1004 Multi-repo disposable excludes declared madeup/sub submodule for ws-09
+
+## Objective
+Verify that the ws-09 disposable multi-repo marker task does not traverse or modify files under the declared secondary submodule path `madeup/sub`.
+
+## Preconditions
+The repository contains `madeup/.gitmodules` that declares submodule `sub` under `madeup/sub`.
+
+## Test data
+Sentinel file: `madeup/sub/sub.txt`.
+
+## Steps
+| # | Action | Expected result |
+| --- | --- | --- |
+| 1 | Record the current content of `madeup/sub/sub.txt` into test output (or keep it unchanged). | Baseline content is known. |
+| 2 | Run `python3 .ploqa/disposable_multi_repo_marker.py --workspace-json .ploqa/workspace.json` (happy path). | Command exits successfully. |
+| 3 | Read `madeup/sub/sub.txt`. | Content is unchanged. |
+
+## Postconditions
+Files under `madeup/sub` remain unchanged.
+
+## Notes
+TC-1004.
+
+## Discussion
+
+## Attachments
```

### TC-1005

```diff
--- /dev/null
+++ b/specifications/test-cases/TC-1005-disposable-multi-repo-failure-path-ws-09.md
@@ -0,0 +1,39 @@
+---
+id: TC-1005
+title: Multi-repo disposable fails explicitly when ws-09 repository resolution fails
+kind: test_case
+status: ready
+level: system
+type: functional
+priority: high
+automation: automated
+requirements: [REQ-0032]
+---
+
+# TC-1005 Multi-repo disposable fails explicitly when ws-09 repository resolution fails
+
+## Objective
+Verify that the ws-09 disposable multi-repo marker task fails clearly when either repository target cannot be resolved from `.ploqa/workspace.json`.
+
+## Preconditions
+A modified workspace fixture omits the primary or secondary repository entry.
+
+## Test data
+Temporary workspace JSON with missing repository entries.
+
+## Steps
+| # | Action | Expected result |
+| --- | --- | --- |
+| 1 | Run the test harness mode that removes the secondary repository entry. | The command fails with an explicit resolution error. |
+| 2 | Run the test harness mode that removes the primary repository entry. | The command fails with an explicit resolution error. |
+| 3 | Run the test harness mode that removes the target directory for either repository. | The command fails with a clear missing-directory error. |
+
+## Postconditions
+The implementation leaves no partial marker writes behind on failure.
+
+## Notes
+TC-1005.
+
+## Discussion
+
+## Attachments
```

## Untouched
3 test cases were not touched by this run.
