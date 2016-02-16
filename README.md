Set of containers that allow for easy simulation of load on Azure Container Service. Code primarily in Python. 

NOTE: Thanks to @rgardler for inspiration and initial source code. 

## Containers and their function

  * simulator: creates random logging activity and writes it to an Azure Queue
  * retriever: picks up messages from Azure Queue and writes to Azure DocumentDB, log files, etc.
  * slacker: sends messages to Slack Channel for monitoring of demo
  * web_app: TBD. Azure Web App to view summary results from DocumentDB

## Python SDK
  * http://azure-sdk-for-python.readthedocs.org/en/latest/index.html 
  * https://azure.microsoft.com/en-us/documentation/articles/documentdb-python-application 

## How to setup
 
  TBD

## Running the demo

  TBD
