from fastapi import APIRouter
from api.v1.endpoints import operadora

api_router = APIRouter()
api_router.include_router(operadora.router, prefix='/operadoras', tags=["operadoras"])