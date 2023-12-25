from typing import Optional

from pydantic import BaseModel


class AddressCreate(BaseModel):
    flat: str
    building: str
    city: str
    street: str

class AddressUpdate(BaseModel):
    is_archieve: Optional[bool] = None