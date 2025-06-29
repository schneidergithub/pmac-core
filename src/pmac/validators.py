
from __future__ import annotations
import json
from importlib import resources
from pathlib import Path
from typing import Tuple, List
import jsonschema

SCHEMA_RESOURCE = resources.files("pmac.schema").joinpath("v0_1.json")
_SCHEMA = json.loads(SCHEMA_RESOURCE.read_text("utf-8"))
_VALIDATOR = jsonschema.Draft202012Validator(_SCHEMA)

def validate(file_path: str | Path) -> Tuple[bool, List[str]]:
    path = Path(file_path).expanduser().resolve()
    if not path.is_file():
        return False, [f"File not found: {path}"]
    try:
        instance = json.loads(path.read_text("utf-8"))
    except json.JSONDecodeError as exc:
        return False, [f"JSON decode error: {exc.msg} (line {exc.lineno}, col {exc.colno})"]
    errors = sorted(_VALIDATOR.iter_errors(instance), key=lambda e: e.path)
    if errors:
        return False, [f"{'.'.join(map(str, e.path)) or '<root>'}: {e.message}" for e in errors]
    return True, []
