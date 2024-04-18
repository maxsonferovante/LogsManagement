from redis import Redis
from models.entities.logs import Logs


from datetime import datetime

class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn


    def insert(self, key: dict, log: Logs) -> None:        
        value = {
            "log": log.get("log"),
            "tag": log.get("tag"),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.__redis_conn.set(key.get("name"), str(value))

    def get(self, key: str) -> any:
        value = self.__redis_conn.get(key)
        if value:
            return eval(value.decode('utf-8'))

    def insert_hash(self, key: dict, field: str, log: Logs) -> None:
        
        value = str({
            "log": log.get("log"),
            "tag": log.get("tag"),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
       
        self.__redis_conn.hset(key.get("name"),
                               field, 
                               value)

    def get_hash(self, key: str, field: str) -> any:
        value = self.__redis_conn.hget(key, field)
        if value:
            return value.decode("utf-8")

    def get_hash_all(self):       
        keys = self.__redis_conn.keys()
        logs = []
        for key in keys:
            log = self.__redis_conn.hgetall(key)
            self.__redis_conn.delete(key)
            logs.append(log)
        return logs
    def insert_ex(self, key: str, value: any, ex: int) -> None:
        self.__redis_conn.set(key, value, ex=ex)

    def insert_hash_ex(self, key: str, field: str, value: any, ex: int) -> None:
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, ex)