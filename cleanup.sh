docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi chzbrgr71/acs-demo-retriever
docker rmi chzbrgr71/acs-demo-simulator
docker rmi chzbrgr71/acs-demo-slacker
docker rmi chzbrgr71/acs-demo-base
docker ps -a
docker images