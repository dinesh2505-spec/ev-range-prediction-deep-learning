
"""
Tests for model_loader.py

Checks:
- ANN model loading
- Scaler loading
"""

from tensorflow.keras.models import Model
from sklearn.preprocessing import StandardScaler

from src.model_loader import (
    load_trained_model,
    load_scaler
)


def test_load_trained_model():
    """
    Test that ANN model loads correctly.
    """

    model = load_trained_model()

    # Check model exists
    assert model is not None

    # Check it is a Keras model
    assert isinstance(model, Model)



def test_model_input_shape():
    """
    Test that model expects 5 input features.
    """

    model = load_trained_model()

    input_shape = model.input_shape

    # Expected:
    # (None, 5)
    assert input_shape[1] == 5



def test_load_scaler():
    """
    Test that scaler loads correctly.
    """

    scaler = load_scaler()

    # Check scaler exists
    assert scaler is not None

    # Check it is StandardScaler
    assert isinstance(
        scaler,
        StandardScaler
    )



def test_scaler_feature_count():
    """
    Test scaler was trained on 5 features.
    """

    scaler = load_scaler()

    assert scaler.n_features_in_ == 5