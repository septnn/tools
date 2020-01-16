docker stop nginx
docker rm nginx
docker run --name nginx -itd -p 80:80 -p 443:443 \
--dns=114.114.114.114 \
-v /c/Users/JWD/Documents/git:/home/git -v /c/Users/JWD/Documents/git/github/septnn/tools/docker/dev/v3/conf/nginx:/etc/nginx nginx:1.17.6
