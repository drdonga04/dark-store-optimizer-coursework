import sys
from pathlib import Path

# Automatically ensure 'src' is importable when running test discovery
src_dir = str(Path(__file__).resolve().parents[1] / "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
