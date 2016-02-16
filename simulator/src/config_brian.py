import os

UNPROCESSED_LOG_FILE='/logs/queue.log'
PROCESSED_LOG_FILE='/logs/archive.log'
SUMMARY_LOG_FILE='/logs/summary.log'

SLACK_WEBHOOK='https://hooks.slack.com/services/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'

SMTP_SERVER='mail.mail.com'
SMTP_PORT='25'
SMTP_USERNAME='azureuser'
SMTP_PASSWORD='password'
MAIL_FROM='brian.redmond@live.com'
MAIL_TO='brian.redmond@outlook.com'

# Queue details
ACS_LOGGING_QUEUE_TYPE=os.getenv('ACS_LOGGING_QUEUE_TYPE', 'AzureStorageQueue')

# Azure Storage Account deatils
AZURE_STORAGE_ACCOUNT_NAME='briardockerstorage'
AZURE_STORAGE_ACCOUNT_KEY='y3KzKM9Dql9hTJXZPBkW+VqQX88OKjKQPREbABljGJepjDYifxn8cJG5SzKmoyVQ8QnTFRfR+a6rd7eJ3iwdCw=='

# Queue Details
AZURE_STORAGE_QUEUE_NAME='testlogqueue'
AZURE_STORAGE_SUMMARY_TABLE_NAME='testlogsummary'


# number of simulation events to create on each run (0 means conmtinue until stopped)
SIMULATION_ACTIONS=os.getenv('SIMULATION_ACTIONS', 5)
# number of seconds to delay between each logging event
SIMULATION_DELAY=os.getenv('SIMULATION_DELAY', 30)
