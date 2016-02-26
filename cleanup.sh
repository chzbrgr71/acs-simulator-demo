docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi chzbrgr71/acs-simulator-demo:retriever
docker rmi chzbrgr71/acs-simulator-demo:simulator
docker rmi chzbrgr71/acs-simulator-demo:slacker
docker rmi chzbrgr71/acs-simulator-demo:base
docker ps -a
docker images