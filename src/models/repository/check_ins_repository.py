from src.models.settings.connections import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from src.main.errors.errors_types.http_conflict import HttpConflictError

class CheckInsRepository:
    def insert_check_in(self, attendee_id: str) -> str:
        with db_connection_handler as database:
            try:
                check_in = CheckIns(attendeeId=attendee_id)
                # print(check_in.attendeeId)
                database.session.add(check_in)
                database.session.commit()
                return attendee_id
            except IntegrityError:
                raise HttpConflictError('Check in já feito!')
            except Exception as exception:
                database.session.rollback()
                raise exception