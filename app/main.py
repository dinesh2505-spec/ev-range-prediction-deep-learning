"""
main.py

FastAPI web application for EV Range Prediction.
"""

import os

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.predictor import predict_range


# -------------------------------------------------
# Project paths
# -------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_DIR = os.path.join(
    BASE_DIR,
    "static"
)

TEMPLATE_DIR = os.path.join(
    BASE_DIR,
    "templates"
)


# -------------------------------------------------
# Create FastAPI application
# -------------------------------------------------

app = FastAPI(
    title="EV Range Prediction API",
    description="Predict EV driving range using Artificial Neural Network",
    version="1.0"
)


# -------------------------------------------------
# Static files (CSS)
# -------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static"
)


# -------------------------------------------------
# HTML Templates
# -------------------------------------------------

templates = Jinja2Templates(
    directory=TEMPLATE_DIR
)


# -------------------------------------------------
# Home page
# -------------------------------------------------

@app.get(
    "/",
    response_class=HTMLResponse
)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# -------------------------------------------------
# Prediction endpoint
# -------------------------------------------------

@app.post(
    "/predict",
    response_class=HTMLResponse
)
def predict(

    request: Request,

    battery_capacity_kWh: float = Form(...),

    efficiency_wh_per_km: float = Form(...),

    torque_nm: float = Form(...),

    acceleration_0_100_s: float = Form(...),

    top_speed_kmh: float = Form(...)

):

    # Run ANN prediction
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

            "prediction": round(
                predicted_range,
                2
            )

        }

    )