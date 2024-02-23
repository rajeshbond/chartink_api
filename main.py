import asyncio
from sched import scheduler
from fastapi import FastAPI
import pytz
from chartink import trasferDataToGoogleSheet
import uvicorn
from datetime import datetime, timedelta

app = FastAPI()



@app.get('/')
async def start():
   trasferDataToGoogleSheet()
async def start():
    await trasferDataToGoogleSheet()
trasferDataToGoogleSheet()



# # Only run the server if this script is executed directly
# if __name__ == "__app__":
#     # Start the Uvicorn server
#     uvicorn.run(app, host="0.0.0.0", port=8000)

