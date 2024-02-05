from flask_caching import Cache

cache = None


def init_cache(app):
    global cache
    cache = Cache(
        config={
            "CACHE_TYPE": app.config["CACHE_TYPE"],
            "CACHE_REDIS_HOST": app.config["CACHE_REDIS_HOST"],
            "CACHE_REDIS_PORT": app.config["CACHE_REDIS_PORT"],
            "CACHE_REDIS_DB": app.config["CACHE_REDIS_DB"],
            "CACHE_REDIS_URL": app.config["CACHE_REDIS_URL"],
        },
    )
    return cache
