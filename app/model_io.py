import json
import pickle
from pathlib import Path

def load_model(model_path: str):
    with open(model_path, "rb") as f:
        return pickle.load(f)

def load_version(version_path: str) -> str:
    p = Path(version_path)
    return p.read_text().strip() if p.exists() else "unknown"

def load_metadata(meta_path: str) -> dict:
    p = Path(meta_path)
    if p.exists():
        return json.loads(p.read_text())
    return {}
