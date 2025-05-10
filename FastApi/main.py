from fastapi import FastAPI   #FastAPI is a Python class that provides all the functionality for your API.
from enum import Enum
app = FastAPI() # create an instance like in express


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/item/43")
async def get_single_item():
    print("This is 43 wala item")
    return {"message": f"this is the the id {43}"}

@app.get("/item/{item_id}")
async def get_single_item(item_id:int):
    print(item_id, "item")
    return {"message": f"this is the the id {item_id}"}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
"""When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters."""
@app.get("/items/")   
async def read_item(skip: int = 0, limit: int = 10):
    """http://127.0.0.1:8000/items/?skip=1&limit=1""" # this is the url.
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    """http://127.0.0.1:8000/items/3?q=6"""
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/bool_items/{item_id}")
async def read_item(item_id: str, q: bool | None = None):   # bool also accepts the values as on, yes, True, true, 1 all are truthy values. 
    """http://127.0.0.1:8000/items/3?q=6"""
    print(q)
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/req_items/{item_id}")
async def read_user_item(item_id: str, needy: str|None = None):
    """http://127.0.0.1:8000/req_items/3?needy=hello"""

    item = {"item_id": item_id, "needy": needy}
    return item
