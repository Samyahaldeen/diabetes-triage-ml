from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.schemas import PredictRequest, PredictResponse, validate_feature_keys
from app.settings import settings
from app.model_io import load_model, load_version, load_metadata
import numpy as np

app = FastAPI(title=settings.app_name)

MODEL = None
VERSION = "unknown"
META = {}

@app.on_event("startup")
def _load():
    global MODEL, VERSION, META
    MODEL = load_model(settings.model_path)
    VERSION = load_version(settings.model_version_path)
    META = load_metadata("artifacts/metadata.json")

@app.get("/health")
def health():
    return {"status": "ok", "model_version": VERSION}

@app.exception_handler(Exception)
async def handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc), "hint": "Check payload keys and types."}
    )

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    missing, extra = validate_feature_keys(req.dict())
    if missing or extra:
        raise HTTPException(status_code=422, detail={"missing": missing, "extra": extra})
    x = np.array([[req.age, req.sex, req.bmi, req.bp, req.s1, req.s2, req.s3, req.s4, req.s5, req.s6]])
    yhat = float(MODEL.predict(x)[0])
    risk_flag = None
    risk_threshold = None
    if "risk_threshold" in META:
        risk_threshold = META["risk_threshold"]
        risk_flag = bool(yhat >= risk_threshold)
    return PredictResponse(
        prediction=yhat,
        model_version=VERSION,
        risk_flag=risk_flag,
        risk_threshold=risk_threshold
    )
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.schemas import PredictRequest, PredictResponse, validate_feature_keys
from app.settings import settings
from app.model_io import load_model, load_version, load_metadata
import numpy as np

app = FastAPI(title=settings.app_name)

MODEL = None
VERSION = "unknown"
META = {}

@app.on_event("startup")
def _load():
    global MODEL, VERSION, META
    MODEL = load_model(settings.model_path)
    VERSION = load_version(settings.model_version_path)
    META = load_metadata("artifacts/metadata.json")

@app.get("/health")
def health():
    return {"status": "ok", "model_version": VERSION}

@app.exception_handler(Exception)
async def handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc), "hint": "Check payload keys and types."}
    )

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    missing, extra = validate_feature_keys(req.dict())
    if missing or extra:
        raise HTTPException(status_code=422, detail={"missing": missing, "extra": extra})
    x = np.array([[req.age, req.sex, req.bmi, req.bp, req.s1, req.s2, req.s3, req.s4, req.s5, req.s6]])
    yhat = float(MODEL.predict(x)[0])
    risk_flag = None
    risk_threshold = None
    if "risk_threshold" in META:
        risk_threshold = META["risk_threshold"]
        risk_flag = bool(yhat >= risk_threshold)
    return PredictResponse(
        prediction=yhat,
        model_version=VERSION,
        risk_flag=risk_flag,
        risk_threshold=risk_threshold
    )
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.schemas import PredictRequest, PredictResponse, validate_feature_keys
from app.settings import settings
from app.model_io import load_model, load_version, load_metadata
import numpy as np

app = FastAPI(title=settings.app_name)

MODEL = None
VERSION = "unknown"
META = {}

@app.on_event("startup")
def _load():
    global MODEL, VERSION, META
    MODEL = load_model(settings.model_path)
    VERSION = load_version(settings.model_version_path)
    META = load_metadata("artifacts/metadata.json")

@app.get("/health")
def health():
    return {"status": "ok", "model_version": VERSION}

@app.exception_handler(Exception)
async def handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc), "hint": "Check payload keys and types."}
    )

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    missing, extra = validate_feature_keys(req.dict())
    if missing or extra:
        raise HTTPException(status_code=422, detail={"missing": missing, "extra": extra})
    x = np.array([[req.age, req.sex, req.bmi, req.bp, req.s1, req.s2, req.s3, req.s4, req.s5, req.s6]])
    yhat = float(MODEL.predict(x)[0])
    risk_flag = None
    risk_threshold = None
    if "risk_threshold" in META:
        risk_threshold = META["risk_threshold"]
        risk_flag = bool(yhat >= risk_threshold)
    return PredictResponse(
        prediction=yhat,
        model_version=VERSION,
        risk_flag=risk_flag,
        risk_threshold=risk_threshold
    )
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.schemas import PredictRequest, PredictResponse, validate_feature_keys
from app.settings import settings
from app.model_io import load_model, load_version, load_metadata
import numpy as np

app = FastAPI(title=settings.app_name)

MODEL = None
VERSION = "unknown"
META = {}

@app.on_event("startup")
def _load():
    global MODEL, VERSION, META
    MODEL = load_model(settings.model_path)
    VERSION = load_version(settings.model_version_path)
    META = load_metadata("artifacts/metadata.json")

@app.get("/health")
def health():
    return {"status": "ok", "model_version": VERSION}

@app.exception_handler(Exception)
async def handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc), "hint": "Check payload keys and types."}
    )

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    missing, extra = validate_feature_keys(req.dict())
    if missing or extra:
        raise HTTPException(status_code=422, detail={"missing": missing, "extra": extra})
    x = np.array([[req.age, req.sex, req.bmi, req.bp, req.s1, req.s2, req.s3, req.s4, req.s5, req.s6]])
    yhat = float(MODEL.predict(x)[0])
    risk_flag = None
    risk_threshold = None
    if "risk_threshold" in META:
        risk_threshold = META["risk_threshold"]
        risk_flag = bool(yhat >= risk_threshold)
    return PredictResponse(
        prediction=yhat,
        model_version=VERSION,
        risk_flag=risk_flag,
        risk_threshold=risk_threshold
    )
