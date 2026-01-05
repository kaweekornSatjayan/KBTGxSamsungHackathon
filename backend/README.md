# Backend (FastAPI)

Run the backend and serve the frontend static page.

Steps (Windows):

1. Create and activate venv

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Run server (from this folder)

```powershell
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000 to access the upload page.

Place your ONNX model at `model.onnx` inside this folder; the app will try to load it on startup. The current code returns placeholder results until you implement preprocessing and inference.
