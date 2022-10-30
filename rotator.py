import gzip, os, shutil, time
from pathlib import Path

def plan_rotations(path: Path, max_bytes: int) -> bool:
    if not path.exists(): return False
    return path.stat().st_size > max_bytes
