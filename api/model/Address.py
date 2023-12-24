from typing import Optional

from pydantic import BaseModel


class AddressCreate(BaseModel):
    flat: str
    building: str
    city: str
    street: str
    creator_id: int

class AddressUpdate(BaseModel):
    is_archieve: Optional[bool] = None