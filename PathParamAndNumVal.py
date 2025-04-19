from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

'''@app.get("/items/{item_id}")
async def read_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results'''
# you can put the parameters in any order Annotated will negate the problem altogether


# The * is used to indicate that all parameters after it are key value pair arguments
'''@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results'''

# ge=1 means greater than or equal to 1
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

#gt=1 means greater than 1
#le=10 means less than or equal to 10
#lt=10 means less than 10
#These validations work on float values as well