from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Tags(str, Enum):
    IMMUTABLE = 'immutable'
    MUTABLE = 'mutable'


@app.post(
    '/a',
    tags=[Tags.IMMUTABLE],
    summary='Первая функция',
    response_description='Возвращается строка',
)
def a() -> str:
    """
    Функция A метода POST.
    """
    return 'Вот это ответ!'


@app.get(
    '/b',
    tags=[Tags.IMMUTABLE],
    summary='Вторая функция',
    description='Эндпоинт /b',
    response_description='Возвращается список строк',
)
def b() -> list[str]:
    return ['Вот', 'это', 'ответ!']


@app.post(
    '/c',
    tags=[Tags.IMMUTABLE],
    summary='Трертья функция',
    response_description='Возвращается число',
)
def c() -> int:
    """
    Функция С метода POST.
    """
    return 42


@app.get(
    '/d',
    tags=[Tags.MUTABLE],
    summary='Четвертая функция',
    description='Эндпоинт /d',
    response_description='Возвращается словарь',
)
def d() -> dict[str, str]:
    return {'Вот': 'это ответ!'}
