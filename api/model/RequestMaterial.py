from pydantic import BaseModel


class RequestMaterial(BaseModel):
    request_id: int
    material_id: int
    count: int
