from typing import Dict
from src.models.settings.connections import db_connection_handler
from src.models.entities.events import Events

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
            events = Events(
                id=eventsInfo.get('uuid'),
                title=eventsInfo.get('title'),
                details=eventsInfo.get('details'),
                slug=eventsInfo.get('slug'),
                maximum_attendees=eventsInfo.get('maximum_attendees'),
            )
            database.session.add(events)
            database.session.commit()

            return eventsInfo