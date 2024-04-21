from flask import Blueprint, jsonify
from src.main.data.check_in_handler import CheckInHandler
from src.main.http_types.http_request import HttpRequest
# from src.main.http_types.http_response import HttpResponse
from src.main.errors.errors_handler import handler_errors

check_in_bp = Blueprint("check_in_routes", __name__)

@check_in_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def create_check_in(attendee_id):
    try:
        check_in_handler = CheckInHandler()
        http_request = HttpRequest(param={"attendee_id":attendee_id})
        http_response = check_in_handler.registry(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code
