docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi chzbrgr71/acs-demo-retriever:2
docker rmi chzbrgr71/acs-demo-simulator:2
docker rmi chzbrgr71/acs-demo-slacker:2
docker rmi chzbrgr71/acs-demo-base:2
docker ps -a
docker images