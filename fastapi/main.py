from fastapi import FastAPI
from routers import accounts, menu

app = FastAPI()
app.include_router(accounts.router)
app.include_router(menu.router)
