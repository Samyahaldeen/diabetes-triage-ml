FROM python:3.11-slim AS builder
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN test -f artifacts/model.pkl || echo "WARNING: artifacts missing; dev build only"

FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY app app
COPY artifacts artifacts
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD python - <<'PY' || exit 1
import json, urllib.request
try:
    with urllib.request.urlopen("http://localhost:8000/health", timeout=2) as r:
        body = json.loads(r.read().decode())
        assert r.status == 200 and body.get("status") == "ok"
except Exception:
    raise SystemExit(1)
PY

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
