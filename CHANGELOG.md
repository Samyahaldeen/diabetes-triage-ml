Changelog

v0.2
- Switched to Ridge(alpha=3.0) for improved RMSE vs v0.1.
- Added calibrated high-risk flag (>= 75th percentile of y_train).
- API now returns risk_flag and risk_threshold.

v0.1
- Baseline StandardScaler + LinearRegression.
- FastAPI service with /health and /predict.
- Deterministic split and seeds; metrics logged to artifacts/metrics.json.
