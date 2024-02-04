"""wikiwikiwrap - A simple Flask application to wrap the Wikipedia API."""

# This file is the main entry point for the application.
# It creates an instance of the Flask application and sets
# up the configuration, logging, and other important settings.

from flask import Flask
from .api.v1 import wikipedia
from .utils.limiter import create_limiter
from .utils.logger import create_logger
from .config import config

__version__ = "0.1.0"

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize the rate limiter
    create_limiter(app, app.config['LIMITER_VALUE'])

    # Configure logging
    create_logger(app.config['LOGGING_LOCATION'], app.config['LOGGING_LEVEL'], app.config['LOGGING_FORMAT'])

    # Register the Wikipedia API blueprint
    app.register_blueprint(wikipedia.bp)

    return app