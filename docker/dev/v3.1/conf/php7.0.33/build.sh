docker stop phpfpm7033
docker rm phpfpm7033
docker rmi $(docker images phpfpm7033 -q)
docker build -t phpfpm7033 .
docker run --name phpfpm7033 -itd --network vhall --network-alias phpfpm7033 --cap-add=SYS_PTRACE  -v /mnt/e/vhall:/home/vhall -v /mnt/e/github/tools/docker/dev/v3.1/conf/php7.0.33:/usr/local/etc phpfpm7033