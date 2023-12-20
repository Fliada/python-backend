from dataclasses import asdict

from fastapi import APIRouter
from starlette.responses import JSONResponse

from api.model.Material import MaterialCreate, MaterialUpdate
from api.data import material

material_routes = APIRouter()


@material_routes.post('/create')
def insert_material(materialRequest: MaterialCreate):
    category_id = materialRequest.category_id
    name = materialRequest.name
    units = materialRequest.units
    material.create_material(category_id, name, units)
    return "Материал создан"


@material_routes.post('/update/{material_id}')
def update_material(material_id: str, materialUpdate: MaterialUpdate):
    if materialUpdate.name is not None:
        material.update_material(material_id, "name", materialUpdate.name)
    if materialUpdate.units is not None:
        material.update_material(material_id, "units", materialUpdate.units)
    if materialUpdate.category_id is not None:
        material.update_material(material_id, "category_id", materialUpdate.category_id)
    return "Материал обновлен"


@material_routes.get('/all')
def get_materials():
    all_materials = material.get_all_materials()
    return JSONResponse(content=[asdict(mat) for mat in all_materials])


@material_routes.get('/{material_id}')
def get_category(material_id: str):
    result_material = material.get_material(material_id)
    return JSONResponse(content=asdict(result_material))


@material_routes.delete('/{material_id}')
def delete_material(material_id: str):
    delete_material(material_id)
    return 'Удалена заявка с Id %s' % material_id
