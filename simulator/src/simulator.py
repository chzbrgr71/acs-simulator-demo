"""
Runs continuously while container is in use. Writes simulated metrics to Azure Queue 
# Config (pull these values from Docker env variables later)
AZURE_STORAGE_ACCOUNT_NAME='briardockerstorage'
AZURE_STORAGE_ACCOUNT_KEY='y3KzKM9Dql9hTJXZPBkW+VqQX88OKjKQPREbABljGJepjDYifxn8cJG5SzKmoyVQ8QnTFRfR+a6rd7eJ3iwdCw=='
AZURE_STORAGE_QUEUE_NAME='briaracsqueue'
SIMULATION_DELAY=15
"""

import os
import random
import socket
import sys
import time
import traceback
import notify
from log import Log
from azure.servicebus import ServiceBusService, Message, Queue

def doSomething():
    hostname = socket.gethostname()
    logMessage = hostname + ": Processing Status @ " + str(time.ctime())
    notify.info(logMessage)
    # Write to log file
    log = Log()
    log.info(logMessage)
    # Write message to SB Queue
    sb_service = ServiceBusService(service_namespace='acslogging',shared_access_key_name='RootManageSharedAccessKey',shared_access_key_value='gnLZ2ixKkXng7rNvaCbgl9ucxsEKK7vuD5QkLl1iemM=')
    msg = Message(logMessage.encode("utf-8"))
    msg.custom_properties={'deviceID':'29299292','temp':'80.8','pressure':'68.23','humidity':'50','windspeed':'12.5'}
    msg.Label = hostname
    sb_service.send_queue_message('statistics', msg)
  
if __name__ == "__main__":
    while True:
        time.sleep(5)
        doSomething()