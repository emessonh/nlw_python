import pytest
from .events_repository import EventsRepository
from src.models.settings.connections import db_connection_handler

db_connection_handler.connect_to_db()

# @pytest.mark.skip(reason="Novo registro no banco")
def test_insert_events():
    event = {
        "uuid":"meu-uuid-2",
        "title":"meu title",
        "slug":"nossa api 2",
        "maximum_attendees": 20
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)
@pytest.mark.skip(reason="Seleção não necessária")
def test_get_event_by_id():
    event_id = "meu uuid"
    event = EventsRepository()
    response = event.get_event_by_id(event_id)
    print(response)
