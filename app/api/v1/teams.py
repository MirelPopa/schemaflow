from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.team import TeamCreate, TeamRead
from app.services.team_service import TeamService

router = APIRouter(prefix="/teams", tags=["Teams"])


@router.post("/", response_model=TeamRead)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    service = TeamService(db)
    try:
        return service.create_team(team)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[TeamRead])
def list_teams(db: Session = Depends(get_db)):
    service = TeamService(db)
    return service.list_teams()
