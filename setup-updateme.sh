# Build containers
docker build -t chzbrgr71/acs-demo-simulator simulator
docker build -t chzbrgr71/acs-demo-retriever retriever
docker build -t chzbrgr71/acs-demo-slacker slacker

# Update commands below with environment variables from your Azure subscription
docker run -d -e "AZURE_SB_SERVICE_NAMESPACE=<add your value here>" -e "AZURE_SB_SHARED_ACCESS_KEY_NAME=<add your value here>" -e "AZURE_SB_SHARED_ACCESS_KEY=<add your value here>" -e "SLACK_CHANNEL=<add your value here>" --name slack chzbrgr71/acs-demo-slacker

docker run -d -e "AZURE_SB_SERVICE_NAMESPACE=<add your value here>" -e "AZURE_SB_SHARED_ACCESS_KEY_NAME=<add your value here>" -e "AZURE_SB_SHARED_ACCESS_KEY=<add your value here>" -e "SLACK_CHANNEL=<add your value here>" --name sim1 chzbrgr71/acs-demo-simulator

docker run -d -e "AZURE_SB_SERVICE_NAMESPACE=<add your value here>" -e "AZURE_SB_SHARED_ACCESS_KEY_NAME=<add your value here>" -e "AZURE_SB_SHARED_ACCESS_KEY=<add your value here>" -e "SLACK_CHANNEL=<add your value here>" --name sim2 chzbrgr71/acs-demo-simulator

docker run -d -e "AZURE_SB_SERVICE_NAMESPACE=<add your value here>" -e "AZURE_SB_SHARED_ACCESS_KEY_NAME=<add your value here>" -e "AZURE_SB_SHARED_ACCESS_KEY=<add your value here>" -e "SLACK_CHANNEL=<add your value here>" -e "AZURE_DOCUMENTDB_URI=<add your value here>" -e "AZURE_DOCUMENTDB_KEY=<add your value here>" --name ret1 chzbrgr71/acs-demo-retriever