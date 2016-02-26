""" 
Runs in background and posts status to Slack Channel 
"""

import os
import socket
import notify
from log import Log
import time

def updateSlack():
    hostname = socket.gethostname()
    logMessage = "SLACKER (" + hostname + "): Checking queue size and posting to Slack starting @ " + str(time.ctime())
    log = Log()
    log.info(logMessage)
    notify.info(logMessage)  
  
    # Connect to Azure Service Bus
    sb_service = ServiceBusService(service_namespace='acslogging',shared_access_key_name='RootManageSharedAccessKey',shared_access_key_value='gnLZ2ixKkXng7rNvaCbgl9ucxsEKK7vuD5QkLl1iemM=')
    sbqueue = sb_service.get_queue('statistics')
    queuelength = sbqueue.message_count 
    logMessage = "SLACKER: Queue length is approximately: " + str(queuelength)
    log.info(logMessage)
    notify.info(logMessage)  
    
if __name__ == "__main__":
    while True:
        # Delay for 7 seconds
        time.sleep(7)
        updateSlack()
    