from fastapi import FastAPI
from routers import (
    reservations,
    menu_items,
    accounts,
    orders,
    order_items,
    cart,
    cart_items,
)
from authenticator import authenticator
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.include_router(reservations.router)
app.include_router(menu_items.router)
app.include_router(authenticator.router)
app.include_router(accounts.router)
app.include_router(orders.router)
app.include_router(order_items.router)
app.include_router(cart.router)
app.include_router(cart_items.router)
# changed to allow deployment database to make CORS requests

origins = [os.environ.get("CORS_HOST", None), "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         os.environ.get(
#             "CORS_HOST",
#             "http://localhost:3000",
#         )
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# origins = [
#     os.environ.get("CORS_HOST", "http://localhost:3000"),
#     os.environ.get("CORS_HOST", "http://localhost:8000"),
#     os.environ.get("CORS_HOST", "https://mar-2-pt-fastrapi.mod3projects.com"),
#     os.environ.get("CORS_HOST", "https://backofthehouse.gitlab.io/"),
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
def root():
    return {"message": "You hit the root path!"}
