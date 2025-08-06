from celery import shared_task
from jsonschema import ValidationError, validate
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.contract import Contract
from app.models.submission import Submission


@shared_task
def validate_submission_task(submission_id: int):
    db: Session = SessionLocal()

    submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not submission:
        print(f"[ERROR] Submission {submission_id} not found.")
        db.close()
        return

    contract = db.query(Contract).filter(Contract.id == submission.contract_id).first()
    if not contract:
        print(f"[ERROR] Contract {submission.contract_id} not found.")
        db.close()
        return

    try:
        validate(instance=submission.payload, schema=contract.json_schema)
        submission.status = "valid"
        submission.error = None
    except ValidationError as ve:
        submission.status = "invalid"
        submission.error = str(ve)

    db.commit()
    db.close()
