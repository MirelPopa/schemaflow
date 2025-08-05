from sqlalchemy.orm import Session
from app.models.contract import Contract
from app.schemas.contract import ContractCreate


class ContractRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, contract_create: ContractCreate) -> Contract:
        contract = Contract(**contract_create.model_dump())
        self.db.add(contract)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def get_by_team(self, team_id: int) -> list[Contract]:
        return self.db.query(Contract).filter_by(Contract.team_id == team_id).all()
