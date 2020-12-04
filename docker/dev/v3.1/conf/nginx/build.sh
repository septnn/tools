docker stop nginx
docker rm nginx
docker run --name nginx -itd --network vhall --network-alias nginx -p 80:80 -p 443:443 -p 81:81 -v /mnt/e/vhall:/home/vhall -v /mnt/e/github/tools/docker/dev/v3.1/conf/nginx:/etc/nginx nginx
