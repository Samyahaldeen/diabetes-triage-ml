from pydantic import BaseModel, Field
from typing import Dict

FEATURES = ["age","sex","bmi","bp","s1","s2","s3","s4","s5","s6"]

class PredictRequest(BaseModel):
    age: float = Field(...)
    sex: float = Field(...)
    bmi: float = Field(...)
    bp: float = Field(...)
    s1: float = Field(...)
    s2: float = Field(...)
    s3: float = Field(...)
    s4: float = Field(...)
    s5: float = Field(...)
    s6: float = Field(...)

class PredictResponse(BaseModel):
    prediction: float
    model_version: str
    risk_flag: bool | None = None
    risk_threshold: float | None = None

def validate_feature_keys(payload: Dict):
    missing = [f for f in FEATURES if f not in payload]
    extra = [k for k in payload.keys() if k not in FEATURES]
    return missing, extra
