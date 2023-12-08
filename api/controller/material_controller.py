from flask import Blueprint, session, request
from api.data import request
from api.data.material import create_material, delete_material

material_routes = Blueprint('material_routes', __name__)


@material_routes.route('/material/create', methods=['POST'])
def insert_material():
    if session['role'] == 'admin':
        data = request.get_json()

        category_id = data.get('category_id')
        name = data.get('name')
        units = data.get('units')
        create_material(category_id, name, units)
        return "Материал создан"
    else:
        return "Недостаточно прав"


@material_routes.route('/material/<int:post_id>', methods=['DELETE'])
def delete_material(order_id):
    if session['role'] == 'admin':
        delete_material(order_id)
        return 'Удалена заявка с Id %d' % order_id
    else:
        return "Недостаточно прав"
