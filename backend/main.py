from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, orders
from app.database import engine, Base

app = FastAPI(openapi_prefix="/proekt-db/api")


# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/user", tags=["user"])
app.include_router(orders.router, prefix="/orders", tags=["order"])
