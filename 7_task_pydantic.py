from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


class Categories(str, Enum):
    PRINTER = 'Принтеры'
    MONOTOR = 'Мониторы'
    PERIFERIA = 'Доп. оборудование'
    INPUT_DEVICE = 'Устройства ввода'


class Person(BaseModel):
    name: str
    surname: str
    age: Optional[int]
    is_staff: bool = False


class AuctionLot(BaseModel):
    category: Categories
    name: str
    model: Optional[str]
    start_price: int = 1000
    seller: Person


@app.post('/new-lot', tags=['auction house'],)
def register_lot(lot: AuctionLot,) -> dict[str, str]:
    return {
        'result': 'Ваша заявка зарегистрирована!',
        'lot': lot,
    }
