import pytest
from src.models.settings.connections import db_connection_handler
from src.models.repository.attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

# @pytest.mark.skip(reason='inserte desnecessário')
def test_insert_attendee():
    event_id = "meu uuid"
    attendee_info = {
        "uuid":"meu-uuid-attendee",
        "name":"Emesson",
        "email":"emesson@gmail.com",
        "event_id": event_id
    }
    attendee = AttendeesRepository()
    response = attendee.insert_attendee(attendee_info)
    print(response)

@pytest.mark.skip(reason='...')
def test_get_attendee_badge_by_id():
    attendee_id = "meu-uuid-attendee"
    attendee_repository = AttendeesRepository()
    attendee = attendee_repository.get_attendee_badge_by_id(attendee_id)
    print(attendee)