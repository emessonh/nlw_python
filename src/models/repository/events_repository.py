from typing import Dict
from src.models.settings.connections import db_connection_handler
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import IntegrityError, NoResultFound

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
            try:
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
            except IntegrityError:
                raise Exception('Evento já cadastrado')
            except Exception as exception:
                database.session.rollback()
                raise exception
        
    def get_event_by_id(self, event_id: str) -> Events:
        with db_connection_handler as database:
            try:
                event = (
                    database.session
                    .query(Events)
                    .filter(Events.id==event_id)
                    .one()
                )
                return event
            except NoResultFound:
                return None
            
    def count_attendes(self, event_id: str) -> Dict:
        with db_connection_handler as database:
            event = (
                database.session
                    .query(Events)
                    .join(Attendees, Attendees.event_id == Events.id)
                    .filter(Events.id == event_id)
                    .with_entities(
                        Events.maximum_attendees,
                        Attendees.id
                    )
                    .all()
            )
            if not len(event):
                return {
                    "maximumAttendees":0,
                    "attendeesAmount":0
                }
            
            return {
                "maximumAttendees":event[0].maximum_attendees,
                "attendeesAmount":len(event),
            }