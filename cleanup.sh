docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi chzbrgr71/acs-simulator
docker ps -a
docker images
