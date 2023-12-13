import json
from dataclasses import asdict

from fastapi import APIRouter

from api.model.Material import MaterialCreate
from api.data import material

material_routes = APIRouter()


@material_routes.post('/create')
def insert_material(materialRequest: MaterialCreate):
    category_id = materialRequest.category_id
    name = materialRequest.name
    units = materialRequest.units
    material.create_material(category_id, name, units)
    return "Материал создан"


@material_routes.get('/{material_id}')
def get_category(material_id: str):
    result_material = material.get_material(material_id)
    print('Возвращена категория с id %s' % material_id)
    print(json.dumps(asdict(result_material), ensure_ascii=False))
    return json.dumps(asdict(result_material), ensure_ascii=False)


@material_routes.delete('/{material_id}')
def delete_material(material_id: str):
    delete_material(material_id)
    return 'Удалена заявка с Id %s' % material_id
