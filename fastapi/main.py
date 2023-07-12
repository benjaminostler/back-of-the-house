from fastapi import FastAPI
from routers import reservations, menu, accounts
from authenticator import authenticator
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.include_router(reservations.router)
app.include_router(menu.router)
app.include_router(authenticator.router)
app.include_router(accounts.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
