from sqlalchemy.orm import Session
from app.schemas.team import TeamCreate
from app.repositories.team_repo import TeamRepository
from app.models.team import Team


class TeamService:
    def __init__(self, db: Session):
        self.repo = TeamRepository(db)

    def create_team(self, team_create: TeamCreate) -> Team:
        existing = self.repo.get_by_name(team_create.name)
        if existing:
            raise ValueError("Team name already exists")
        return self.repo.create(team_create)

    def list_teams(self) -> list[Team]:
        return self.repo.get_all()
