from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/multiplication')
def multiplication(
    length: int,
    width: int,
    depth: Optional[int]=1,
) -> int:
    res = length * width * depth
    return res
