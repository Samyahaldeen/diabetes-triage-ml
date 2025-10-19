from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert "status" in r.json()

def test_predict_schema_error():
    r = client.post("/predict", json={"age": 0.1})
    assert r.status_code in (400, 422)

def test_predict_happy_path(monkeypatch):
    from app import main as m
    class FakeModel:
        def predict(self, X): return [123.45]
    m.MODEL = FakeModel()
    m.VERSION = "test"
    payload = {"age":0.02,"sex":-0.044,"bmi":0.06,"bp":-0.03,"s1":-0.02,"s2":0.03,"s3":-0.02,"s4":0.02,"s5":0.02,"s6":-0.001}
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    assert "prediction" in r.json()
