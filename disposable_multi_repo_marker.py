from __future__ import annotations

import json
import os
import sys
from pathlib import Path


def _workspace_json_from_argv(argv: list[str]) -> str:
    for index, value in enumerate(argv):
        if value == "--workspace-json" and index + 1 < len(argv):
            return argv[index + 1]
    return os.environ.get("PLOQA_WORKSPACE_JSON", ".ploqa/workspace.json")


def _load_workspace(workspace_json: Path) -> dict:
    try:
        return json.loads(workspace_json.read_text())
    except FileNotFoundError as exc:
        raise RuntimeError(f"cannot read workspace json: {workspace_json}") from exc


def _repo_root_by_name(workspace: dict, repo_name: str) -> Path:
    for repo in workspace.get("repositories", []):
        if repo.get("name") == repo_name:
            path = repo.get("path")
            if not path:
                break
            return Path(path)
    raise RuntimeError(f"cannot resolve {repo_name} repo path from workspace.json")


def _target_path(repo_root: Path, relative_path: str) -> Path:
    if not relative_path:
        raise RuntimeError("invalid target path: empty")
    if relative_path.startswith("/"):
        raise RuntimeError("invalid target path: absolute paths not allowed")
    if ".." in relative_path.split("/"):
        raise RuntimeError("invalid target path: must not contain ..")
    target_path = repo_root / relative_path
    if not target_path.parent.is_dir():
        raise RuntimeError(f"target directory missing: {target_path.parent}")
    return target_path


def _write_marker(target_path: Path, text: str) -> None:
    target_path.write_text(text + "\n")


def main() -> int:
    # TC-1000: ws-08 happy path.
    # TC-1001: ws-09 happy path and madeup/sub preservation.
    # TC-1002: ws-09 explicit resolution and target-dir failures.
    workspace_json = Path(_workspace_json_from_argv(sys.argv[1:]))
    workspace = _load_workspace(workspace_json)
    workspace_root = workspace_json.resolve().parent.parent

    primary_repo = _repo_root_by_name(workspace, workspace.get("primary", ""))
    secondary_repo = _repo_root_by_name(workspace, "madeup")

    primary_root = workspace_root / primary_repo
    secondary_root = workspace_root / secondary_repo
    marker_text = "Multi repo disposable run default-workflow-e2e-ws-09 issue 01"

    primary_target = _target_path(primary_root, "disposable-e2e/default-workflow-e2e-ws-09/primary-01.txt")
    secondary_target = _target_path(secondary_root, "disposable-e2e/default-workflow-e2e-ws-09/madeup-01.txt")

    submodule_root = secondary_root / "sub"
    if not submodule_root.exists():
        raise RuntimeError("missing madeup/sub submodule guard")

    _write_marker(primary_target, marker_text)
    _write_marker(secondary_target, marker_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
