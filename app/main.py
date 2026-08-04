# Import Libraries
from fastapi import FastAPI

from app.schemas import EVInput

from src.predictor import predict_range

# Create FastAPI instance
app = FastAPI(
    title="EV Range Prediction API",
    description="Predict EV driving range using ANN",
    version="1.0"
)

# Create the home end point
@app.get("/")
def home():
    return {
        "message": "EV Range Prediction API is running"
    }

@app.post("/predict")
def predict(ev: EVInput):
    """
    Predict EV driving range.

    Parameters
    ----------
    ev : EVInput
        Input data for prediction.

    Returns
    -------
    dict
        Predicted range in km.
    """

    # Extract input values from the Pydantic model
    battery_capacity_kWh = ev.battery_capacity_kWh
    efficiency_wh_per_km = ev.efficiency_wh_per_km
    torque_nm = ev.torque_nm
    acceleration_0_100_s = ev.acceleration_0_100_s
    top_speed_kmh = ev.top_speed_kmh

    # Call the prediction function
    predicted_range = predict_range(
        battery_capacity_kWh,
        efficiency_wh_per_km,
        torque_nm,
        acceleration_0_100_s,
        top_speed_kmh
    )

    return {
    "predicted_range_km": round(float(predicted_range), 2)
}

