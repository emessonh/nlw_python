from flask import Blueprint, request, jsonify
from src.main.http_types.http_request import HttpRequest
from src.main.data.attendees_handler import AttendeeHandler

attendee_route_bp = Blueprint("attendees_route", __name__)

@attendee_route_bp.route("/attendees/<event_id>/register", methods=["POST"])
def create_register(event_id):
    attendee_handle = AttendeeHandler()
    http_request = HttpRequest(param={"event_id":event_id}, body=request.json)
    http_response = attendee_handle.registry(http_request)

    return jsonify(http_response.body), http_response.status_code

@attendee_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendees_badge(attendee_id):
    attendee_handle = AttendeeHandler()
    http_request = HttpRequest(param={"attendee_id":attendee_id})
    http_response = attendee_handle.find_badge_id(http_request)

    return jsonify(http_response.body), http_response.status_code

@attendee_route_bp.route("/events/<event_id>/attendees", methods=["GET"])
def get_attendees(event_id):
    attendee_handler = AttendeeHandler()
    http_request = HttpRequest(param={'event_id':event_id})
    http_response = attendee_handler.find_attendees_from_event(http_request)

    return jsonify(http_response.body), http_response.status_code