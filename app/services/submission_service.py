from sqlalchemy.orm import Session

from app.models.submission import Submission
from app.repositories.contract_repo import ContractRepository
from app.repositories.submission_repo import SubmissionRepository
from app.schemas.submission import SubmissionCreate
from worker.tasks.validate_submission import validate_submission_task


class SubmissionService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = SubmissionRepository(db)
        self.contract_repo = ContractRepository(db)

    def create(self, submission: SubmissionCreate) -> Submission:
        submission = self.repo.create(submission, status="pending", error=None)
        validate_submission_task.delay(submission.id)

        return submission

    def list_by_contract(self, contract_id: int) -> list[Submission]:
        return self.repo.list_by_contract(contract_id)
