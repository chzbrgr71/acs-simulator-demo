# Build containers
docker build -t chzbrgr71/acs-simulator-demo:simulator simulator
docker build -t chzbrgr71/acs-simulator-demo:retriever retriever
docker build -t chzbrgr71/acs-simulator-demo:slacker slacker

# Update commands below with environment variables from your Azure subscription
docker run -d -e "AZURE_SB_SERVICE_NAMESPACE=" -e "AZURE_SB_SHARED_ACCESS_KEY_NAME=" -e "AZURE_SB_SHARED_ACCESS_KEY==" -e "SLACK_CHANNEL=" --name slack chzbrgr71/acs-simulator-demo:slacker

docker run -d -e "AZURE_SB_SERVICE_NAMESPACE=" -e "AZURE_SB_SHARED_ACCESS_KEY_NAME=" -e "AZURE_SB_SHARED_ACCESS_KEY=" -e "SLACK_CHANNEL=" --name sim1 chzbrgr71/acs-simulator-demo:simulator

docker run -d -e "AZURE_SB_SERVICE_NAMESPACE=" -e "AZURE_SB_SHARED_ACCESS_KEY_NAME=" -e "AZURE_SB_SHARED_ACCESS_KEY=" -e "SLACK_CHANNEL=" --name sim2 chzbrgr71/acs-simulator-demo:simulator

docker run -d -e "AZURE_SB_SERVICE_NAMESPACE=" -e "AZURE_SB_SHARED_ACCESS_KEY_NAME=" -e "AZURE_SB_SHARED_ACCESS_KEY==" -e "SLACK_CHANNEL=" -e "AZURE_DOCUMENTDB_URI=" -e "AZURE_DOCUMENTDB_KEY=" --name ret1 chzbrgr71/acs-simulator-demo:retriever

# Compose
#docker-compose up -d
#docker-compose scale simulate=4
#docker-compose scale retrieve=1