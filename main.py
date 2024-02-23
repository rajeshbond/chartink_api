

from fastapi import FastAPI,BackgroundTasks
from chartink import trasferDataToGoogleSheet
from datetime import datetime, timedelta
import asyncio
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Fetch data in the startup context
#     trasferDataToGoogleSheet()
#     yield
#     # No need to explicitly close resources here
# app = FastAPI(lifespan=lifespan)

# @app.get("/")
# async def root(lifespan):
#     print("Hello")
#     return {"message": "started"}

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def under_construction():
    with open("templates/under_construction.html", "r") as file:
        return file.read()
    
@app.get('/start')
async def start():
    BackgroundTasks.add_task(trasferDataToGoogleSheet())
    return {"Message" : "Server Started"}




