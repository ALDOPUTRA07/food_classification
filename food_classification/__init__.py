from pathlib import Path

import food_classification

# Project Directories
PACKAGE_ROOT = Path(food_classification.__file__).resolve().parent

with open(PACKAGE_ROOT / "VERSION") as version_file:
    __version__ = version_file.read().strip()
