from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        workflow = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"{path.relative_to(ROOT)}: invalid JSON: {error}"]

    nodes = workflow.get("nodes")
    connections = workflow.get("connections")
    if not isinstance(workflow.get("name"), str) or not workflow["name"].strip():
        errors.append(f"{path.relative_to(ROOT)}: missing workflow name")
    if not isinstance(nodes, list) or not nodes:
        errors.append(f"{path.relative_to(ROOT)}: nodes must be a non-empty list")
        return errors
    if not isinstance(connections, dict):
        errors.append(f"{path.relative_to(ROOT)}: connections must be an object")
        return errors

    names: set[str] = set()
    for node in nodes:
        if not isinstance(node, dict):
            errors.append(f"{path.relative_to(ROOT)}: node is not an object")
            continue
        for key in ("name", "type", "typeVersion", "position", "parameters"):
            if key not in node:
                errors.append(f"{path.relative_to(ROOT)}: node missing {key}")
        name = node.get("name")
        if isinstance(name, str):
            if name in names:
                errors.append(f"{path.relative_to(ROOT)}: duplicate node name {name!r}")
            names.add(name)

    for source, outputs in connections.items():
        if source not in names:
            errors.append(f"{path.relative_to(ROOT)}: unknown connection source {source!r}")
        if not isinstance(outputs, dict):
            errors.append(f"{path.relative_to(ROOT)}: connection outputs for {source!r} are invalid")
            continue
        for branches in outputs.values():
            if not isinstance(branches, list):
                continue
            for branch in branches:
                if not isinstance(branch, list):
                    continue
                for edge in branch:
                    target = edge.get("node") if isinstance(edge, dict) else None
                    if target not in names:
                        errors.append(f"{path.relative_to(ROOT)}: unknown connection target {target!r}")
    return errors


def main() -> int:
    files = sorted(ROOT.glob("labs/**/*.workflow.json"))
    if not files:
        print("N8N WORKFLOW VALIDATION: FAIL - no workflow fixtures found")
        return 1
    errors = [error for path in files for error in validate(path)]
    if errors:
        print("N8N WORKFLOW VALIDATION: FAIL")
        for error in errors:
            print(" -", error)
        return 1
    print(f"N8N WORKFLOW VALIDATION: PASS ({len(files)} workflow fixture(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
