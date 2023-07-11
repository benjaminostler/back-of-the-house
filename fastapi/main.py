from fastapi import FastAPI
from routers import reservations, menu

app = FastAPI()
app.include_router(reservations.router)
app.include_router(menu.router)
