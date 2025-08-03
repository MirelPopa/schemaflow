from fastapi import APIRouter
from app.api.v1 import teams

api_router = APIRouter()
api_router.include_router(teams.router)
