docker stop wxbot
docker rm wxbot
docker rmi $(docker images septnn/wxbot:1.0 -q)
docker build -t septnn/wxbot:1.0 .
docker run --name wxbot -itd \
-p 8040:8040 \
--cap-add=SYS_PTRACE \
--dns=114.114.114.114 \
septnn/wxbot:1.0