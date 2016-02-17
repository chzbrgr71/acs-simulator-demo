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
from messageQueue import Queue

def simulate():
  msgQueue = Queue(account_name = 'briardockerstorage', account_key='y3KzKM9Dql9hTJXZPBkW+VqQX88OKjKQPREbABljGJepjDYifxn8cJG5SzKmoyVQ8QnTFRfR+a6rd7eJ3iwdCw==', queue_name='briaracsqueue')
  _actions = 1
  while True:
    data = 'Writing message #' + str(_actions) + ' to Queue.'
    str(data)
    # notify.info(data)
    msgQueue.enqueue(data)
    _actions = _actions + 1
    msgQueue.close()

if __name__ == "__main__":
      str('Starting simulate loop code')
      hostname = socket.gethostname()
      msg = 'Simulator: ' + hostname + ' running until stopped.'
      str(msg)
      # notify.info(msg)
      while True:
        simulate()
        time.sleep(15)