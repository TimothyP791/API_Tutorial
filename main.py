'''from fastapi import FastAPI # Import FastAPI inherits from Starlette

app = FastAPI() # Create an instance of FastAPI

# The @somthing is called a decorator
@app.get("/users/me") # Define a path operation decorator; Tells you the function below handles requests that go to / path using a get operation
async def read_users_me(): #define an asynchronous function
    return {"user id": "The current user"} # return the content

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user id": user_id} '''
#Enumerators
'''from enum import Enum

from fastapi import FastAPI

# Use Enum to define a set of model names
# Inherits from str and Enum to allow string values
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName): # Create path parameter with the type annotation using the enum class you created
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Lerning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}'''
#file Path as path parameter
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")#the parameter is file_path and the :path tells it that the parameter should math any path
async def read_file(file_path: str):
    return {"file_path": file_path}