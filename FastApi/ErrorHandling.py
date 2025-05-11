from fastapi import FastAPI, HTTPException,Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

# @app.exception_handler(RequestValidationError)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_name_to_request(request:Request, call_next):
    print(request, "request")
    request.state.name = "John Doe" 
    print("first")
    body = await request.body()
    print(body, "body")
    response = await call_next(request)
    print("second")

    return response


@app.get("/items/{item_id}")
async def read_item(request:Request, item_id: str, name: str):
    print(request.state.name , "STATE")
    print(item_id, "itemiD")
    print("third")
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    print("fourth")
    return {"item": items[item_id]}

