from fastapi import FastAPI, Path, Query
from typing import Optional
from enum import Enum

app = FastAPI()


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get(
    '/{name}',
    tags=['common methods'],
    summary='Общее приветствие',
    response_description='Полная строка приветствия'
)
def greetings(
    *,
    name: str = Path(..., min_length=2, max_length=20),
    surname: str = Query(..., min_length=2, max_length=50),
    age: Optional[int] = None,
    is_staff: bool = False,
    education_level: Optional[EducationLevel] = None,
    cyrillic_string: str = Query('Только кириллица', regex='^[А-Яа-яЁё ]+$'),
) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if education_level is not None:
        result += ', ' + education_level.lower()
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}
