from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


# User schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Order schema
class OrderCreate(BaseModel):
    total_price: float
    user_id: Optional[int] = None

    class Config:
        orm_mode = True


class OrderResponse(BaseModel):
    id: int
    total_price: float
    created_at: datetime
    updated_at: datetime
    user_id: Optional[int]

    class Config:
        orm_mode = True

# Shipment schema
class ShipmentCreate(BaseModel):
    weight: float
    destination: str
    status: str

    class Config:
        orm_mode = True


class ShipmentResponse(BaseModel):
    id: int
    weight: float
    destination: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Vehicle schema
class VehicleCreate(BaseModel):
    license_plate: str
    capacity: float
    driver_id: Optional[int]  # Допускаем, что может не быть водителя

    class Config:
        orm_mode = True


class VehicleResponse(BaseModel):
    id: int
    license_plate: str
    capacity: float
    driver_id: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Driver schema
class DriverBase(BaseModel):
    name: str


class DriverCreate(DriverBase):
    class Config:
        orm_mode = True


class DriverResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Warehouse schema
class WarehouseCreate(BaseModel):
    location: str
    capacity: float

    class Config:
        orm_mode = True


class WarehouseResponse(BaseModel):
    id: int
    location: str
    capacity: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Inventory schema
class InventoryBase(BaseModel):
    item_name: str
    quantity: int


class InventoryCreate(InventoryBase):
    warehouse_id: int

    class Config:
        orm_mode = True


class InventoryResponse(InventoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Payment schema
class PaymentCreate(BaseModel):
    amount: float
    order_id: int

    class Config:
        orm_mode = True


class PaymentResponse(BaseModel):
    id: int
    amount: float
    order_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# Invoice schema
class InvoiceCreate(BaseModel):
    total_amount: float
    order_id: int

    class Config:
        orm_mode = True


class InvoiceResponse(BaseModel):
    id: int
    total_amount: float
    created_at: datetime
    updated_at: datetime
    order_id: int

    class Config:
        orm_mode = True