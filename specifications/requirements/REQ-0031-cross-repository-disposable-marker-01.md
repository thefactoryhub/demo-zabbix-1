---
id: REQ-0031
title: Cross-repository disposable marker #01
kind: requirement
status: implemented
type: functional
priority: high
verification_method: demonstration
tags: [disposable, multi-repo]
---

# REQ-0031 Cross-repository disposable marker #01

## Statement
The disposable multi-repository harness shall write the exact marker text `Multi repo disposable run default-workflow-e2e-ws-07 issue 01` into `disposable-e2e/default-workflow-e2e-ws-07/primary-01.txt` in the primary repository (`demo-zabbix-1`) and into `disposable-e2e/default-workflow-e2e-ws-07/madeup-01.txt` in the secondary repository (`madeup`), while explicitly avoiding any writes under the declared `madeup/sub` submodule path.

## Rationale
This validates that the harness can perform safe, deterministic cross-repository writes without crossing submodule boundaries.

## User story
As an engineer, I want disposable multi-repository runs to update expected marker files in each repository so that end-to-end orchestration can be validated.

## Acceptance criteria
- After the run, the primary marker file exists and contains the exact marker text.
- After the run, the secondary marker file exists and contains the exact marker text.
- After the run, no file under `madeup/sub` is modified.

## Notes
- The harness must base repository selection on `.ploqa/workspace.json`.

## Discussion
- **assistant** (2026-10-08T00:00:00Z): Verified that the marker files were created with the exact text in the produced workspace tree.
