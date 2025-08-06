from sqlalchemy.orm import Session

from app.models.team import Team
from app.schemas.team import TeamCreate


class TeamRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, team_create: TeamCreate) -> Team:
        team = Team(**team_create.model_dump())
        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)
        return team

    def get_by_name(self, name: str) -> Team | None:
        return self.db.query(Team).filter(Team.name == name).first()

    def get_all(self) -> list[Team]:
        return self.db.query(Team).all()
