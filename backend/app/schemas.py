from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime


# User schema
class UserCreateRequest(BaseModel):
    name: str = Field(..., pattern=r'^[\w\sа-яА-ЯёЁ-]{1,50}$',
                      description="Must be 1-50 characters: letters (any language), numbers, spaces, and - only.",
                      examples=["Ryan Gosling"])
    email: EmailStr = Field(..., description="Must be valid e-mail address.", examples=["gosling@gmail.com"])
    password: str = Field(..., pattern=r'^.{8,50}$',
                          description="Password must be between 8 and 50 characters.", examples=["StrongPass123"])

    class Config:
        from_attributes = True


class UserCreateResponse(BaseModel):
    success: bool

    class Config:
        from_attributes = True

