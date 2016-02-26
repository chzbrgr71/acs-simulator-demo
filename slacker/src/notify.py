'''
Helper class for working with Slack webhooks.
'''

import json
import requests

def send(msg, channel="general"):
    payload = {
        "channel": "#" + channel,
        "text": msg
    }
    requests.post('https://hooks.slack.com/services/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', json.dumps(payload))

def info(msg):
    #send(msg, 'info')
    send(msg)
    
def error(msg):
    #send(msg, 'error')
    send(msg)

if __name__ == "__main__":
    send("Test message from ACS Logging Test Slack Bot")


