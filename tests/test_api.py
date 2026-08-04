
"""
Tests for FastAPI endpoints.
"""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_home_page():

    """
    Test that home page loads successfully.
    """

    response = client.get("/")


    assert response.status_code == 200

    assert "EV Range Prediction" in response.text



def test_prediction_endpoint():

    """
    Test prediction form submission.
    """

    response = client.post(
        "/predict",
        data={
            "battery_capacity_kWh": 75,
            "efficiency_wh_per_km": 170,
            "torque_nm": 500,
            "acceleration_0_100_s": 5,
            "top_speed_kmh": 250
        }
    )


    assert response.status_code == 200


    assert "Predicted Range" in response.text