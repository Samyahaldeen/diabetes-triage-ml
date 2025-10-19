\# Virtual Diabetes Clinic Triage — ML Service

Predicts short-term disease progression from sklearn diabetes data. Higher prediction ≈ higher risk. Ships as a Dockerized FastAPI service.



\## Local quickstart

```bash

python -m venv .venv \&\& .\\.venv\\Scripts\\activate   # (Windows) use 'source .venv/bin/activate' on macOS/Linux

pip install -r requirements.txt

set MODEL\_VERSION=v0.1 \&\& python training\\train\_v01.py   # PowerShell: $env:MODEL\_VERSION="v0.1"; python training\\train\_v01.py

uvicorn app.main:app --host 0.0.0.0 --port 8000



