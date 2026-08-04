
"""
Tests for predictor.py

Checks:
- Prediction runs successfully
- Output type is correct
- Prediction value is realistic
- Different inputs produce different predictions
"""


from src.predictor import predict_range



def test_prediction_returns_value():
    """
    Test that prediction function returns a value.
    """

    prediction = predict_range(
        battery_capacity_kWh=75,
        efficiency_wh_per_km=170,
        torque_nm=500,
        acceleration_0_100_s=5,
        top_speed_kmh=250
    )


    assert prediction is not None



def test_prediction_returns_float():
    """
    Test prediction output type.
    """

    prediction = predict_range(
        battery_capacity_kWh=75,
        efficiency_wh_per_km=170,
        torque_nm=500,
        acceleration_0_100_s=5,
        top_speed_kmh=250
    )


    assert isinstance(
        prediction,
        float
    )



def test_prediction_is_realistic():
    """
    Test predicted range is within realistic EV limits.
    """

    prediction = predict_range(
        battery_capacity_kWh=75,
        efficiency_wh_per_km=170,
        torque_nm=500,
        acceleration_0_100_s=5,
        top_speed_kmh=250
    )


    assert prediction > 0

    assert prediction < 1500



def test_different_vehicle_inputs_change_prediction():
    """
    Test that different vehicles produce different predictions.
    """


    small_ev_prediction = predict_range(
        battery_capacity_kWh=40,
        efficiency_wh_per_km=220,
        torque_nm=300,
        acceleration_0_100_s=8,
        top_speed_kmh=160
    )


    large_ev_prediction = predict_range(
        battery_capacity_kWh=120,
        efficiency_wh_per_km=160,
        torque_nm=900,
        acceleration_0_100_s=3.5,
        top_speed_kmh=300
    )


    assert small_ev_prediction != large_ev_prediction