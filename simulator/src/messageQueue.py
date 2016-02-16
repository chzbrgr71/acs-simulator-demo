""" Manage the queue for the log messages """

from azure.storage.queue import QueueService
import os

# Config (pull these values from Docker env variables later)
AZURE_STORAGE_ACCOUNT_NAME='briardockerstorage'
AZURE_STORAGE_ACCOUNT_KEY='y3KzKM9Dql9hTJXZPBkW+VqQX88OKjKQPREbABljGJepjDYifxn8cJG5SzKmoyVQ8QnTFRfR+a6rd7eJ3iwdCw=='
AZURE_STORAGE_QUEUE_NAME='testlogqueue'

class Queue:
    def __init__(self, account_name, account_key, queue_name):
        # Initialiaze Azure storage queue.
        self.queue_name = queue_name
        self.createAzureQueues(account_name, account_key)

    def createAzureQueues(self, account_name, account_key):
        # Create a queue for unprocessed log messages
        self.queue_service = QueueService(account_name, account_key)
        self.queue_service.create_queue(self.queue_name)

    def close(self):
        # Perform any necessary cleanup on the queue
        pass
        
    def enqueue(self, msg, level = "INFO"):
        msg = level + " - " + msg
        self.queue_service.put_message(self.queue_name, msg)
        
    def dequeue(self):
        messages = []
        messages = self.queue_service.get_messages(self.queue_name)
        return messages

    def delete(self, message):
        self.queue_service.delete_message(self.queue_name, message.message_id, message.pop_receipt)

    def delete_queue(self, queue_name):
        self.queue_service.delete_queue(queue_name, False)

    def getLength(self):
        # Get the approximate length of the queue
        queue_metadata = self.queue_service.get_queue_metadata(self.queue_name)
        count = queue_metadata['x-ms-approximate-messages-count']
        return count
