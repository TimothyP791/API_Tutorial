# A Requst body is data sent by the client to your API
from fastapi import FastAPI
from pydantic import BaseModel # Pydantic is used for data validation

# Declare data model as a class that inherits from BaseModel
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI() #App istance of FastAPI

# Create a request body with the Item model
@app.post("/items/")
async def create_item(item: Item):# parameter item is of type Item class
    return item

'''# Create a request body with the Item model using a dictionary
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()  # Convert the Pydantic model to a dictionary
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
#Request body with path parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}'''

#Request body with query parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q" : q})
    return result