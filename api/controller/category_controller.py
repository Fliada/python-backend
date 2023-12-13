import json
from dataclasses import asdict

from fastapi import APIRouter
from api.data import category
from api.model.Category import Category

category_routes = APIRouter()


@category_routes.get('/{category_id}')
def get_category(category_id: str):
    result_category = category.get_category(category_id)
    print(json.dumps(asdict(result_category), ensure_ascii=False))
    return json.dumps(asdict(result_category), ensure_ascii=False)