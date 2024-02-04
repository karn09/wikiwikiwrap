from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


# Rate limiting for the Wikipedia API
def create_limiter(app, limiter_value):
    """Create and configure a rate limiter."""

    if limiter_value is None:
        raise ValueError("Rate limiter value is not set.")

    if app is None:
        raise ValueError("Flask app is not set.")

    storage_uri = "memory://"

    if "LIMITER_STORAGE" in app.config:
        storage_uri = app.config["LIMITER_STORAGE"]

    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=[limiter_value],
        storage_uri=storage_uri,
    )
    return limiter
