from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.contract import Contract
from app.schemas.contract import ContractCreate, ContractRead
from app.services.contract_service import ContractService

router = APIRouter(prefix="/contracts", tags=["Contracts"])


@router.post("/", response_model=ContractRead)
def create_contract(
    contract_create: ContractCreate, db: Session = Depends(get_db)
) -> Contract:
    service = ContractService(db)
    return service.create_contract(contract_create)


@router.get("/by_team/{team_id}", response_model=list[ContractRead])
def list_contracts(team_id: int, db: Session = Depends(get_db)) -> list[Contract]:
    service = ContractService(db)
    return service.list_contracts_for_team(team_id)
