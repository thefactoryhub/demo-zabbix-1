# Requirements and test specifications

This folder is the project's requirement and test database. Every requirement, test case,
test suite and test run is one markdown file; git is the history and the default branch is
the released truth. Read this guide before you create or change a file, then check your work:

```text
python3 .ploqa/specifications/spec_tool.py validate            # every error and warning with file and line
python3 .ploqa/specifications/spec_tool.py next-id REQ         # the next free id (also TC, TS, TR); never invent ids
python3 .ploqa/specifications/spec_tool.py trace REQ-0116      # everything linked to one entity, with its computed state
python3 .ploqa/specifications/spec_tool.py coverage            # requirement coverage, results and implementation states
python3 .ploqa/specifications/spec_tool.py markers             # TC-/REQ- markers found in the code
```

Add `--json` to any command for machine-readable output. The tool is the same parser the
product uses, so a file that validates here is accepted everywhere.

## Layout

```text
specifications/
├── README.md                          # this guide
├── requirements/REQ-NNNN-<slug>.md    # one requirement per file
├── test-cases/TC-NNNN-<slug>.md       # one test case or checklist per file
├── test-suites/TS-NNNN-<slug>.md      # ordered sets of test cases
├── test-runs/TR-NNNN-<slug>.md        # planned and executed runs with results
├── attachments/<ID>/<file>            # files linked from `## Attachments`
└── evidence/<ISSUE-KEY>/<run-id>/     # reports written by the workflow check steps
```

## Rules that always apply

1. **One entity per file**, named `<ID>-<slug>.md` or `<ID>.md`, inside the folder of its kind.
   The `id` key must match the file name. Ids are allocated with `next-id`, never invented,
   never renumbered and never reused, even after a file is removed.
2. **Frontmatter is a strict YAML subset.** Keys are `snake_case` and unique. A value is a
   scalar, an inline list `[a, b, "quoted, text"]`, a block list of `- item` lines, or empty
   (null). Scalars are unquoted text, double-quoted text with `\"` `\\` `\n` `\t` escapes,
   integers, `true`/`false`, or ISO 8601 timestamps such as `2026-10-07T09:12:00Z`. Nested
   mappings, single quotes and multi-line scalars are errors. Unknown keys are kept and
   reported as warnings.
3. **The body starts with a display-only `# <id> <title>` heading** followed by level-2
   sections (`## Statement`, `## Steps`, ...). Sections may come in any order; unknown sections
   are preserved. Nothing but the heading may precede the first section.
4. **Tables are strict.** Headers must match exactly, a `| --- |` row follows the header, every
   row has the same number of cells, `|` inside a cell is written `\|` and a line break inside a
   cell is written `<br>`. Step numbers are consecutive from 1.
5. **Discussion entries** look like `- **author** (2026-10-07T09:12:00Z): text`; continuation
   lines are indented by two spaces. **Attachments** look like `- [label](../attachments/REQ-0116/file.png)`.
6. **Status needs proof.** A requirement may only carry `status: implemented` or
   `status: released` when its computed implementation state is `implemented`
   or `verified` (see *Computed states* below). The product refuses the change otherwise and the
   requirements check step fails with the missing proof.
7. **Evidence reports are written by the workflow steps.** Do not edit `evidence/` by hand.
8. **Timestamps** are ISO 8601 in UTC: `2026-10-07T09:12:00Z`.

## Requirements (`requirements/REQ-NNNN-<slug>.md`)

| Key | Required | Values |
| --- | --- | --- |
| `id` | yes | `REQ-` and at least four digits; must match the file name prefix |
| `title` | yes | text |
| `kind` | yes | `capability`, `sub_capability`, `requirement` |
| `status` | yes | `proposed`, `approved`, `in_development`, `implemented`, `released`, `postponed`, `rejected` |
| `parent` | no | id of an existing requirement (hierarchy of unlimited depth) |
| `type` | no | `functional`, `non_functional`, `constraint`, `interface`, `business`, `quality` |
| `priority` | no | `critical`, `high`, `medium`, `low` |
| `review_status` | no | `new`, `in_review`, `reviewed`, `rework` |
| `reviewer`, `owner`, `sprint`, `source`, `external_id` | no | text |
| `verification_method` | no | `test`, `analysis`, `inspection`, `demonstration` |
| `tags` | no | list |
| `depends_on`, `related` | no | lists of requirement ids |
| `created_by`, `created_at` | no | text / ISO 8601 timestamp (`2026-10-07T09:12:00Z`) |

Body sections: `## Statement` (required for `kind: requirement`), `## Rationale`,
`## User story`, `## Acceptance criteria`, `## Notes`, `## Discussion`, `## Attachments`.

```markdown
---
id: REQ-0116
title: Time synchronisation
kind: requirement
status: approved
parent: REQ-0100
type: functional
priority: high
verification_method: test
tags: [realtime, ntp]
depends_on: [REQ-0114]
---

# REQ-0116 Time synchronisation

## Statement
The system shall synchronise all subsystems with NTP and act as an NTP client.

## Rationale
Operators compare events across subsystems.

## User story

## Acceptance criteria
- Clock drift between subsystems stays below 100 ms.

## Notes

## Discussion
- **ola@example.com** (2026-10-07T09:12:00Z): Reviewed with the customer.

## Attachments
- [Timing diagram](../attachments/REQ-0116/timing.png)
```

Capabilities and sub-capabilities (`kind: capability`, `kind: sub_capability`) group requirements
through `parent` and do not need a statement.

## Test cases (`test-cases/TC-NNNN-<slug>.md`)

| Key | Required | Values |
| --- | --- | --- |
| `id` | yes | `TC-` and at least four digits; must match the file name prefix |
| `title` | yes | text |
| `kind` | yes | `test_case`, `checklist` |
| `status` | yes | `draft`, `ready`, `deprecated` |
| `level` | no | `unit`, `integration`, `system`, `acceptance` |
| `type` | no | `functional`, `regression`, `performance`, `security`, `usability`, `smoke`, `exploratory` |
| `priority` | no | `critical`, `high`, `medium`, `low` |
| `automation` | no | `manual`, `automated`, `semi_automated` (the intent; whether a test exists is measured from markers) |
| `requirements` | no | list of requirement ids the test case verifies |
| `owner`, `external_id` | no | text |
| `estimated_minutes` | no | integer |
| `tags` | no | list |
| `created_by`, `created_at` | no | as for requirements |

Body sections: `## Objective`, `## Preconditions`, `## Test data`, `## Steps`,
`## Postconditions`, `## Notes`, `## Discussion`, `## Attachments`.

```markdown
---
id: TC-0071
title: NTP synchronisation across subsystems
kind: test_case
status: ready
level: system
type: functional
priority: high
automation: automated
requirements: [REQ-0116]
---

# TC-0071 NTP synchronisation across subsystems

## Objective
Verify that every subsystem follows the central clock.

## Preconditions
All subsystems are running and reachable.

## Test data

## Steps
| # | Action | Expected result |
| --- | --- | --- |
| 1 | Open the central system clock page | Time is correct and NTP sync is active |
| 2 | Compare the clock of every subsystem | Drift is below 100 ms |

## Postconditions

## Notes

## Discussion

## Attachments
```

A **checklist** (`kind: checklist`) is a test case whose steps have no expected result; its
table has two columns: `| # | Check |`.

## Test suites (`test-suites/TS-NNNN-<slug>.md`)

Frontmatter: `id`, `title` (required), `test_cases` (ordered list of test case ids), `owner`,
`tags`, `created_by`, `created_at`. Body: `## Description`.

## Test runs (`test-runs/TR-NNNN-<slug>.md`)

| Key | Required | Values |
| --- | --- | --- |
| `id`, `title` | yes |  |
| `type` | yes | `acceptance`, `system`, `integration`, `regression`, `smoke`, `verification` (`verification` runs are written by the test specification check step) |
| `status` | yes | `planned`, `in_progress`, `completed`, `aborted` |
| `sprint`, `environment`, `commit`, `branch`, `baseline`, `issue`, `issue_id` | no | text |
| `owners` | no | list |
| `created_by`, `created_at`, `completed_at` | no |  |

```markdown
# TR-0168 SAT3: Value assurance

## Description

## Executions
| Test case | Suite | Assigned | Result | Executed by | Executed at | Defects | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-0018 | TS-0003 | mia@example.com | ok_with_comment | mia@example.com | 2024-06-10T12:15:12Z | PFT-2114 | Underlying minute values are not marked |

## Execution log
### TC-0018
| Step | Result | Executed by | Executed at | Comment |
| --- | --- | --- | --- | --- |
| 1 | ok | mia@example.com | 2024-06-10T11:21:43Z |  |
| 5 | ok_with_comment | mia@example.com | 2024-06-10T12:13:55Z | Underlying minute values are not marked |
```

Results: `ok`, `ok_with_comment`, `failed`, `blocked`, `in_progress`, `not_run`. A result of `ok`, `ok_with_comment`, `failed`, `blocked` needs an `Executed at`
timestamp. The row in `## Executions` is the test case's result in the run; the `## Execution
log` holds the step results. The latest execution of a test case across all runs (by
`Executed at`) is its current result. Defects are comma-separated issue keys.

## Evidence reports (`evidence/<ISSUE-KEY>/<run-id>/*.md`)

Written by the **Requirements check** and **Test specification check** workflow steps and
committed with the issue. Frontmatter: `kind` (`requirements_check`, `test_spec_check`), `issue`, `issue_id`,
`issue_title`, `run_id`, `step_key`, `created_at`, `base_commit`, `branch`, `agent_log`, `model`,
`requirements_touched` / `test_cases_touched`, `test_run`, `summary`. Body: `## Summary`,
a `## Requirements` (or `## Test cases`) table with ID, title, disposition
(`created`, `updated`, `removed`, `unchanged`), fulfilled (or result) and motivation, `## Changes` with one
`### <ID>` and a fenced `diff` block per created, updated or removed entity, and `## Untouched`
with the count of entities the run did not touch.

## Markers: linking code to test cases and requirements

An automated test is linked to its test case by writing the test case id anywhere in the test
source: in the test name (`test_tc_0071_ntp_sync`), a comment (`# TC-0071`), a docstring, a
decorator or a test title (`test("TC-0071 syncs the clock", ...)`). Code can reference
requirements the same way (`REQ-0116`). Every tracked file outside `specifications/` is scanned for
`TC-NNNN` and `REQ-NNNN` (also written `tc_0071`); the matches are the implementation proof of
a test case and the code references of a requirement. **Every automated test you add or change
must carry the id of the test case it verifies.**

## Computed states and proof

Nothing below is stored; it is derived from the files and the code on every read.

| Entity | State | Rule | Proof shown |
| --- | --- | --- | --- |
| Requirement | `verified` | at least one linked test case and the latest execution of every linked test case is `ok` or `ok_with_comment` | the executions (run, date, executor) |
| Requirement | `failing` | the latest execution of a linked test case is `failed` | the failing executions |
| Requirement | `implemented` | not verified and not failing, and either a committed requirements-check report marks it fulfilled or every linked test case has a test implementation in the code | the report (issue, run, commit) or the markers |
| Requirement | `unverified` | none of the above | the missing piece (no test cases, no executions, no report) |
| Test case | `implemented` | at least one `TC-` marker in the code | file and line of every marker |
| Test case | `missing` | automation is not `manual` and no marker exists | — |
| Test case | `manual` | automation is `manual` and no marker exists | — |

The marker check comes first: a test case declared `manual` that carries a marker is `implemented`.
Deprecated test cases (`status: deprecated`) verify nothing. A requirement's `status` is the
declared lifecycle; the computed state is the measured truth, and `implemented` /
`released` may only be declared when the measured state supports it.

## Working as an agent

- Run `python3 .ploqa/specifications/spec_tool.py validate` after every change to this folder and fix every error.
- Allocate ids with `python3 .ploqa/specifications/spec_tool.py next-id <REQ|TC|TS|TR>`; when you need several, take consecutive
  numbers from the first free one.
- Keep statements testable: one requirement, one `shall`, measurable criteria.
- Link test cases to requirements with `requirements: [REQ-...]` and mark the test code with
  the test case id.
- Leave `evidence/` and status changes to `implemented` / `released` to the
  workflow check steps unless a step asks you to change them.
