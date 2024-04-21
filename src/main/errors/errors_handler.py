from src.main.http_types.http_response import HttpResponse
from src.main.errors.errors_types.http_conflict import HttpConflictError
from src.main.errors.errors_types.http_not_found import HttpNotFoundError

def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpConflictError)):
        return HttpResponse(
            body={
                "errors":[{
                    "title":error.name,
                    "details":error.message
                }]
            },
            status_code=error.status_code
        )
    
    return HttpResponse(
        body={
            "errors":[{
                "title":"erro",
                "details":str(error)
            }]
        }
    )