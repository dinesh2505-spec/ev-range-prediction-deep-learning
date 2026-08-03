
"""
predictor.py

Contains the prediction pipeline for EV range prediction.
"""


import pandas as pd
import numpy as np

from src.model_loader import (
    load_trained_model,
    load_scaler
)


# Load model and scaler once
model = load_trained_model()
scaler = load_scaler()



def predict_range(
    battery_capacity_kWh,
    efficiency_wh_per_km,
    torque_nm,
    acceleration_0_100_s,
    top_speed_kmh
):
    """
    Predict EV driving range.

    Parameters
    ----------
    battery_capacity_kWh : float
    efficiency_wh_per_km : float
    torque_nm : float
    acceleration_0_100_s : float
    top_speed_kmh : float

    Returns
    -------
    float
        Predicted range in km
    """


    # Create input dataframe
    input_data = pd.DataFrame(
        [[
            battery_capacity_kWh,
            efficiency_wh_per_km,
            torque_nm,
            acceleration_0_100_s,
            top_speed_kmh
        ]],
        columns=[
            "battery_capacity_kWh",
            "efficiency_wh_per_km",
            "torque_nm",
            "acceleration_0_100_s",
            "top_speed_kmh"
        ]
    )


    # Apply same scaling used during training
    input_scaled = scaler.transform(
        input_data
    )


    # Make prediction
    prediction = model.predict(
        input_scaled
    )


    # Convert numpy array to float
    predicted_range = float(
        prediction[0][0]
    )


    return predicted_range