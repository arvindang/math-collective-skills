#!/usr/bin/env python3
"""Create deterministic per-skill archives and one filesystem bundle."""

from __future__ import annotations

import argparse
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = ROOT / "skills"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def files_under(path: Path) -> list[Path]:
    return sorted(item for item in path.rglob("*") if item.is_file())


def add_file(archive: zipfile.ZipFile, source: Path, target: Path) -> None:
    info = zipfile.ZipInfo(target.as_posix(), FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, source.read_bytes())


def package_skill(skill_dir: Path, output_dir: Path) -> Path:
    output = output_dir / f"{skill_dir.name}.zip"
    with zipfile.ZipFile(output, "w") as archive:
        for source in files_under(skill_dir):
            add_file(archive, source, Path(skill_dir.name) / source.relative_to(skill_dir))
    return output


def package_bundle(skill_dirs: list[Path], output_dir: Path) -> Path:
    output = output_dir / "math-founder-stack-all.zip"
    with zipfile.ZipFile(output, "w") as archive:
        for name in ("LICENSE", "NOTICE.md", "README.md"):
            source = ROOT / name
            if source.is_file():
                add_file(archive, source, Path(name))
        for skill_dir in skill_dirs:
            for source in files_under(skill_dir):
                target = Path("skills") / skill_dir.name / source.relative_to(skill_dir)
                add_file(archive, source, target)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()

    skill_dirs = sorted(
        path for path in SKILLS_ROOT.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )
    if not skill_dirs:
        raise SystemExit("No skills found")
    args.output.mkdir(parents=True, exist_ok=True)
    outputs = [package_skill(skill_dir, args.output) for skill_dir in skill_dirs]
    outputs.append(package_bundle(skill_dirs, args.output))
    for output in outputs:
        print(output.relative_to(ROOT) if output.is_relative_to(ROOT) else output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
