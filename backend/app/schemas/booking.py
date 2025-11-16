from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class BookingBase(BaseModel):
    user_id: int = Field(...)
    ticket_id: int = Field(...)
    date: datetime

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BookingBase):
    pass

class BookingInDB(BookingBase):
    id: int

    class Config:
        from_attributes = True