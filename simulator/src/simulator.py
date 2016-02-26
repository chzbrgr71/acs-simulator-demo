"""
Writes simulated metrics to Azure Queue
Runs continuously and does not stop 
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
    # Write to log file and update Slack
    hostname = socket.gethostname()
    logMessage = "SIMULATOR (" + hostname + "): Creating statistics starting @ " + str(time.ctime())
    log = Log()
    log.info(logMessage)
    notify.info(logMessage)
    
    # Start loop and write random messages to Azure Service Bus Queue
    x=0
    
    while True:
        x=x+1
        time.sleep(2)
        # Write message to SB Queue
        sb_service = ServiceBusService(service_namespace='acslogging',shared_access_key_name='RootManageSharedAccessKey',shared_access_key_value='gnLZ2ixKkXng7rNvaCbgl9ucxsEKK7vuD5QkLl1iemM=')
        msg_text = "Update number: " + str(x)    
        msg = Message(msg_text.encode("utf-8"))
        # Randomly create data for SB Queue
        r = random.randint(1, 10)
        if r == 1:
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'40.8','pressure':'61.93','humidity':'20','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
        elif r == 2: 
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'50.8','pressure':'62.83','humidity':'30','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
        elif r == 3: 
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'60.8','pressure':'63.73','humidity':'40','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
        elif r == 4: 
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'70.8','pressure':'64.63','humidity':'50','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
        elif r == 5: 
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'80.8','pressure':'51.93','humidity':'60','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
        elif r == 6: 
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'90.8','pressure':'55.93','humidity':'70','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
        elif r == 7: 
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'45.2','pressure':'34.99','humidity':'45','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
        elif r == 8: 
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'55.2','pressure':'38.99','humidity':'55','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
        elif r == 9:
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'65.2','pressure':'36.99','humidity':'65','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
        else:
            msg.custom_properties={'deviceid':'mydevice' + str(r),'temp':'75.2','pressure':'71.77','humidity':'38','windspeed':str(r) + '.5'}
            sb_service.send_queue_message('statistics', msg)
         
        log.info("Message #" + str(x) + " posted.")
               
if __name__ == "__main__":
    doSomething()