"""
This container retrieves values from Azure Service Bus Queue and writes them to DocumentDB
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
import pydocumentdb.document_client as document_client

def retrieve():
    # Write to log file and update Slack
    hostname = socket.gethostname()
    logMessage = "RETRIEVER (" + hostname + "): Pulling queue messages and writing to DB starting @ " + str(time.ctime())
    log = Log()
    log.info(logMessage)
    notify.info(logMessage)
    
    # Connect to Azure Service Bus
    sb_service = ServiceBusService(service_namespace='acslogging',shared_access_key_name='RootManageSharedAccessKey',shared_access_key_value='gnLZ2ixKkXng7rNvaCbgl9ucxsEKK7vuD5QkLl1iemM=')
        
    while True:
        sbqueue = sb_service.get_queue('statistics')
        queuelength = sbqueue.message_count
        if queuelength<1:
            log.info("Queue is empty")
        else:
            # Gather variables
            rtnmsg = sb_service.receive_queue_message('statistics', peek_lock=False, timeout=30)
            data_body = str(rtnmsg.body)
            data_deviceid = str(rtnmsg.custom_properties['deviceid'])
            data_temp = str(rtnmsg.custom_properties['temp'])
            data_pressure = str(rtnmsg.custom_properties['pressure'])
            data_humidity = str(rtnmsg.custom_properties['humidity'])
            data_windspeed = str(rtnmsg.custom_properties['windspeed'])
            data_timestamp = str(time.ctime())
            
            # Connect to Azure DocumentDB
            client = document_client.DocumentClient('https://acs1.documents.azure.com:443', {'masterKey': "N0CLphgulonYd/ZEft0ArUGLAt1lgjG/yWbQTEy/QoZzq2bJTLYPj+t+lsrDdxVNXn43i5f8HVnh4jwvrL/KzQ=="})
            db = next((data for data in client.ReadDatabases() if data['id'] == 'acs-demo'))
            collection = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == 'stats'))
            
            # Create document
            document = client.CreateDocument(collection['_self'],
                { 
                    'Device ID': data_deviceid,
                    'TimeStamp': data_timestamp,
                    'Temperature': data_temp,
                    'Pressure': data_pressure,
                    'Humidity': data_humidity,
                    'Windspeed': data_windspeed,
                    'Body': data_body
                }) 
            log.info("Added document to documentDB")
                                  
if __name__ == "__main__":
    retrieve()