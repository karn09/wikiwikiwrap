import pytest
from flask import Flask
from flask_limiter import Limiter
from wikiwikiwrap.utils.limiter import create_limiter


def test_create_limiter():
    app = Flask(__name__)
    app.config["LIMITER_STORAGE"] = "memory://"
    app.config["RATELIMIT_DEFAULT"] = "100 per day"
    app.config["STORAGE_URI"] = "memory://"
    limiter = create_limiter(app)
    assert isinstance(limiter, Limiter)


def test_create_limiter_no_app():
    with pytest.raises(ValueError) as exc_info:
        create_limiter(None)
    assert str(exc_info.value) == "Flask app is not set."


def test_create_limiter_no_limiter_value():
    app = Flask(__name__)
    app.config["RATELIMIT_DEFAULT"] = None
    app.config["STORAGE_URI"] = "memory://"
    with pytest.raises(ValueError) as exc_info:
        create_limiter(app)
    assert str(exc_info.value) == "Rate limiter value is not set."
