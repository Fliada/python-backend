from datetime import datetime

from pydantic import BaseModel


class OrderCreate(BaseModel):
    user_id: int
    address_id: int
    comment: str
    date_selected: datetime
