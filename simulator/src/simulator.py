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
    for x in range(1, 6):
        msg = Message(logMessage.encode("utf-8"))
        msg.custom_properties={'deviceid':str(x),'temp':'80.8','pressure':'68.23','humidity':'50','windspeed':'12.5'}
        sb_service.send_queue_message('statistics', msg)
        notify.info("Message #" + str(x) + " posted.")
               
    # Pull messages from SB Queue and notify
    for x in range(1, 6):
        rtnmsg = sb_service.receive_queue_message('statistics', peek_lock=False, timeout=30)
        if rtnmsg is None:
            notify.info("Zero messages in Service Bus Queue")
        else:
            customvalue = str(rtnmsg.custom_properties['deviceid'])
            notify.info(customvalue)
                
if __name__ == "__main__":
    #while True:
    #    time.sleep(5)
        doSomething()