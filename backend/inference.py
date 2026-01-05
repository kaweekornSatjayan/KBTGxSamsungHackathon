"""
Inference helper placeholder for ONNX model.

Place your `model.onnx` in the same folder as this file. This module exposes
`load_model()` and `predict_from_video(path)` functions. The real preprocessing
and model input creation should be implemented where marked.
"""
import os
from typing import Dict

try:
    import onnxruntime as ort
    ONNX_AVAILABLE = True
except Exception:
    ONNX_AVAILABLE = False

MODEL_FILENAME = "model.onnx"
_session = None


def load_model(path: str = None):
    global _session
    if not ONNX_AVAILABLE:
        _session = None
        return False
    if path is None:
        path = os.path.join(os.path.dirname(__file__), MODEL_FILENAME)
    if not os.path.exists(path):
        _session = None
        return False
    _session = ort.InferenceSession(path)
    return True


def predict_from_video(video_path: str) -> Dict:
    """
    Placeholder function to predict on a saved video file.

    Implement these steps:
    1. Extract frames (e.g., with OpenCV). Select frames the model expects.
    2. Preprocess frames into model input tensor(s) (resize, normalize, stack, etc.).
    3. Run `_session.run(output_names, {input_name: input_array})`.
    4. Postprocess logits/scores into desired output (e.g., probability/confidence).

    Returns dict with keys: `deepfake` (bool), `confidence` (float), `note` (str).
    """
    if _session is None:
        return {"deepfake": False, "confidence": 0.0, "note": "Model not loaded"}

    # TODO: implement real preprocessing + inference here.
    # Example return format (placeholder):
    return {"deepfake": False, "confidence": 0.0, "note": "Placeholder inference"}
"""
Inference helper placeholder for ONNX model.

Place your `model.onnx` in the same folder as this file. This module exposes
`load_model()` and `predict_from_video(path)` functions. The real preprocessing
and model input creation should be implemented where marked.
"""
import os
from typing import Dict

try:
    import onnxruntime as ort
    ONNX_AVAILABLE = True
except Exception:
    ONNX_AVAILABLE = False

MODEL_FILENAME = "model.onnx"
_session = None


def load_model(path: str = None):
    global _session
    if not ONNX_AVAILABLE:
        _session = None
        return False
    if path is None:
        path = os.path.join(os.path.dirname(__file__), MODEL_FILENAME)
    if not os.path.exists(path):
        _session = None
        return False
    _session = ort.InferenceSession(path)
    return True


def predict_from_video(video_path: str) -> Dict:
    """
    Placeholder function to predict on a saved video file.

    Implement these steps:
    1. Extract frames (e.g., with OpenCV). Select frames the model expects.
    2. Preprocess frames into model input tensor(s) (resize, normalize, stack, etc.).
    3. Run `_session.run(output_names, {input_name: input_array})`.
    4. Postprocess logits/scores into desired output (e.g., probability/confidence).

    Returns dict with keys: `deepfake` (bool), `confidence` (float), `note` (str).
    """
    if _session is None:
        return {"deepfake": False, "confidence": 0.0, "note": "Model not loaded"}

    # TODO: implement real preprocessing + inference here.
    # Example return format (placeholder):
    return {"deepfake": False, "confidence": 0.0, "note": "Placeholder inference"}
