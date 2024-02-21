from fastapi import FastAPI
from chartink import trasferDataToGoogleSheet
import uvicorn

app = FastAPI()

@app.get('/')
async def start():
    trasferDataToGoogleSheet()

# Only run the server if this script is executed directly
if __name__ == "__app__":
    # Start the Uvicorn server
    uvicorn.run(app, host="0.0.0.0", port=8000)

