from django.conf import settings
import redis
import json
import logging

class CacheService:
    def __init__(self, db_instance=0) -> None:
        self.redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, 
                                  db=db_instance)
    def getKey(self, key):
        self.redis_instance.get(key)
        logging.info(f"Key: {key}, retrieved.")
    def setKey(self, key, value):
        self.redis_instance.set(key, value)
        logging.info(f"Key: {key}, updated with {value}.")
    def deleteKey(self, key):
        self.redis_instance.delete(key)
        logging.info(f"Key: {key}, deleted.")


