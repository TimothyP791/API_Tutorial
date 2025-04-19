from typing import Annotated
from fastapi import FastAPI, Query

from pydantic import AfterValidator

app = FastAPI()


'''@app.get("/items/")
async def read_items(
    # ^ meand starts with the following characters
    # fixedquery has the exact value fixedquery
    # $ meands ends her with no following characters
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$") #could use regex instead of pattern
    ] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

# Old method using Query
'''@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

# default values other than None 
'''@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

# required parameters using Query
'''@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]): # dont declare default values
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

# declare None as a valid type but not a default value
# This maks the parameter required but allows None as a value
'''@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)]): # dont declare default values
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

#declare a list as a query parameter
'''@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query(min_length=3)] = ["foo", "bar"]): # default value is a list
    query_items = {"q": q}
    return query_items'''

# Use list directly instead of list[str] but fastapi will not validate the type of the list items
'''@app.get("/items/")
async def read_items(q: Annotated[list | None, Query(min_length=3)] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items'''

# Add a title and description to the query parameter
'''@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(
        title="Query string",
        description= "Query string for the items to search in the database that have a good match",
        min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

# Alias for the query parameter
'''@app.get("/items/")
async def read_items(
    # Since item-query is not a valid Python variable name, we use an alias to map it to the query parameter
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''
# Use deprecated query parameter
'''@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results'''

# To exclude a query parameter set the parameter include_in_schema of Qery to false
'''@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}'''
# Use AfterValidator to validate the query parameter
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items())) # convert data tuple to a list
    return {"id": id, "name": item}
