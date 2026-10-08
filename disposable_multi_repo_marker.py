from __future__ import annotations

import os
import runpy
import sys

# Re-export the implementation from `.ploqa/`.
from pathlib import Path


def _workspace_json_from_argv(argv: list[str]) -> str:
    for i, v in enumerate(argv):
        if v == "--workspace-json" and i + 1 < len(argv):
            return argv[i + 1]
    return os.environ.get("PLOQA_WORKSPACE_JSON", ".ploqa/workspace.json")


def main() -> int:
    # TC-1000: marker writes happen for primary + secondary.
    # TC-1001: madeup/sub is excluded from any writes/traversal.
    # TC-1002: explicit failure path errors when secondary cannot be resolved.
    #
    # These markers must live under `demo-zabbix-1/` because `spec_tool` skips `.ploqa/`.
    root = Path(__file__).resolve().parent.parent
    impl = root / ".ploqa" / "disposable_multi_repo_marker.py"
    if not impl.exists():
        raise RuntimeError(f"missing implementation: {impl}")

    # Execute implementation in-process and propagate its exit status.
    # The implementation raises DisposableTaskError (subclass of RuntimeError)
    # and also uses SystemExit for the `__main__` entrypoint.
    workspace_json = _workspace_json_from_argv(sys.argv[1:])
    sys.argv = [str(impl), "--workspace-json", workspace_json]
    sys.path.insert(0, str(Path(impl).parent.parent))
    try:
        runpy.run_path(str(impl), run_name="__main__")
    except SystemExit as e:
        if isinstance(e.code, int):
            return e.code
        return 0 if e.code is None else 1
    except Exception as e:
        raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
