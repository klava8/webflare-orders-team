import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from orders import total
assert total(100, 3) == 300
assert total(100, 0) == 0
try:
    total(-1, 2)
except ValueError:
    pass
else:
    raise AssertionError("Negative price accepted")
print("PASS:3 order checks")
