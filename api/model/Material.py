from typing import Optional

from pydantic import BaseModel


class MaterialCreate(BaseModel):
    category_id: int
    name: str
    units: str


class MaterialUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    units: Optional[str] = None


class Material(BaseModel):
    name: str
    count: int
    units: str
    category: str
