from pydantic import BaseModel


class MaterialCreate(BaseModel):
    category_id: int
    name: str
    units: str
