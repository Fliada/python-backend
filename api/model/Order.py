from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class Forms(BaseModel):
    material_id: int
    count: int


class OrderCreate(BaseModel):
    forms: List[Forms]
    comment: str
    address: str
    date_selected: datetime


class OrderUpdate(BaseModel):
    address: Optional[str] = None
    comment: Optional[str] = None
    date_selected: Optional[datetime] = None
