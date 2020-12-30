docker stop phpfpm7325
docker rm phpfpm7325
docker rmi $(docker images phpfpm7325 -q)
docker build -t phpfpm7325 .
docker run --name phpfpm7325 -itd --network vhall --network-alias phpfpm7325 --cap-add=SYS_PTRACE  -v /mnt/e/vhall:/home/vhall -v /mnt/e/github/tools/docker/dev/v3.1/conf/php7.3.25:/usr/local/etc phpfpm7325