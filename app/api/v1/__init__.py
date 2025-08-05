from fastapi import APIRouter
from app.api.v1 import teams, contracts, submissions

api_router = APIRouter()
api_router.include_router(teams.router)
api_router.include_router(contracts.router)
api_router.include_router(submissions.router)
