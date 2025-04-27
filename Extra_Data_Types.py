#UUID str
#datetime.datetime str format 2008-09-15T15:53:00+05:00
#datetime.date str format 2008-09-15
#datetime.time str format 14:23:55.003
#datetime.timedelta represented as a float of total seconds
#frozenset read as a list and interpreted as a set in responses set will be converted to list
#bytes responses will be treated as str
#Decimal handled the same as float, but with more precision
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()

@app.put("/itmes/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }