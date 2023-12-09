from pydantic import BaseModel


class AddressCreate(BaseModel):
    flat: str
    building: str
    city: str
    street: str
    creator_id: int
