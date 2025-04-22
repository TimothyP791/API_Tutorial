#List fields
from typing import List, Union # Needed to define a list with a type parameter

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

'''class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = [] ''' # Define an attribute to be a subtype
    # The above list can hold any type of data even different types in the same list
'''class Item(BaseModel):
    name: str
    description: Union[str, None] = None  # Union allows for multiple types
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []  # List of strings'''

# Declare tags as a set of strings to ensure uniqueness
'''class Item(BaseModel):
    name: str
    description: Union[str, None] = None  # Union allows for multiple types
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()  # Set of unique strings

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id" : item_id, "item": item}
    return results'''

#Nested Models

class Image(BaseModel):
    url: HttpUrl #pydantic's HttpURL type ensures the URL is valid
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: list[Image] | None = None # Optional nested model Can also use models as subtypes of lists, sets, etc.

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# You can deeply nest models as needed like  an Image model
# inside an Item model inside another model, etc.

#if the value of the JSON body you expect is a JSON array
#you can declare the type in the parameter of the funciton

'''@app.post("/items/multiple/")
async def create_multiple_images(images: list[Image]): #here is the expected type
    return images'''

# Use a dict to get different keys with different types
@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]): # recieves any dict with int keys and float values
    return weights