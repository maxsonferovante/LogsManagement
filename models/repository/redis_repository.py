from redis import Redis
from models.entities.logs import Logs


from datetime import datetime

class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn


    def insert(self, key: dict, log: Logs) -> None:        
        key_value = key.get("name") + "_" + datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
        
        value = {
            "log": log.get("log"),
            "tag": log.get("tag")
        }
        
        response = self.__redis_conn.set(key_value, str(value))
        
        return key_value if response else None

    def get(self, key: str) -> any:
        value = self.__redis_conn.get(key)
        if value:
            return eval(value.decode('utf-8'))

    def get_all(self) -> any:
        keys = self.__redis_conn.keys(
            order_by="created_at",
        )
        if not keys:
            return []
        logs = []
        for key in keys:
            value = self.__redis_conn.get(key)
            if value:
                logs.append(eval(value.decode("utf-8")))
            
        return logs
    
    def insert_hash(self, key: dict, log: Logs) -> str:
        key_value = key.get("name") + "_" + datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
        
        field = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        value = str({
            "log": log.get("log"),
            "tag": log.get("tag")
        })
        
        response = self.__redis_conn.hset(key_value,
                               field, 
                               value)
        
        return key_value if response else None
        
    def get_hash(self, key: str, field: str) -> any:
        value = self.__redis_conn.hget(key, field)
        if value:
            return value.decode("utf-8")

    def get_hash_all(self):       
        keys = self.__redis_conn.keys()
        logs = []
        for key in keys:
            log = self.__redis_conn.hgetall(key)
            
            key, value = list(log.items())[0]
            
            logs.append({key.decode("utf-8"): eval(value.decode("utf-8"))})
            
            # self.__redis_conn.delete(key)                        
            
        return logs
    
    def delete_hash_all(self):
        for key in self.__redis_conn.keys():
            self.__redis_conn.delete(key)
                    
    def insert_ex(self, key: str, value: any, ex: int) -> None:
        self.__redis_conn.set(key, value, ex=ex)

    def insert_hash_ex(self, key: str, field: str, value: any, ex: int) -> None:
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, ex)