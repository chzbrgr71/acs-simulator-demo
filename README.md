Set of containers that allow for easy simulation of load on Azure Container Service. Code primarily in Python. 

NOTE: Thanks to @rgardler for inspiration and initial source code. 

## Containers and their function

  * simulator: creates random logging activity and writes it to an Azure Service Bus Queue
  * retriever: picks up messages from Azure SB queue and writes to Azure DocumentDB
  * slacker: sends messages to Slack Channel for monitoring of demo
  * web_app: TBD. Azure Web App to view summary results from DocumentDB
  * Note: Each container based on a "base" container with Azure Python libraries loaded: In [Docker Hub](https://hub.docker.com/r/chzbrgr71/acs-simulator-demo) 

## How to setup
 
  * Create an Azure Service Bus Queue, Azure documentDB, and Slack Channel.
  * Pull base container from Docker Hub: 
  ```
  docker pull chzbrgr71/acs-simulator-demo:base
  ```
  * Build the 3 containers (simulator, retriever, slacker). 
  ```
  docker build -t chzbrgr71/acs-simulator simulator
  docker build -t chzbrgr71/acs-retriever retriever
  docker build -t chzbrgr71/acs-slacker slacker 
  ```
  * Run docker-compose. With 4 simulators and 1 retriever, the queue should increase.
  ```
  docker-compose up -d
  docker-compose scale simulate=4
  docker-compose scale retrieve=1
  ```
  
## Running the demo

  * Everything can be run as above or the `setup.sh` can be used to get everything started.
  * Use `docker-compose scale` to increase/decrease each container and monitor queue length.
  * With Slack open, the slacker container will provide status of the queue every few seconds.
  * Future will scale up/down in Azure Container Service.
  
## To do

  - [x] Create initial container images and test on single docker vm
  - [ ] Need to create environment variables for Azure queues, documentDB, etc. Env variables will be declared in container definition
  - [ ] Integrate with ACS
  - [ ] Create Azure Web App to display results
