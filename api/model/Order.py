from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OrderCreate(BaseModel):
    user_id: int
    address: str
    comment: str
    date_selected: datetime


class OrderUpdate(BaseModel):
    user_id: Optional[int] = None
    address: Optional[str] = None
    comment: Optional[str] = None
    date_selected: Optional[datetime] = None

