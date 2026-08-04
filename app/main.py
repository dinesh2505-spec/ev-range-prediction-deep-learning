# Import Libraries
from fastapi import FastAPI, Form

from app.schemas import EVInput

from src.predictor import predict_range

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Create FastAPI instance
app = FastAPI(
    title="EV Range Prediction API",
    description="Predict EV driving range using ANN",
    version="1.0"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


templates = Jinja2Templates(directory="templates")

# Create the home end point
@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/predict", response_class=HTMLResponse)
def predict(

    request: Request,

    battery_capacity_kWh: float = Form(...),
    efficiency_wh_per_km: float = Form(...),
    torque_nm: float = Form(...),
    acceleration_0_100_s: float = Form(...),
    top_speed_kmh: float = Form(...)

):

    predicted_range = predict_range(

        battery_capacity_kWh,
        efficiency_wh_per_km,
        torque_nm,
        acceleration_0_100_s,
        top_speed_kmh

    )


    return templates.TemplateResponse(

        request=request,

        name="index.html",

        context={

            "prediction": round(predicted_range,2)

        }

    )

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

