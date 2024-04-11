from src.models.settings.base import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey

class CheckIns(Base):
    __tablename__='check_ins'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendeeId = (String, ForeignKey("attendees.id"))

    def __repr__(self):
        return f"Check-ins [AttendeeId={self.attendeeId}]"