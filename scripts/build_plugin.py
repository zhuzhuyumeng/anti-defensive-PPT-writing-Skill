#!/usr/bin/env python3
"""Build a public plugin ZIP, including each skill's referenced resources."""

import argparse
import json
from pathlib import Path
from tempfile import NamedTemporaryFile
import zipfile


def build(output=None):
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    output = Path(output) if output else root / "dist" / f"{manifest['name']}-{version}.zip"
    output = output.resolve()
    files = [root / name for name in (
        "plugin.json", ".codex-plugin/plugin.json", ".agents/plugins/marketplace.json",
        "LICENSE", "PRIVACY.md", "README.md", "README_EN.md", "scripts/build_plugin.py",
    )]
    for directory in ("skills", "assets", "prompts"):
        files.extend(path for path in (root / directory).rglob("*")
                     if path.is_file() and not path.name.startswith(".")
                     and "__pycache__" not in path.parts and path.suffix not in {".pyc", ".zip"})
    files = sorted(set(files))
    for path in files:
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Expected a regular distribution file: {path}")
    if output in files:
        raise ValueError("Output must not overwrite a distribution source file")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with NamedTemporaryFile(dir=output.parent, suffix=".zip", delete=False) as handle:
            temporary = Path(handle.name)
        with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in files:
                archive.write(path, path.relative_to(root).as_posix())
        with zipfile.ZipFile(temporary) as archive:
            corrupt = archive.testzip()
            if corrupt:
                raise ValueError(f"Corrupt archive member: {corrupt}")
        temporary.replace(output)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    print(build(args.output))
