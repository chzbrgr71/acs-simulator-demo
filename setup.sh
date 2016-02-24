# Build containers
docker build -t chzbrgr71/acs-simulator simulator

docker run -d --name simulator chzbrgr71/acs-simulator

# Compose
# docker-compose up -docker