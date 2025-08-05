from sqlalchemy import Column, Integer, String, JSON, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.base import Base


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    json_schema = Column(JSON, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    team = relationship("Team", backref="contracts")
