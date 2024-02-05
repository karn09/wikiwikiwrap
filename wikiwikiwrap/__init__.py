"""wikiwikiwrap - A simple Flask application to wrap the Wikipedia API."""

# This file is the main entry point for the application.
# It creates an instance of the Flask application and sets
# up the configuration, logging, and other important settings.

from flask import Flask
from .utils.limiter import create_limiter
from .utils.logger import create_logger
from .config import config
from .utils.cache import init_cache

__version__ = "0.1.0"


def create_app():
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__)
    app.config.from_object(config)

    # Configure logging
    create_logger(
        app.config["LOGGING_LOCATION"],
        app.config["LOGGING_LEVEL"],
        app.config["LOGGING_FORMAT"],
    )

    # Initialize the cache
    if "TESTING" not in app.config or not app.config["TESTING"]:
        init_cache(app).init_app(app)
        app.logger.info(
            f"Cache initialized with type: {app.config['CACHE_TYPE']} and location: {app.config['CACHE_REDIS_HOST']}:{app.config['CACHE_REDIS_PORT']}"
        )

    # Initialize the rate limiter
    if "TESTING" not in app.config or not app.config["TESTING"]:
        create_limiter(app)
        app.logger.info(
            f"Global Rate limiter initialized with value: {app.config['RATELIMIT_DEFAULT']}"
        )

    # Import and register the Wikipedia API blueprint
    from .api.v1 import wikipedia

    # Register the Wikipedia API blueprint
    app.register_blueprint(wikipedia.bp)

    app.logger.info("Wikipedia API blueprint registered")

    app.logger.info(f"Application created with configuration: {app.config}")
    return app
