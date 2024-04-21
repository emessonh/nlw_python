import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.main.errors.errors_types.http_not_found import HttpNotFoundError
from src.main.errors.errors_types.http_conflict import HttpConflictError

class AttendeeHandler:
    def __init__(self) -> None:
        self.__attendee_repository = AttendeesRepository()
        self.__event_repository = EventsRepository()

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.param['event_id']
        event_count_attendees = self.__event_repository.count_attendes(event_id)

        if (
            event_count_attendees["attendeesAmount"]
            and event_count_attendees['maximumAttendees'] < event_count_attendees["attendeesAmount"]
        ):raise HttpConflictError("Evento lotado")

        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendee_repository.insert_attendee(body)

        return HttpResponse(body=None, status_code=201)
    
    def find_badge_id(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param["attendee_id"]
        badge = self.__attendee_repository.get_attendee_badge_by_id(attendee_id)
        if not badge:
            raise HttpNotFoundError("Participante não encontrado")
        
        return HttpResponse(
            body={
                "badge":{
                    "name":badge.name,
                    "title":badge.title,
                    "email":badge.email
                }
            },
            status_code=200
        )
    
    def find_attendees_from_event(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        attendees = self.__attendee_repository.get_attendees_by_event_id(event_id)
        format_attendees = []
        if not attendees:
            raise HttpNotFoundError("Participantes não encontrados")
        for attendee in attendees:
            format_attendees.append(
                {
                    "id":attendee.id,
                    "name":attendee.name,
                    "email":attendee.email,
                    "checkedInAt":attendee.checkedInAt,
                    "createdAt":attendee.createdAt
                }
            )

        return HttpResponse(
            body={"attendees":format_attendees},
            status_code=200
        )