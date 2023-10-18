from settings import settings
from typing import Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/user", status_code=501)
async def create_user():
    pass

@app.get("/user", status_code=501)
async def get_user():
    pass

@app.post("/item", status_code=501)
async def create_item():
    pass

@app.get("/item", status_code=501)
async def get_item():
    pass

if __name__ == '__main__':
    uvicorn.run(app, host=settings.uvicorn.host, port=settings.uvicorn.port)
