
from django.conf import settings
import redis
import json
import logging

class CacheService:
    """Common cache service."""
    def __init__(self, db_instance=0) -> None:
        self.redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, 
                                  db=db_instance)
    def getKey(self, key):
        value = self.redis_instance.get(key)
        if value is not None:
            logging.info(f"===Key: {key}, retrieved.===")
            return json.loads(value)
        else:
            logging.info(f"===No value found for key: {key}===")
            return 0
    def setKey(self, key, value):
        self.redis_instance.set(key, json.dumps(value))
        logging.info(f"===Key: {key}, updated with {value}.===")
    def deleteKey(self, key):
        self.redis_instance.delete(key)
        logging.info(f"===Key: {key}, deleted.===")


