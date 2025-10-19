import json, subprocess, sys, pathlib

def run(cmd):
    p = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return p.stdout

def test_train_v01_smoke(monkeypatch):
    monkeypatch.setenv("MODEL_VERSION", "v0.1")
    out = run([sys.executable, "training/train_v01.py"])
    assert "RMSE:" in out
    m = json.loads(pathlib.Path("artifacts/metrics.json").read_text())
    assert "rmse" in m

def test_train_v02_smoke(monkeypatch):
    monkeypatch.setenv("MODEL_VERSION", "v0.2")
    out = run([sys.executable, "training/train_v02.py"])
    assert "RMSE:" in out
    m = json.loads(pathlib.Path("artifacts/metrics.json").read_text())
    assert "precision_at_thr" in m and "recall_at_thr" in m
