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

def doLoop():
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
            notify.info("No messages in Service Bus Queue")
            log.info("No messages in Service Bus Queue")
        else:
            # Gather variables
            rtnmsg = sb_service.receive_queue_message('statistics', peek_lock=False, timeout=30)
            data_body = str(rtnmsg.body)
            data_deviceid = str(rtnmsg.custom_properties['deviceid'])
            data_temp = str(rtnmsg.custom_properties['temp'])
            data_pressure = str(rtnmsg.custom_properties['pressure'])
            data_humidity = str(rtnmsg.custom_properties['humidity'])
            data_windspeed = str(rtnmsg.custom_properties['windspeed'])
            log.info("Debug Info: Temperature: " + data_temp + " > Message: " + data_body)
            # Write to Azure DocumentDB
            client = document_client.DocumentClient('https://acs1.documents.azure.com:443/', {'masterKey': "N0CLphgulonYd/ZEft0ArUGLAt1lgjG/yWbQTEy/QoZzq2bJTLYPj+t+lsrDdxVNXn43i5f8HVnh4jwvrL/KzQ=="})
            # Attempt to delete the database.  This allows this to be used to recreate as well as create
            try:
                db = next((data for data in client.ReadDatabases() if data['id'] == 'acs-simulator-demo'))
                client.DeleteDatabase(db['_self'])
            except:
                pass

            # Create database
            db = client.CreateDatabase({ 'id': 'acs-simulator-demo' })

            # Create collection
            collection = client.CreateCollection(db['_self'],{ 'id': 'statistics' }, { 'offerType': 'S1' })

            # Create document
            document = client.CreateDocument('statistics',
                { 'id': 'device-measurements',
                'Body': data_body,
                'Device ID': data_deviceid,
                'Temperature': data_temp,
                'Pressure': data_pressure,
                'Humidity': data_humidity,
                'Windspeed': data_windspeed,
                'name': 'device-measurements' 
                })                    
if __name__ == "__main__":
    doLoop()