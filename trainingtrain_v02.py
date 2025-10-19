import json, pickle, numpy as np, random, os
from pathlib import Path
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, precision_score, recall_score
from src.pipeline import make_pipeline_v02_ridge

SEED = 42
random.seed(SEED); np.random.seed(SEED)

def main():
    Xy = load_diabetes(as_frame=True)
    X = Xy.frame.drop(columns=["target"])
    y = Xy.frame["target"]

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=SEED)

    # Improved pipeline: Ridge tends to reduce RMSE vs plain LR
    pipe = make_pipeline_v02_ridge(alpha=3.0)
    pipe.fit(Xtr, ytr)

    preds_te = pipe.predict(Xte)
    rmse = float(mean_squared_error(yte, preds_te, squared=False))

    # Define a high-risk threshold: 75th percentile of y_train
    thr = float(np.percentile(ytr, 75))
    risk_pred = preds_te >= thr
    true_high = yte >= thr

    precision = float(precision_score(true_high, risk_pred))
    recall = float(recall_score(true_high, risk_pred))

    Path("artifacts").mkdir(exist_ok=True)
    with open("artifacts/model.pkl", "wb") as f:
        pickle.dump(pipe, f)

    Path("artifacts/metrics.json").write_text(json.dumps({
        "rmse": rmse,
        "risk_threshold": thr,
        "precision_at_thr": precision,
        "recall_at_thr": recall,
        "split_random_state": SEED
    }, indent=2))

    version = os.environ.get("MODEL_VERSION", "v0.2")
    Path("artifacts/version.txt").write_text(version)
    Path("artifacts/metadata.json").write_text(json.dumps({"risk_threshold": thr}, indent=2))

    print(f"RMSE: {rmse:.4f}  Precision@thr: {precision:.3f}  Recall@thr: {recall:.3f}")

if __name__ == "__main__":
    main()
