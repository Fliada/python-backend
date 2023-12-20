from dataclasses import asdict

from fastapi import APIRouter
from starlette.responses import JSONResponse

from api.data import category

category_routes = APIRouter()


@category_routes.get('/all')
def get_all_categories():
    all_categories = category.get_all_categories()
    formatted_categories = [asdict(cat) for cat in all_categories]
    return JSONResponse(content=formatted_categories)


@category_routes.get('/{category_id}')
def get_category(category_id: str):
    result_category = category.get_category(category_id)
    return JSONResponse(content=asdict(result_category))


