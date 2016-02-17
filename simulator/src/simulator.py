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

if __name__ == "__main__":
    logger = logging.getLogger('scope.name')
    file_log_handler = logging.FileHandler('logfile.log')
    logger.addHandler(file_log_handler)

    stderr_log_handler = logging.StreamHandler()
    logger.addHandler(stderr_log_handler)

    # nice output format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_log_handler.setFormatter(formatter)
    stderr_log_handler.setFormatter(formatter)
    logger.info('Starting simulate loop code')
    #logger.error('Error message')
    
    hostname = socket.gethostname()
    msg = 'Simulator: ' + hostname + ' running until stopped.'
    logger.info(msg)