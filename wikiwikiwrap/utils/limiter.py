from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import jsonify, make_response


def ratelimit_handler(_request_limit):
    return make_response(jsonify(error="ratelimit exceeded"), 429)


# Rate limiting for the Wikipedia API
def create_limiter(app):
    """Create and configure a rate limiter."""

    if app is None:
        raise ValueError("Flask app is not set.")

    if "RATELIMIT_DEFAULT" not in app.config or not app.config["RATELIMIT_DEFAULT"]:
        raise ValueError("Rate limiter value is not set.")

    if "STORAGE_URI" not in app.config or not app.config["STORAGE_URI"]:
        raise ValueError("Storage URI for the rate limiter is not set.")

    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=[app.config["RATELIMIT_DEFAULT"]],
        storage_uri=app.config["STORAGE_URI"],
        on_breach=ratelimit_handler,
    )

    return limiter
