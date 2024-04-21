import uuid
from src.models.repository.events_repository import EventsRepository
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class EventHandler:
    def __init__(self) -> None:
        self.__event_repository = EventsRepository()

    def register(self, event_request: HttpRequest) -> HttpResponse:
        body = event_request.body
        body['uuid'] = str(uuid.uuid4())
        self.__event_repository.insert_event(body)

        return HttpResponse(
            body={"eventId":body['uuid']},
            status_code=200
        )
    
    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param['event_id']
        event = self.__event_repository.get_event_by_id(event_id)

        event_count_attendee = self.__event_repository.count_attendes(event_id)

        if not event:
            raise Exception("Evento não encontrado")
        return HttpResponse(
            body={
                "event": {
                    "id":event.id,
                    "title":event.title,
                    "detail":event.details,
                    "slug":event.slug,
                    "maximum_attendee":event.maximum_attendees,
                    "attendeeAmount":event_count_attendee["attendeesAmount"]
                }
            },
            status_code=200
        )