from fastapi import FastAPI
from app.router import prayer_routers

app = FastAPI()

app.include_router(prayer_routers.router)

@app.get("/")
async def root():
    return {
        "message": "CrossAPI Root Print"
    }