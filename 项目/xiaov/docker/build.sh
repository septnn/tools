docker stop xiaov
docker rm xiaov
docker rmi $(docker images septnn/xiaov:1.0 -q)
docker build -t septnn/xiaov:1.0 .
docker run --name xiaov -itd \
-p 8140-8150:8140-8150 \
--cap-add=SYS_PTRACE \
--dns=114.114.114.114 \
-v /c/Users/JWD/Documents/git/github/septnn/tools/项目/xiaov/docker:/home/project/www \
septnn/xiaov:1.0