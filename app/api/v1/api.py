from fastapi import APIRouter
from .endpoints import marcas

api_router = APIRouter()


api_router.include_router(marcas.router, prefix="/marcas", tags=["marcas"])
