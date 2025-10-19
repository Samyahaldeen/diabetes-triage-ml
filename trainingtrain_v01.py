import json, pickle, numpy as np, random, os
from pathlib import Path
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from src.pipeline import make_pipeline_v01

SEED = 42
random.seed(SEED); np.random.seed(SEED)

def main():
    Xy = load_diabetes(as_frame=True)
    X = Xy.frame.drop(columns=["target"])
    y = Xy.frame["target"]

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=SEED)

    pipe = make_pipeline_v01()
    pipe.fit(Xtr, ytr)

    preds = pipe.predict(Xte)
    rmse = float(mean_squared_error(yte, preds, squared=False))

    Path("artifacts").mkdir(exist_ok=True)
    with open("artifacts/model.pkl", "wb") as f:
        pickle.dump(pipe, f)

    Path("artifacts/metrics.json").write_text(json.dumps(
        {"rmse": rmse, "split_random_state": SEED}, indent=2
    ))

    version = os.environ.get("MODEL_VERSION", "v0.1")
    Path("artifacts/version.txt").write_text(version)
    Path("artifacts/metadata.json").write_text(json.dumps({}, indent=2))

    print(f"RMSE: {rmse:.4f}")

if __name__ == "__main__":
    main()
