from fastapi import APIRouter

from api.data import request_materials
from api.model.RequestMaterial import RequestMaterial

request_materials_routes = APIRouter()


@request_materials_routes.post('/create')
def insert_request_material(requestMaterial: RequestMaterial):
    request_id = requestMaterial.request_id
    material_id = requestMaterial.material_id
    count = requestMaterial.count
    request_materials.create_request_material(request_id, material_id, count)
    return 'Запрашиваемый ресурс создан'
