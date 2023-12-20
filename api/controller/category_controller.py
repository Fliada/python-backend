import json
from dataclasses import asdict

from fastapi import APIRouter

from api.data import category

category_routes = APIRouter()


@category_routes.get('/all')
def get_all_categories():
    all_materials = category.get_all_categories()
    return json.dumps(all_materials, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4, ensure_ascii=False)


@category_routes.get('/{category_id}')
def get_category(category_id: str):
    result_category = category.get_category(category_id)
    print(json.dumps(asdict(result_category), ensure_ascii=False))
    return json.dumps(asdict(result_category), ensure_ascii=False)


