docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi chzbrgr71/acs-simulator
docker rmi chzbrgr71/acs-retriever
docker ps -a
docker images