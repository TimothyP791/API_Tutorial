from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/itmes/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}