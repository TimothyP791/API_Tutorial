'''from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
# Parameters declared that are not part of the path parameters are automatically query parameters
async def read_item(skip: int = 0, limit: int = 10): #query parameters are skip and limit with default values
    return fake_items_db[skip : skip + limit]

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
# the |  None = none makes q an optional parameter with default value none
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
#Any bool type parameter is converted in the URL so 1,yes,true, etc. delivers the value
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}") #path parmeters are in app.get brackets
async def read_user_item(# Fastapi will determine path and query parameters for you by name
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item'''

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
#In order to make a query parameter required don't declare a default value
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item