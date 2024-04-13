import uuid
from src.models.repository.events_repository import EventsRepository
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class EventHandler:
    def __init__(self) -> None:
        self.__event_repository = EventsRepository()

    def register(self, event_request: HttpRequest) -> HttpResponse:
        body = event_request.body
        body['uuid'] = str(uuid.uuid4)
        self.__event_repository.insert_event(body)

        return HttpResponse(
            body={"eventId":body['uuid']},
            status_code=200
        )