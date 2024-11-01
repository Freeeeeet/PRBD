from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, orders, shipments, vehicles, drivers, warehouses, inventory, payments, invoices
from app.database import engine, Base

app = FastAPI()


# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Укажите разрешенные источники, например: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, OPTIONS и т.д.)
    allow_headers=["*"],   # Разрешить все заголовки
)
# Создание таблиц
Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(orders.router)
app.include_router(shipments.router)
# app.include_router(vehicles.router)
# app.include_router(drivers.router)
# app.include_router(warehouses.router)
# app.include_router(inventory.router)
app.include_router(payments.router)
app.include_router(invoices.router)
