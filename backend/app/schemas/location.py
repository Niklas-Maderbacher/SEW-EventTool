from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class LocationBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    address: str = Field(..., min_length=10, max_length=100)
    capacity: int = Field(...)

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    pass

class LocationInDB(LocationBase):
    id: int

    class Config:
        from_attributes = True
