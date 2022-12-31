from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class PrompterHint(BaseModel):
    actor: str
    replica: str

    class Config:
        title = 'Класс подсказок'
        min_anystr_length = 2
        schema_extra = {
           'examples': {
                'work_1': {
                    'summary': 'Колобок',
                    'description': 'Первое произведение',
                    'value': {
                       'actor': 'Медведь',
                       'replica': 'Колобок, колобок, я тебя съем!',
                    }
                },
                'work_2': {
                    'summary': 'Гамлет, принц датский',
                    'description': 'Второе произведение',
                    'value': {
                       'actor': 'Гамлет',
                       'replica': 'Бедный Йорик! Я знал его, Горацио.',
                    }
                },
                'work_3': {
                    'summary': 'Палата номер 6',
                    'description': 'Третье произведение',
                    'value': {
                        'actor': 'Рагин',
                        'replica': 'Покой и довольство человека не вне его, а в нём самом.',
                    }
                }
            }
        }


@app.post('/give-a-hint')
def send_prompt(
    hint: PrompterHint = Body(
            ..., examples=PrompterHint.Config.schema_extra['examples']
    )
) -> dict[str, str]:
    return hint
