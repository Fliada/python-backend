from fastapi import APIRouter

from api.model.Material import MaterialCreate
from api.data.material import create_material, delete_material

material_routes = APIRouter()


@material_routes.post('/material/create')
def insert_material(materialRequest: MaterialCreate):
    category_id = materialRequest.category_id
    name = materialRequest.name
    units = materialRequest.units
    create_material(category_id, name, units)
    return "Материал создан"


@material_routes.delete('/material/<int:post_id>')
def delete_material(order_id):
    delete_material(order_id)
    return 'Удалена заявка с Id %d' % order_id
