from pydantic import BaseModel
from typing import Annotated
from fastapi import FastAPI, Body


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    print(item, "requeset.body")
    return item

@app.post("/items/{item_id}")
async def create_item(item_id:int, item: Item):
    print(type(item), "requeset.body")
    return {
        "item_id": item_id,
        **item.dict() # this was a pydyanitc class hence had to do like this else **item works to unpack a dictionary.
    }

"""The function parameters will be recognized as follows:

If the parameter is also declared in the path, it will be used as a path parameter.
If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.
"""





class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/mul_body/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    """For such two body parameteres Fast Api expects you to have request body like this 
    Notice that even though the item was declared the same way as before, it is now expected to be inside of the body with a key item.
    {
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
    }
    
    """
    results = {"item_id": item_id, "item": item, "user": user}
    return results

@app.put("/sin_body/{item_id}")
async def update_item(item_id: int, item: Item):
    """For such two body parameteres Fast Api expects you to have request body like this 
    
    {
  
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    
    }
    
    """
    results = {"item_id": item_id, "item": item,}
    return results



@app.put("/sin_body/{item_id}")
async def update_item(item_id: int, item: Annotated[Item,Body(embed=True)]):
    """For single but embedeed body parameteres Fast Api expects you to have request body like this 

    
    {
    "item":{
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
    
    }
    
    """
    results = {"item_id": item_id, "item": item,}
    return results




# data = {"names": "himanshu", "age": 50, "class": "eight"}
# la = {"hello": "greet", "bro": "yes"}
# print({**data, **la})