from src.models.settings.base import Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from src.models.entities.events import Events

class Attendees(Base):
    __tablename__="attendees"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey('events.id'))
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"Attendees [nome={self.name}, email={self.email}, event_id={self.event_id}]"

