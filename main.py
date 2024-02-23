
from sched import scheduler
from fastapi import FastAPI,BackgroundTasks
import time
from chartink import trasferDataToGoogleSheet
from datetime import datetime, timedelta
import asyncio
from contextlib import asynccontextmanager

from nse_data import maketStatus



app = FastAPI()


@app.get('/')
async def start():
    BackgroundTasks.add_task(trasferDataToGoogleSheet())
    return {"Message" : "Server Started"}



# @app.get('/')
# async def start():
#    trasferDataToGoogleSheet()
# async def start():
#     await trasferDataToGoogleSheet()
# trasferDataToGoogleSheet()



# # Only run the server if this script is executed directly
# if __name__ == "__app__":
#     # Start the Uvicorn server
#     uvicorn.run(app, host="0.0.0.0", port=8000)

