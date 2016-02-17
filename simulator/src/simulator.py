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
import logging

def doSomething():
  summary = "Processing Status"
  print(summary)
  
if __name__ == "__main__":
    while True:
        # Delay for 10 seconds
        time.sleep(10)
        doSomething()