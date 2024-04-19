from pathlib import Path

import eccodes

vendor = eccodes.codes_definition_path()
defs_path = Path.home() / "eccodes-cosmo-resources/definitions"
eccodes.codes_set_definitions_path(f"{defs_path}:{vendor}")

from grixraz.find import find_files
from grixraz.reference import create_references

__all__ = ["find_files", "create_references"]
