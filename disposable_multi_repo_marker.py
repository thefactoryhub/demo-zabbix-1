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
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"cannot parse workspace json: {workspace_json}") from exc


def _workspace_root(workspace_json: Path) -> Path:
    if workspace_json.name != "workspace.json":
        raise RuntimeError(f"cannot resolve workspace root from: {workspace_json}")
    return workspace_json.resolve().parent.parent


def _repo_root_by_name(workspace: dict, repo_name: str) -> Path:
    for repo in workspace.get("repositories", []):
        if repo.get("name") == repo_name:
            path = repo.get("path")
            if not path:
                break
            return Path(path)
    raise RuntimeError(f"cannot resolve {repo_name} repo path from workspace.json")


def _repo_root(workspace: dict, workspace_root: Path, repo_name: str) -> Path:
    repo_root = _repo_root_by_name(workspace, repo_name)
    return workspace_root / repo_root


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
    # TC-0001, TC-0002, TC-0003: ws-13 happy path and failure coverage.
    workspace_json = Path(_workspace_json_from_argv(sys.argv[1:]))
    workspace = _load_workspace(workspace_json)
    workspace_root = _workspace_root(workspace_json)

    primary_root = _repo_root(workspace, workspace_root, workspace.get("primary", ""))
    secondary_root = _repo_root(workspace, workspace_root, "madeup")
    marker_text = "Multi repo disposable run default-workflow-e2e-ws-13 issue 01"

    primary_target = _target_path(primary_root, "disposable-e2e/default-workflow-e2e-ws-13/primary-01.txt")
    secondary_target = _target_path(secondary_root, "disposable-e2e/default-workflow-e2e-ws-13/madeup-01.txt")

    submodule_root = secondary_root / "sub"
    if not submodule_root.exists():
        raise RuntimeError("missing madeup/sub submodule guard")

    _write_marker(primary_target, marker_text)
    _write_marker(secondary_target, marker_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
