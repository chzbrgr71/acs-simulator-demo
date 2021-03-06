Set of containers that allow for easy simulation of load on Azure Container Service. Code primarily in Python. 

NOTE: Thanks to @rgardler for inspiration and initial source code. 

## Containers and their function

  * simulator: creates random logging activity and writes it to an Azure Service Bus Queue
  * retriever: picks up messages from Azure SB queue and writes to Azure DocumentDB
  * slacker: sends messages to Slack Channel for monitoring of demo
  * Note: Each container based on a "base" container with Azure Python libraries loaded: In [Docker Hub](https://hub.docker.com/r/chzbrgr71/acs-demo-base) 

## How to setup
 
  * Create an Azure Service Bus Queue, Azure documentDB, and Slack Channel.
    * Service Bus namespace is called "acslogging" and the queue is called "statistics"
    * DocumentDB database is "acs-demo" and the collection is called "stats" 
  * When running containers, you must update the below environment variables
  * To save time, you can pull the containers from Docker Hub or build in advance 
  * Added config for Marathon and Docker bundles
  ```
  docker pull chzbrgr71/acs-demo-simulator:2
  docker pull chzbrgr71/acs-demo-retriever:2
  docker pull chzbrgr71/acs-demo-slacker:2
  ```
  
  * To build from source (or run `setup.sh`):
  
  ```
  docker build -t chzbrgr71/acs-demo-simulator:2 simulator
  docker build -t chzbrgr71/acs-demo-retriever:2 retriever
  docker build -t chzbrgr71/acs-demo-slacker:2 slacker
  ```
  
  * Run docker-compose. With 4 simulators and 1 retriever, the queue should increase. 
  
  ```
  docker-compose up -d
  docker-compose scale simulator=4
  docker-compose scale retriever=1
  
  docker-compose stop
  ```
  
  * Environment variables (set in `docker run` or `docker-compose.yml`):
    * AZURE_SB_SERVICE_NAMESPACE
    * AZURE_SB_SHARED_ACCESS_KEY_NAME
    * AZURE_SB_SHARED_ACCESS_KEY
    * AZURE_DOCUMENTDB_URI
    * AZURE_DOCUMENTDB_KEY
    * SLACK_CHANNEL
  
## Running the demo

  * Use `docker-compose scale` to increase/decrease each container and monitor queue length.
  * With Slack open, the slacker container will provide status of the queue every few seconds.
  * Azure DocumentDB will contain documents with simulated statistics recorded.

## Running in Azure Container Service

  * Setup Azure Container Service as described [here](https://azure.microsoft.com/en-us/documentation/articles/container-service-deployment)
    * For a Swarm cluster, the operation is the same as above. Direct docker commands to Swarm Master
    * For Mesos, use the `acs-simulator-demo.json` file and update the environment variables
    * Once your SSH tunnel for port 80 has been created, run the containers with the following command:
  
      ```
      curl -X POST http://localhost/marathon/v2/groups -d @acs-simulator-demo.json -H "Content-type: application/json"
      ```
