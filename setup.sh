# Build containers
docker build -t chzbrgr71/acs-simulator simulator
docker build -t chzbrgr71/acs-retriever retriever

# docker run -d --name sim1 chzbrgr71/acs-simulator
# docker run -d --name sim2 chzbrgr71/acs-simulator
docker run -d --name retriever chzbrgr71/acs-retriever

# Compose
# docker-compose up -docker