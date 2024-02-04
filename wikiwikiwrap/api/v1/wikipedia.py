import requests
import re
import json
import calendar
from flask import Blueprint, jsonify, Response, request

bp = Blueprint("wikipedia", __name__)

def create_error_response(message, status_code):
    """Create a JSON error response."""
    error_data = {
        "title": "Error",
        "status": status_code,
        "detail": message,
        "uri": request.path
    }
    response = Response(json.dumps(error_data), status=status_code, mimetype='application/json')
    return response

@bp.route('/views/<string:article>/<string:year>/<string:month>', methods=['GET'])
def get_views(article, year, month):
    """Get the number of views for a Wikipedia article."""

    # Sanitize inputs
    if not re.match(r'^[\w\s-]+$', article):
        return create_error_response("Invalid article name. Only alphanumeric characters are allowed.", 400)
    if not year.isdigit() or len(year) != 4:
        return create_error_response("Invalid year. Year should be a 4-digit number.", 400)
    if not month.isdigit() or len(month) != 2 or int(month) < 1 or int(month) > 12:
        return create_error_response("Invalid month. Month should be a 2-digit number between 01 and 12.", 400)

    last_day = calendar.monthrange(int(year), int(month))[1]

    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{article}/monthly/{year}{month}0100/{year}{month}{last_day}00"
    response = requests.get(url,
                            headers={'User-Agent': 'wikiwikiwrap/0.1.0',
                                     'Content-Type': 'application/json'})

    # If the request was not successful, return the error message
    if response.status_code != 200:
        err_data = response.json()
        err_data['uri'] = request.path
        return create_error_response(err_data['detail'], response.status_code)

    data = response.json()

    return jsonify(data)
