from pydantic import BaseModel, EmailStr, Field, constr, condecimal
from typing import List, Optional
from datetime import datetime



class UserCreateRequest(BaseModel):
    name: str = Field(..., pattern=r'^[\w\sа-яА-ЯёЁ-]{1,50}$',
                      description="Must be 1-50 characters: letters (any language), numbers, spaces, and - only.",
                      examples=["Ryan Gosling"])
    email: EmailStr = Field(..., description="Must be valid e-mail address.", examples=["gosling@gmail.com"])
    password: str = Field(..., pattern=r'^.{8,50}$',
                          description="Password must be between 8 and 50 characters.", examples=["StrongPass123"])
    # token: str = Field(..., description="Authorization token to verify user identity.",
    #                    examples=["eyJhbGciOiJIUzI1NiIsInR5cCI6"])

    class Config:
        from_attributes = True


class UserCreateResponse(BaseModel):
    success: bool

    class Config:
        from_attributes = True


class LoginUserRequest(BaseModel):
    email: EmailStr = Field(..., description="Must be valid e-mail address.", examples=["gosling@gmail.com"])
    password: str = Field(..., pattern=r'^.{8,50}$',
                          description="Password must be between 8 and 50 characters.", examples=["StrongPass123"])

    class Config:
        from_attributes = True


class LoginUserResponse(BaseModel):
    token: str


class OrderStatus(BaseModel):
    status_name: str
    created_at: datetime

    class Config:
        from_attributes = True


class OrderDeliveryStatusResponse(BaseModel):
    id: int
    status_name: str
    description: str

    class Config:
        from_attributes = True


class OrderCreateRequest(BaseModel):
    weight: condecimal(gt=0, max_digits=10, decimal_places=2) = Field(...,
                                    description="Weight of the order in kilograms. Must be positive.", examples=[12.5])
    source_location: str = Field(..., min_length=1, max_length=100,
                                 description="Source location address or name.", examples=["Warehouse A"])
    destination_location: str = Field(..., min_length=1, max_length=100,
                                      description="Destination location address or name.",
                                      examples=["Customer's address"])
    total_price: condecimal(gt=0, max_digits=10, decimal_places=2) = Field(...,
                                  description="Total price of the order in currency. Must be positive.",
                                                                           examples=[199.99])
    # token: str = Field(..., description="Authorization token to verify user identity.",
    #                    examples=["eyJhbGciOiJIUzI1NiIsInR5cCI6"])

    class Config:
        from_attributes = True


class OrderCreateResponse(BaseModel):
    order_id: int

    class Config:
        from_attributes = True


class OrderInfoResponse(BaseModel):
    id: int
    weight: float
    source_location: str
    destination_location: str
    tracking_number: str
    total_price: float
    created_at: datetime
    order_statuses: list[OrderStatus] = []

    class Config:
        from_attributes = True


class OrderChangeStatusRequest(BaseModel):
    order_id: int
    status_id: int

    class Config:
        from_attributes = True


class OrderChangeStatusResponse(BaseModel):
    success: bool

    class Config:
        from_attributes = True


class OrderDeliveryStatusesResponse(BaseModel):
    statuses: list[OrderDeliveryStatusResponse]

    class Config:
        from_attributes = True



