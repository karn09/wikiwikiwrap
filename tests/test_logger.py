import logging
import pytest
from wikiwikiwrap import create_app


@pytest.fixture
def app():
    return create_app()


def test_logger_initialization(app):
    assert hasattr(app, "logger")
    assert isinstance(app.logger, logging.Logger)


def test_logger_logs_messages(app, caplog):
    with caplog.at_level(logging.INFO):
        app.logger.info("Test message")
    assert "Test message" in caplog.text
