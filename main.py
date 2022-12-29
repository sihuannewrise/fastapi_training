from enum import Enum
from typing import Optional, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


class Person(BaseModel):
    name: str
    surname: Union[str, list[str]]
    age: Optional[int]
    is_staff: bool = False
    education_level: Optional[EducationLevel]


@app.post('/hello')
def greetings(person: Person) -> dict[str, str]:
    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname
    result = ' '.join([person.name, surnames])
    result = result.title()
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}
