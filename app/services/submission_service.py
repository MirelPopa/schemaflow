from jsonschema import validate, ValidationError
from app.repositories.contract_repo import ContractRepository
from app.repositories.submission_repo import SubmissionRepository
from sqlalchemy.orm import Session
from app.schemas.submission import SubmissionCreate
from app.models.submission import Submission
from app.models.contract import Contract


class SubmissionService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = SubmissionRepository(db)
        self.contract_repo = ContractRepository(db)

    def create(self, submission: SubmissionCreate) -> Submission:
        contract = self.contract_repo.db.query(Contract).filter_by(id=submission.contract_id).first()
        if not contract:
            raise ValueError(f"Contract {submission.contract_id} does not exist")

        try:
            validate(instance=submission.payload, schema=contract.json_schema)
            status = "valid"
            error = None
        except ValidationError as ve:
            status = "invalid"
            error = str(ve)

        return self.repo.create(submission, status, error)

    def list_by_contract(self, contract_id: int) -> list[Submission]:
        return self.repo.list_by_contract(contract_id)
