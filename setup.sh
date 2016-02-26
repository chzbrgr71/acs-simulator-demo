# Build containers
docker build -t chzbrgr71/acs-simulator simulator
docker build -t chzbrgr71/acs-retriever retriever
docker build -t chzbrgr71/acs-slacker slacker

docker run -d --name sim1 chzbrgr71/acs-simulator
docker run -d --name sim2 chzbrgr71/acs-simulator
docker run -d --name ret1 chzbrgr71/acs-retriever
docker run -d --name slack chzbrgr71/acs-slacker

# Compose
# docker-compose up -docker