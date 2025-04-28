from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
# Header will convert _ to - in the header name automatically
# if you want to cancel automatic conversion you can use Header(convert_underscores=False) 

#To make duplicate headers work you can use the List type
# e.g. user_agent: Annotated[list[str] | None Header()] = None