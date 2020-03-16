docker stop wechaty
docker rm wechaty
docker rmi $(docker images septnn/wechaty:1.0 -q)
docker build -t septnn/wechaty:1.0 .
docker run --name wechaty -itd \
-p 8050:8050 \
--cap-add=SYS_PTRACE \
--dns=114.114.114.114 \
-v /c/Users/JWD/Documents/git/github/septnn/python-wechaty:/home/project/wechaty \
septnn/wechaty:1.0