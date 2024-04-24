import requests
import random
import time
from datetime import datetime

def get_random_tag():
    list_tag = ["INFO", "ERROR", "WARNING", "DEBUG"]
    return list_tag[random.randint(0, 3)]

def get_random_log():
    list_log = ['Log 1', 'Log 2', 'Log 3', 'Log 4']
    return list_log[random.randint(0, 3)] + " - " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_seed():
    response = requests.post(
        'http://127.0.0.1:8000/logs?name=app',
        json={
            "tag": get_random_tag(),
            "log": get_random_log()
        }
    )
    print (response.json())
    
while True:
    get_seed()
    time.sleep(2)

    
