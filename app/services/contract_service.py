from sqlalchemy.orm import Session
from app.models.contract import Contract
from app.schemas.contract import ContractCreate
from app.repositories.contract_repo import ContractRepository


class ContractService:
    def __init__(self, db: Session):
        self.repo = ContractRepository(db)

    def create_contract(self, contract_create: ContractCreate) -> Contract:
        return self.repo.create(contract_create)

    def list_contracts_for_team(self, team_id: int) -> list[Contract]:
        return self.repo.get_by_team(team_id)
