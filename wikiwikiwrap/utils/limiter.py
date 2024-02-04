from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Rate limiting for the Wikipedia API
def create_limiter(app, limiter_value):
    limiter = Limiter(
        app = app,
        key_func=get_remote_address,
        default_limits=[limiter_value]
    )
    return limiter
