from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.submission import SubmissionCreate, SubmissionRead
from app.services.submission_service import SubmissionService

router = APIRouter(prefix="/submissions", tags=["Submissions"])


@router.post("/", response_model=SubmissionRead)
def submit(submission: SubmissionCreate, db: Session = Depends(get_db)):
    service = SubmissionService(db)
    try:
        return service.create(submission)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/by_contract/{contract_id}", response_model=list[SubmissionRead])
def list_subs(contract_id: int, db: Session = Depends(get_db)):
    service = SubmissionService(db)
    return service.list_by_contract(contract_id)
