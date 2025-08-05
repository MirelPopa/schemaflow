from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Any
from jsonschema import Draft7Validator, SchemaError


class ContractBase(BaseModel):
    name: str
    json_schema: dict[str, Any]

    @classmethod
    @field_validator("json_schema")
    def validate_json_schema(cls, schema: dict[str, Any]) -> dict[str, Any]:
        try:
            Draft7Validator.check_schema(schema)
        except SchemaError as e:
            raise ValueError(f"Invalid JSON Schema: {e.message}")
        return schema



class ContractCreate(ContractBase):
    team_id: int


class ContractRead(ContractBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
