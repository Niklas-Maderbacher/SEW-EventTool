from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

from app.models.user_roles import USER_ROLE


class UserBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=15)
    email: EmailStr = Field(..., min_length=7, max_length=50)
    phone_number: str
    role: USER_ROLE


class UserCreate(UserBase):
    password: str = Field(..., min_length=1, max_length=50)


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: int

    class Config:
        from_attributes = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    password_hash: str
