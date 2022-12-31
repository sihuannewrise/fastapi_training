from fastapi import FastAPI
from enum import IntEnum

app = FastAPI()


class ObjectDiametr(IntEnum):
    SUN = 1_392_000
    JUPITER = 139_822
    SATURN = 116_464
    URANUS = 50_724
    NEPTUNE = 49_224
    EARTH = 12_742
    VENUS = 12_104
    MARS = 6_780
    GANYMEDE = 5_262
    TITAN = 5_151
    MERCURY = 4_879


@app.get('/get-solar-object-name')
def get_solar_object_name(
    diameter: ObjectDiametr,
) -> str:
    return diameter.name
