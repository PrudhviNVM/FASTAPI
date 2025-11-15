from fastapi import FastAPI
from app.backend.routers import sip

app = FastAPI(title = "MF SIP Calculator", version="1.0.0")

app.include_router(sip.router)


@app.get("/")
def home():
    return {"message": "Welcome to the Mutual Fund SIP Calculator API"}
