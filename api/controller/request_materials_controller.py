from dataclasses import asdict

from fastapi import APIRouter
from starlette.responses import JSONResponse

from api.data import request_materials
from api.model.RequestMaterial import RequestMaterial, AllRequestMaterial

request_materials_routes = APIRouter()


@request_materials_routes.post('/create')
def insert_request_material(requestMaterial: RequestMaterial):
    request_id = requestMaterial.request_id
    material_id = requestMaterial.material_id
    count = requestMaterial.count
    request_materials.create_request_material(request_id, material_id, count)
    return 'Запрашиваемый ресурс создан'


@request_materials_routes.get('/all')
def get_materials(order_id: AllRequestMaterial):
    all_request_materials = request_materials.get_all_request_material(order_id.order_id)
    return JSONResponse(content=[asdict(req_mat) for req_mat in all_request_materials])


