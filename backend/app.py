from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import shutil
import os
import uuid

from . import inference

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.onnx")
# Try to load model on startup if present
inference.load_model(MODEL_PATH)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")


@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    uploads_dir = os.path.join(BASE_DIR, "uploads")
    os.makedirs(uploads_dir, exist_ok=True)
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    dest_path = os.path.join(uploads_dir, filename)
    with open(dest_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # If model not loaded, predict_from_video will return placeholder
    result = inference.predict_from_video(dest_path)
    return JSONResponse(result)
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import shutil
import os
import uuid

from . import inference

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.onnx")
# Try to load model on startup if present
inference.load_model(MODEL_PATH)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

frontend_dir = os.path.join(BASE_DIR, "..", "frontend")
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")


@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    uploads_dir = os.path.join(BASE_DIR, "uploads")
    os.makedirs(uploads_dir, exist_ok=True)
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    dest_path = os.path.join(uploads_dir, filename)
    with open(dest_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # If model not loaded, predict_from_video will return placeholder
    result = inference.predict_from_video(dest_path)
    return JSONResponse(result)
