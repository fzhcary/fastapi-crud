from fastapi import FastAPI

from app.api import ping

app = FastAPI()

# wire ping route to main app
app.include_router(ping.router)

