from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/math-sum')
def math_sum(
    add: list[float] = Query(
        ..., gt=0, lt=100,
        title='Параметр', description='Можно вводить несколько параметров',
    ),
) -> float:
    return round(sum(add), 2)
