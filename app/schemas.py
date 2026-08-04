
from pydantic import BaseModel


class EVInput(BaseModel):

    battery_capacity_kWh: float

    efficiency_wh_per_km: float

    torque_nm: float

    acceleration_0_100_s: float

    top_speed_kmh: float