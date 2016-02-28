import os
import time
from log import Log
import pydocumentdb.document_client as document_client

def doMain():
    logMessage = "DocumentDB Testing"
    log = Log()
    log.info(logMessage)
    
    client = document_client.DocumentClient(AZURE_DOCUMENTDB_URI, {'masterKey': AZURE_DOCUMENTDB_KEY})
    log.info("Connected to DocDB")
    data_body = 'device memo'
    data_deviceid = 'mydevice1'
    data_temp = '85.2'
    data_pressure = '52.9'
    data_humidity = '88'
    data_windspeed = '11.4'
    data_timestamp = str(time.ctime())

    # Connect to DB
    # db = client.CreateDatabase({ 'id': 'acs-demo' })
    db = next((data for data in client.ReadDatabases() if data['id'] == 'acs-demo'))
    log.info("Connected to DocDB database acs-demo")
    
    # Create collection
    # collection = client.CreateCollection(db['_self'],{ 'id': 'stats' }, { 'offerType': 'S1' })
    collection = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == 'stats'))
    log.info("Connected to Collection")
    
    # Create document
    document = client.CreateDocument(collection['_self'],
        { 'id': data_timestamp,
          'Device ID': data_deviceid,
          'TimeStamp': data_timestamp,
          'Temperature': data_temp,
          'Pressure': data_pressure,
          'Humidity': data_humidity,
          'Windspeed': data_windspeed,
          'Body': data_body,
          'name': data_timestamp
        }) 
    log.info("Created document")   
                             
if __name__ == "__main__":
    doMain()