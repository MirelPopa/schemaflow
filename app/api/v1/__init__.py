from fastapi import APIRouter

from app.api.v1 import contracts, submissions, teams

api_router = APIRouter()
api_router.include_router(teams.router)
api_router.include_router(contracts.router)
api_router.include_router(submissions.router)
