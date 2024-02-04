import logging
import os

class Config(object):
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False

    # Production-specific logging configuration
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'stdout'
    LOGGING_LEVEL = logging.ERROR
    LIMITER_VALUE = '200 per minute'

class DevelopmentConfig(Config):
    DEBUG = True

    # Development-specific logging configuration
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'development.log'
    LOGGING_LEVEL = logging.DEBUG
    LIMITER_VALUE = '5 per minute'

class TestingConfig(Config):
    TESTING = True


config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

# Set the configuration to the value of the 'FLASK_ENV' environment variable
# Default to 'Production' if 'FLASK_ENV' is not set
flask_env = os.getenv('FLASK_ENV', 'development').lower()
config = config_dict.get(flask_env)

if config is None:
    raise ValueError(f"Invalid value for FLASK_ENV: '{flask_env}'. Valid environments are: {', '.join(config_dict.keys())}")
