#!/usr/bin/env python3
"""Structural checks for the Grove Street MLO source scaffold."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "fxmanifest.lua", "config.lua", "BUILD_CHECKLIST.md",
    "blender/generate_dual_shop_blockout.py", "stream/README.txt", "data/README.txt",
]

def main() -> int:
    failures = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            failures.append(f"Missing required file: {rel}")
    cfg = ROOT / "config.lua"
    if cfg.exists():
        content = cfg.read_text(encoding="utf-8")
        for token in ("Config.ClothingShop", "Config.JewelryShop", "GROVE THREADS", "GROVE GOLD"):
            if token not in content:
                failures.append(f"config.lua missing expected setting: {token}")
    script = ROOT / "blender/generate_dual_shop_blockout.py"
    if script.exists():
        source = script.read_text(encoding="utf-8")
        for token in ("GROVE THREADS", "GROVE GOLD", "Fitting_", "DisplayCase_", "SecureOfficeDesk"):
            if token not in source:
                failures.append(f"Blender generator missing expected feature: {token}")
        try:
            compile(source, str(script), "exec")
        except SyntaxError as exc:
            failures.append(f"Blender generator Python syntax error: {exc}")
    manifest = ROOT / "fxmanifest.lua"
    if manifest.exists():
        source = manifest.read_text(encoding="utf-8")
        if "fx_version 'cerulean'" not in source or "game 'gta5'" not in source:
            failures.append("fxmanifest.lua needs fx_version and game declarations")
    if failures:
        print("VALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("VALIDATION PASSED: source scaffold and basic checks look good.")
    print("This does not compile or validate a FiveM MLO in-game.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
