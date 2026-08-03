

"""
model_loader.py

Loads the trained ANN model and scaler.
"""

from tensorflow.keras.models import load_model
import joblib
import os


# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Models directory
MODELS_DIR = os.path.join(BASE_DIR, "Models")


# File paths
MODEL_PATH = os.path.join(
    MODELS_DIR,
    "final_ev_range_ann_model.keras"
)

SCALER_PATH = os.path.join(
    MODELS_DIR,
    "scaler.pkl"
)


def load_trained_model():
    """
    Load the trained ANN model.

    Returns
    -------
    keras.Model
        Loaded TensorFlow model.
    """

    model = load_model(MODEL_PATH)

    return model


def load_scaler():
    """
    Load the saved StandardScaler.

    Returns
    -------
    sklearn.preprocessing.StandardScaler
    """

    scaler = joblib.load(SCALER_PATH)

    return scaler