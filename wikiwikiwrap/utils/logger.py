import logging

def create_logger(location, level, format):
    """Create and configure a logger."""
    logger = logging.getLogger('wikiwikiwrap')

    if location == 'stdout':
        handler = logging.StreamHandler(location)
    else:
        handler = logging.FileHandler(location)

    handler.setLevel(level)
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
