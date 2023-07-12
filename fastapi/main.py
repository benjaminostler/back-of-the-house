from fastapi import FastAPI
from routers import accounts, menu_item

app = FastAPI()
app.include_router(accounts.router)
app.include_router(menu_item.router)
