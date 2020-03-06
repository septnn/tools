docker stop aria2
docker rm aria2
docker rmi $(docker images septnn/aria2:1.0 -q)
docker build -t septnn/aria2:1.0 .
docker run --name aria2 -itd \
-p 8030:8030 \
-p 8031:8031 \
-p 8032:8032 \
--cap-add=SYS_PTRACE \
--dns=114.114.114.114 \
septnn/aria2:1.0