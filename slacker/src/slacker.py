""" 
Runs in background and posts status to Slack Channel 
"""

import config
import notify
from log import Log
from messageQueue import Queue
from summaryTable import SummaryTable

import json
import optparse
import pickle
import time

def updateSlack():
  log = Log()
  table = SummaryTable(config.AZURE_STORAGE_ACCOUNT_NAME, config.AZURE_STORAGE_ACCOUNT_KEY, config.AZURE_STORAGE_SUMMARY_TABLE_NAME)
  queue_service = getQueueService()
  summary = "Processing Status [" + str(time.ctime()) + "]\n\n"
  summary = summary + "Queue Length is approximately: " + queue_service.getLength() + "\n"
  summary = summary + "Errors: " + str(table.getCount("ERROR")) + "\n"
  summary = summary + "Warnings: " + str(table.getCount("WARNING")) + "\n"
  summary = summary + "Infos: " + str(table.getCount("INFO")) + "\n"
  summary = summary + "Debugs: " + str(table.getCount("DEBUG")) + "\n"
  summary = summary + "Others: " + str(table.getCount("OTHER")) + "\n"
  print(summary)
  notify.info(summary)

def getQueueService():
  queue_service = Queue(account_name = config.AZURE_STORAGE_ACCOUNT_NAME, account_key=config.AZURE_STORAGE_ACCOUNT_KEY, queue_name=config.AZURE_STORAGE_QUEUE_NAME)
  return queue_service

def dumpUnprocessedLogs():
  print ("Unproccessed logs")
  try:
      with open(config.UNPROCESSED_LOG_FILE, 'r') as f:
          log = f.read()
      print (log)
  except:
      print("No logs waiting to be processed")

def dumpLogs():
  print ("Proccessed logs")
  try:
      with open(config.PROCESSED_LOG_FILE, 'r') as f:
          log = f.read()
      print (log)
  except:
      print("No logs have been processed")

def readSummary():
  try:
    with open(config.SUMMARY_LOG_FILE, 'r') as f:
      summary = json.loads(f.read())
  except FileNotFoundError:
    summary = {'ERRORS': 0, 'WARNINGS':0, 'INFOS':0}
  return summary

def deleteQueue():
  log = Log()
  getQueueService().delete_queue(config.AZURE_STORAGE_QUEUE_NAME)
  log.info("Queue deleted: " + config.AZURE_STORAGE_QUEUE_NAME)

def createQueue():
  queue_service = getQueueService()

def createTable():
  table = SummaryTable(config.AZURE_STORAGE_ACCOUNT_NAME, config.AZURE_STORAGE_ACCOUNT_KEY, config.AZURE_STORAGE_SUMMARY_TABLE_NAME)

def deleteTable():
  log = Log()
  getQueueService().delete_queue(config.AZURE_STORAGE_SUMMARY_TABLE_NAME)
  log.info("Table deleted: " + config.AZURE_STORAGE_SUMMARY_TABLE_NAME)
  
if __name__ == "__main__":
    while True:
        # Delay for 10 seconds
        time.sleep(10)
        updateSlack()
    