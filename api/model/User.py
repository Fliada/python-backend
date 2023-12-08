import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    is_superuser: bool
    is_active: bool
    is_staff: bool
    first_name: str
    last_name: str
    second_name: str
    password: str
    email: str
    phone_number: int


class UserLogin(BaseModel):
    email: str
    password: str
