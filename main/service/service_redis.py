from models.settings.redis.redis_connection import redis_connection_handle
from models.settings.connection import db_connection_handler, insert
from models.entities.logs import Logs
from models.repository.redis_repository import RedisRepository

from datetime import datetime

import time
import threading

TIMESLEEP = 10
class RedisService:    
    def __init__(self, redis_repository):
        self.redis_repository = redis_repository        
        
    def run(self):
        thread = threading.Thread(target=self.transfer_redis_to_database)        
        thread.start()
        
            
        
    def transfer_redis_to_database(self,):
        while True:
            print(f"Running Redis Service - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")        
            
            logs = self.redis_repository.get_all()    
            
            if logs:
                with db_connection_handler as database:
                    print(f"Transfering log to database {logs.__len__()} logs found in Redis")                  
                    for log in logs:
                        database.session.add(Logs(
                            log=log["log"],
                            tag=log["tag"]
                        ))      
                    database.session.commit()
                            
                self.redis_repository.delete_hash_all()
            else:
                print("No log found")
            
            print(f"Redis Service finished - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")        
            
            time.sleep(TIMESLEEP)    
            
                
                    
        
redis_service = RedisService(
    RedisRepository(
        redis_connection_handle.connect()
        )
    )


    
    