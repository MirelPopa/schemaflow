from datetime import datetime
from pydantic import BaseModel
from typing import Any, Optional


class SubmissionBase(BaseModel):
    payload: dict[str, Any]


class SubmissionCreate(SubmissionBase):
    contract_id: int


class SubmissionRead(SubmissionBase):
    id: int
    status: str
    error: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
