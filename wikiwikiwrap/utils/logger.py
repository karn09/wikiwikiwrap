import logging
import sys


def create_logger(location, level, format):
    """Create and configure a logger."""
    logger = logging.getLogger()

    if logger.hasHandlers():
        return logger

    if location == "stdout":
        handler = logging.StreamHandler(sys.stdout)
    else:
        handler = logging.FileHandler(location)

    handler.setLevel(level)
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
