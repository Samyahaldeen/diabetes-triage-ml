from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor

def make_pipeline_v01():
    return Pipeline([
        ("scale", StandardScaler()),
        ("lr", LinearRegression())
    ])

def make_pipeline_v02_ridge(alpha: float = 1.0):
    return Pipeline([
        ("scale", StandardScaler()),
        ("ridge", Ridge(alpha=alpha, random_state=42))
    ])

def make_pipeline_v02_rf(n_estimators=300, max_depth=None, random_state=42):
    return Pipeline([
        ("rf", RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            n_jobs=-1,
            random_state=random_state
        ))
    ])
