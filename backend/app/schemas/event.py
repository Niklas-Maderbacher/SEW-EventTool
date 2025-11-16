from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class EventBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)
    date: datetime = Field(...)
    description: str
    location_id: int = Field(...)
    organizer_id: int = Field(...)

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class EventInDB(EventBase):
    id: int

    class Config:
        from_attributes = True