import logging
import os
import warnings

config_dict = {
    "development": "wikiwikiwrap.config.DevelopmentConfig",
    "production": "wikiwikiwrap.config.ProductionConfig",
    "testing": "wikiwikiwrap.config.TestingConfig",
}

# Set the configuration to the value of the 'FLASK_ENV' environment variable
# Default to 'development' if 'FLASK_ENV' is not set
flask_env = os.getenv("FLASK_ENV", "development").lower()
config = config_dict.get(flask_env)

if config is None:
    raise ValueError(
        f"Invalid value for FLASK_ENV: '{flask_env}'. Valid environments are: {', '.join(config_dict.keys())}"
    )


def get_env_variable_or_default(env_var_name, default_value):
    """Get the value of an environment variable or return a default value."""
    value = os.getenv(env_var_name, default_value)
    if value == default_value and flask_env == "production":
        warnings.warn(
            f"Environment variable '{env_var_name}' not set. Using default value: '{default_value}'"
        )
    return value


class Config(object):
    DEBUG = False
    TESTING = False
    LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOGGING_LOCATION = "stdout"
    LOGGING_LEVEL = logging.DEBUG
    STORAGE_URI = "memory://"
    RATELIMIT_DEFAULT = "200 per minute"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False

    LOGGING_LEVEL = get_env_variable_or_default("LOGGING_LEVEL", logging.ERROR)

    # Rate limiter configuration
    RATELIMIT_DEFAULT = get_env_variable_or_default(
        "RATELIMIT_DEFAULT", "200 per minute"
    )

    # Storage URI for the rate limiter
    STORAGE_URI = get_env_variable_or_default("STORAGE_URI", "memory://")
