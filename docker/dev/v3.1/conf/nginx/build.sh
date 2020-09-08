docker stop nginx
docker rm nginx
docker run --name nginx -itd -p 80:80 -p 443:443 -p 81:81 --dns=114.114.114.114 -v /e/vhall:/home/vhall -v /e/github/tools/docker/dev/v3.1/conf/nginx:/etc/nginx nginx /bin/bash
