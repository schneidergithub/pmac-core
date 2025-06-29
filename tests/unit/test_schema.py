
from pathlib import Path
from pmac.validators import validate
import pytest

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures"

@pytest.mark.parametrize("fixture, should_pass", [("valid/pmac_min.json", True), ("invalid/missing_team.json", False)])
def test_validation(fixture, should_pass):
    ok, _ = validate(FIXTURES / fixture)
    assert ok is should_pass
