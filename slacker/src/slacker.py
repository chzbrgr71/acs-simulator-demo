""" 
Runs in background and posts status to Slack Channel 
"""

import os
import socket
import notify
from log import Log
import time
from azure.servicebus import ServiceBusService, Message, Queue
import pydocumentdb.document_client as document_client

def updateSlack():
    hostname = socket.gethostname()
    logMessage = "SLACKER (" + hostname + "): Checking queue size and posting to Slack starting @ " + str(time.ctime())
    log = Log()
    log.info(logMessage)
    notify.info(logMessage)  
    
    # Gather environment variables
    AZURE_SB_SERVICE_NAMESPACE = os.getenv('AZURE_SB_SERVICE_NAMESPACE')
    AZURE_SB_SHARED_ACCESS_KEY_NAME = os.getenv('AZURE_SB_SHARED_ACCESS_KEY_NAME')
    AZURE_SB_SHARED_ACCESS_KEY = os.getenv('AZURE_SB_SHARED_ACCESS_KEY')
    
    # Connect to Azure Service Bus
    sb_service = ServiceBusService(service_namespace=AZURE_SB_SERVICE_NAMESPACE,shared_access_key_name=AZURE_SB_SHARED_ACCESS_KEY_NAME,shared_access_key_value=AZURE_SB_SHARED_ACCESS_KEY)
        
    while True:
        # Delay for 6 seconds
        time.sleep(6)
        sbqueue = sb_service.get_queue('statistics')
        queuelength = sbqueue.message_count 
        logMessage = "SLACKER: Queue length is approximately: " + str(queuelength)
        log.info(logMessage)
        notify.info(logMessage)  
    
if __name__ == "__main__":
    updateSlack()
    