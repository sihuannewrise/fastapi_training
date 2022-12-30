from fastapi import FastAPI
from pydantic import BaseModel, root_validator

app = FastAPI()

FORBIDDEN_NAMES = [
    'Luke Skywalker',
    'Darth Vader',
    'Leia Organa',
    'Han Solo',
]


class Person(BaseModel):
    name: str
    surname: str

    @root_validator
    def using_different_languages(cls, values):
        checked_value = values['name'].capitalize() + ' ' + values['surname'].capitalize()
        if checked_value in FORBIDDEN_NAMES:
            raise ValueError(
                'Это имя запрещено использовать!'
            )
        return values


@app.post('/hello')
def greetings(person: Person) -> dict[str, str]:
    result = ' '.join([person.name, person.surname])
    result = result.title()
    return {'Hello': result}
