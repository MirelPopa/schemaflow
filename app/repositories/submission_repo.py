from sqlalchemy.orm import Session

from app.models.submission import Submission
from app.schemas.submission import SubmissionCreate


class SubmissionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self, submission: SubmissionCreate, status: str, error: str | None
    ) -> Submission:
        submission = Submission(
            contract_id=submission.contract_id,
            payload=submission.payload,
            status=status,
            error=error,
        )
        self.db.add(submission)
        self.db.commit()
        self.db.refresh(submission)
        return submission

    def list_by_contract(self, contract_id: int) -> list[Submission]:
        return (
            self.db.query(Submission)
            .filter(Submission.contract_id == contract_id)
            .all()
        )
