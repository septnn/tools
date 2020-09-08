docker stop php-fpm
docker rm php-fpm
docker rmi $(docker images php:1.0-fpm-septnn -q)
docker build -t php:1.0-fpm-septnn .
docker run --name php-fpm -itd -p 9000:9000 --cap-add=SYS_PTRACE --dns=114.114.114.114 -v /e/vhall:/home/vhall -v /e/github/tools/docker/dev/v3.1/conf/php:/usr/local/etc php:1.0-fpm-septnn /bin/bash