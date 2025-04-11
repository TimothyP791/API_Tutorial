from fastapi import FastAPI # Import FastAPI inherits from Starlette

app = FastAPI() # Create an instance of FastAPI

# The @somthing is called a decorator
@app.get("/users/me") # Define a path operation decorator; Tells you the function below handles requests that go to / path using a get operation
async def read_users_me(): #define an asynchronous function
    return {"user id": "The current user"} # return the content

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user id": user_id}