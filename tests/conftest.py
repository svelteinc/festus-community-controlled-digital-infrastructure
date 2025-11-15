import sys
from pathlib import Path

# Ensure the repository root (and thus the `src/` directory) is on sys.path
ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Optionally, also add the `src/` directory directly for tools that expect it.
SRC_DIR = ROOT / "src"
if SRC_DIR.exists() and str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

