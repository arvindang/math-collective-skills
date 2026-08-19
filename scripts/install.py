#!/usr/bin/env python3
"""Install the skill collection for Claude Code and/or OpenAI Codex."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import sys


ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = ROOT / "skills"


def available_skills() -> dict[str, Path]:
    if not SKILLS_ROOT.exists():
        return {}
    return {
        path.name: path
        for path in sorted(SKILLS_ROOT.iterdir())
        if path.is_dir() and (path / "SKILL.md").is_file()
    }


def target_root(host: str, scope: str, project: Path) -> Path:
    if scope == "project":
        return project / (".claude/skills" if host == "claude" else ".agents/skills")
    if host == "claude":
        return Path.home() / ".claude/skills"
    codex_home = os.environ.get("CODEX_HOME")
    return Path(codex_home).expanduser() / "skills" if codex_home else Path.home() / ".agents/skills"


def same_link(target: Path, source: Path) -> bool:
    if not target.is_symlink():
        return False
    return (target.parent / os.readlink(target)).resolve() == source.resolve()


def remove_target(target: Path, root: Path) -> None:
    if target.parent.resolve() != root.resolve():
        raise RuntimeError(f"refusing to replace target outside install root: {target}")
    if target.is_symlink() or target.is_file():
        target.unlink()
    elif target.is_dir():
        shutil.rmtree(target)


def install_one(source: Path, target: Path, root: Path, mode: str, force: bool) -> str:
    if target.exists() or target.is_symlink():
        if same_link(target, source):
            return "current"
        if not force:
            return "exists (use --force to replace this exact skill target)"
        remove_target(target, root)

    root.mkdir(parents=True, exist_ok=True)
    if mode == "link":
        target.symlink_to(source, target_is_directory=True)
    else:
        shutil.copytree(source, target)
    return "installed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=("claude", "codex", "all"), default="all")
    parser.add_argument("--scope", choices=("user", "project"), default="user")
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--mode", choices=("auto", "link", "copy"), default="auto")
    parser.add_argument("--skill", action="append", dest="selected", metavar="NAME")
    parser.add_argument("--force", action="store_true", help="replace only colliding named skill targets")
    parser.add_argument("--list", action="store_true", help="list bundled skills without installing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skills = available_skills()
    if args.list:
        print("\n".join(skills))
        return 0
    if not skills:
        print("No skills found. The package may be incomplete.", file=sys.stderr)
        return 1

    selected = args.selected or list(skills)
    unknown = sorted(set(selected) - set(skills))
    if unknown:
        print(f"Unknown skill(s): {', '.join(unknown)}", file=sys.stderr)
        return 2

    hosts = ("claude", "codex") if args.host == "all" else (args.host,)
    mode = args.mode
    if mode == "auto":
        mode = "copy" if os.name == "nt" else "link"

    project = args.project.expanduser().resolve()
    had_conflict = False
    for host in hosts:
        root = target_root(host, args.scope, project)
        print(f"{host}: {root} ({mode})")
        for name in selected:
            result = install_one(skills[name], root / name, root, mode, args.force)
            print(f"  {name}: {result}")
            had_conflict = had_conflict or result.startswith("exists")
    return 3 if had_conflict else 0


if __name__ == "__main__":
    raise SystemExit(main())
