#Mix Path, Query and Body parameters in FastAPI
from typing import Annotated

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

#Multiple body parameters
class User(BaseModel):
    username: str
    full_name: str | None = None


'''@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item: 
        results.update({"item": item})
    return results'''

'''@app.put("/items/{item_id}")
async def update_item(
    item_id: int, 
    item: Item, 
    user: User,
    #Ensures parameter is treated as a body parameter rather thatn a query parameter
    importance: Annotated[int, Body()] #importance is a singular value body parameter
    ):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results'''

# You can embed Body parameters to expecet key value with a model as the contents
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results