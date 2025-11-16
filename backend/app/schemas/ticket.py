from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

from app.models.ticket_status import TICKET_STATUS

class TicketBase(BaseModel):
    owner: int = Field(...)
    seat_number: str = Field(..., min_length=5, max_length=50)
    price: float = Field(...)
    event_id: int = Field(...)
    status: TICKET_STATUS = Field(...)

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    pass

class TicketInDB(TicketBase):
    id: int

    class Config:
        from_attributes = True