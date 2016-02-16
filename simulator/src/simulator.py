# Runs continuously while container is in use. Writes simulated metrics to Azure Queue 

import os
import random
import socket
import sys
import time
import traceback
import notify
from messageQueue import Queue

# Config (pull these values from Docker env variables later)
AZURE_STORAGE_ACCOUNT_NAME='briardockerstorage'
AZURE_STORAGE_ACCOUNT_KEY='y3KzKM9Dql9hTJXZPBkW+VqQX88OKjKQPREbABljGJepjDYifxn8cJG5SzKmoyVQ8QnTFRfR+a6rd7eJ3iwdCw=='
AZURE_STORAGE_QUEUE_NAME='testlogqueue'
SIMULATION_DELAY=15
# SIMULATION_DELAY=os.getenv('SIMULATION_DELAY', 15)

def simulate():
  hostname = socket.gethostname()
  msgQueue = Queue(account_name = AZURE_STORAGE_ACCOUNT_NAME, account_key=AZURE_STORAGE_ACCOUNT_KEY, queue_name=AZURE_STORAGE_QUEUE_NAME)

  msg = hostname + ': Simulating until stopped'
  msg = 'Simulator: ' + hostname + ' running until stopped.'
  echo msg
  # notify.info(msg)

  _actions = 1
  while True:
    data = 'Writing message #' + str(_actions) + ' to Queue.'
    msgQueue.enqueue(data)
    _actions = _actions + 1
    msgQueue.close()

    time.sleep(int(SIMULATION_DELAY))

if __name__ == "__main__":
    try:
      simulate()
    except:
      e = sys.exc_info()[0]
      hostname = socket.gethostname()
      # notify.error(hostname + ": ACS Logging simulation failed")
