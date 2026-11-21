from pathlib import Path
import sys, tomllib
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools/course_checks"))
from common import validate_reference

meta = ROOT / "exercises/practice/variable-length-quantity/.meta/tests.toml"
data = tomllib.loads(meta.read_text())
assert len(data) == 31, f"expected 31 canonical entries, got {len(data)}"
assert all(not item.get("include") is False for item in data.values()), "unexpected exclusion"
ids = ["35c9db2e-f781-4c52-b73b-8e76427defd0", "be44d299-a151-4604-a10e-d4b867f41540", "890bc344-cb80-45af-b316-6806a6971e81"]
for key in ids:
    assert data[key].get("comment"), f"missing rationale for {key}"
out, count = validate_reference(ROOT, "variable-length-quantity")
report = f"Canonical entries: 31; exclusions: 0; executed Bats cases: {count}\n\n{out}"
(ROOT / "work/R06-T001/results.txt").write_text(report)
print(f"PASS: 31 TOML entries; 0 exclusions; {count} reference tests executed")
