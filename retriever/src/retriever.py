import os
import random
import socket
import sys
import time
import traceback
import notify
from log import Log
from azure.servicebus import ServiceBusService, Message, Queue

def doLoop():
    hostname = socket.gethostname()
    logMessage = hostname + ": Processing Status @ " + str(time.ctime())
    notify.info(logMessage)
    # Write to log file
    log = Log()
    log.info(logMessage)
    sb_service = ServiceBusService(service_namespace='acslogging',shared_access_key_name='RootManageSharedAccessKey',shared_access_key_value='gnLZ2ixKkXng7rNvaCbgl9ucxsEKK7vuD5QkLl1iemM=')
        
    while True:
        sbqueue = sb_service.get_queue('statistics')
        queuelength = sbqueue.message_count
        log.info(str(queuelength))
        if queuelength<1:
            notify.info("No messages in Service Bus Queue")
        else:
            rtnmsg = sb_service.receive_queue_message('statistics', peek_lock=False, timeout=30)
            data_body = str(rtnmsg.body)
            log.info("Mesage body: " + data_body)
            data_deviceid = str(rtnmsg.custom_properties['deviceid'])
            data_temp = str(rtnmsg.custom_properties['temp'])
            data_pressure = str(rtnmsg.custom_properties['pressure'])
            data_humidity = str(rtnmsg.custom_properties['humidity'])
            data_windspeed = str(rtnmsg.custom_properties['windspeed'])
            notify.info("Temperature: " + data_temp + " >Message: " + data_body)          
                                
if __name__ == "__main__":
    doLoop()