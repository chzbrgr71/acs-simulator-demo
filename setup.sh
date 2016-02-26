# Build containers
docker build -t chzbrgr71/acs-simulator-demo:simulator simulator
docker build -t chzbrgr71/acs-simulator-demo:retriever retriever
docker build -t chzbrgr71/acs-simulator-demo:slacker slacker

docker run -d --name slack chzbrgr71/acs-simulator-demo:slacker
docker run -d --name sim1 chzbrgr71/acs-simulator-demo:simulator
docker run -d --name sim2 chzbrgr71/acs-simulator-demo:simulator
docker run -d --name ret1 chzbrgr71/acs-simulator-demo:retriever

# Compose
# docker-compose up -d
# docker-compose scale simulate=4
# docker-compose scale retrieve=1