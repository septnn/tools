# vhall

```shell script
docker network create vhall

docker stop php-fpm 
docker rm php-fpm
docker run --name php-fpm -itd --network vhall --network-alias php-fpm --cap-add=SYS_PTRACE --dns=114.114.114.114 --add-host='dev-api-zhike.vhall.domain:127.0.0.1' --add-host='dev-zhike.vhall.domain:127.0.0.1' -v /e/vhall:/home/vhall -v /e/github/tools/docker/dev/v3.1/conf/php:/usr/local/etc php:7.4-fpm

docker stop php-fpm-7.0.33 
docker rm php-fpm-7.0.33
docker run --name php-fpm-7.0.33 -itd --network vhall --network-alias php-fpm-7.0.33 --cap-add=SYS_PTRACE --dns=114.114.114.114 --add-host='dev-api-zhike.vhall.domain:127.0.0.1' --add-host='dev-zhike.vhall.domain:127.0.0.1' -v /e/vhall:/home/vhall -v /e/github/tools/docker/dev/v3.1/conf/php7.0.33:/usr/local/etc php:7.0.33-fpm

docker stop nginx 
docker rm nginx
docker run --name nginx -itd --network vhall --network-alias nginx -p 80:80 -p 443:443 -p 81:81 --dns=114.114.114.114 --add-host='dev-api-zhike.vhall.domain:127.0.0.1' --add-host='dev-zhike.vhall.domain:127.0.0.1' -v /e/vhall:/home/vhall -v /e/github/tools/docker/dev/v3.1/conf/nginx:/etc/nginx nginx

```

```shell script
# php

#sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
apt update
apt install imagemagick


export LD_RUN_PATH=/usr/local/lib/
export LD_LIBRARY_PATH=/usr/local/lib/
docker-php-ext-install pdo_mysql bcmath 

pecl install yaf 
pecl install imagick 
pecl install mcrypt-1.0.1 
pecl install mongodb 
pecl install swoole 
docker-php-ext-enable mcrypt imagick yaf mongodb swoole 
docker-php-ext-install  pdo_pgsql pdo_sqlite pcntl tokenizer xml sockets zip 
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ 
docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" gd 
pecl install -o -f redis 
rm -rf /tmp/pear 
docker-php-ext-enable redis
```