# vhall

## zhike

```shell script

docker pull php:7.0.33-fpm
docker pull nginx


docker stop php-fpm 
docker rm php-fpm
#docker run --name php-fpm -itd --network-alias php-fpm --cap-add=SYS_PTRACE --dns=114.114.114.114 --add-host='dev-api-zhike.vhall.domain:127.0.0.1' --add-host='dev-zhike.vhall.domain:127.0.0.1' --add-host='elk.vhallservice.com:127.0.0.1' -v /e/vhall:/home/vhall -v /e/github/tools/docker/dev/v3.1/conf/php:/usr/local/etc php:7.4-fpm

docker stop phpfpm7033 && docker rm phpfpm7033
#docker run --name phpfpm7033 -itd --network vhall --network-alias phpfpm7033 --cap-add=SYS_PTRACE --dns=114.114.114.114 --add-host='dev-api-zhike.vhall.domain:127.0.0.1' --add-host='dev-zhike.vhall.domain:127.0.0.1' --add-host='elk.vhallservice.com:127.0.0.1' -v /e/vhall:/home/vhall -v /e/github/tools/docker/dev/v3.1/conf/php7.0.33:/usr/local/etc php:7.0.33-fpm

docker stop phpfpm7033 
docker rm phpfpm7033
docker run --name phpfpm7033 -itd --network-alias phpfpm7033 --cap-add=SYS_PTRACE --dns=114.114.114.114 --add-host='dev-api-zhike.vhall.domain:127.0.0.1' --add-host='dev-zhike.vhall.domain:127.0.0.1' --add-host='elk.vhallservice.com:127.0.0.1' -v /mnt/e/vhall:/home/vhall -v /mnt/e/github/tools/docker/dev/v3.1/conf/php7.0.33:/usr/local/etc php:7.0.33-fpm


docker stop nginx 
docker rm nginx
# docker run --name nginx -itd --network-alias nginx -p 80:80 -p 443:443 -p 81:81 -p 5141:5141 --dns=114.114.114.114 --add-host='dev-api-zhike.vhall.domain:127.0.0.1' --add-host='dev-zhike.vhall.domain:127.0.0.1' --add-host='elk.vhallservice.com:127.0.0.1' -v /e/vhall:/home/vhall -v /e/github/tools/docker/dev/v3.1/conf/nginx:/etc/nginx nginx
docker run --name nginx -itd --network-alias nginx -p 80:80 -p 443:443 -p 81:81 -p 5141:5141 --dns=114.114.114.114 --add-host='dev-api-zhike.vhall.domain:127.0.0.1' --add-host='dev-zhike.vhall.domain:127.0.0.1' --add-host='elk.vhallservice.com:127.0.0.1' -v /mnt/e/vhall:/home/vhall -v /mnt/e/github/tools/docker/dev/v3.1/conf/nginx:/etc/nginx nginx

# 可选 es+kibana
docker run -it --rm --name=es1 --network-alias es -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.8.0
docker run -it --rm --name k1 --network-alias k -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://es1:9200/" kibana:7.8.0

```

```shell script
# php

#sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
apt update
apt install imagemagick libmagick++-dev
apt install libmcrypt-dev

export LD_RUN_PATH=/usr/local/lib/ && export LD_LIBRARY_PATH=/usr/local/lib/
docker-php-ext-install pdo_mysql bcmath 

pecl install yaf
pecl install redis
pecl install imagick
pecl install mcrypt-1.0.1 # > 7.2
pecl install mongodb 
pecl install swoole 
docker-php-ext-enable imagick yaf mongodb swoole 
docker-php-ext-install pdo_pgsql pdo_sqlite 
docker-php-ext-install mcrypt
docker-php-ext-install gd
docker-php-ext-install pcntl tokenizer xml sockets zip 
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ 
docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" gd 
pecl install -o -f redis 
rm -rf /tmp/pear 
docker-php-ext-enable redis
```



## saas

```json
{
  "registry-mirrors": [],
  "insecure-registries": [],
  "debug": false,
  "experimental": false,
  "features": {
    "buildkit": true
  },
  "dns": [
    "192.168.1.160",
    "192.168.1.161",
    "192.168.13.26",
    "192.168.13.27",
    "114.114.114.114"
  ]
}
```

```shell script
docker network create vhall
```
```shell script
# php
#sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
apt update
apt install imagemagick libmagick++-dev
apt install libmcrypt-dev
export LD_RUN_PATH=/usr/local/lib/ && export LD_LIBRARY_PATH=/usr/local/lib/
docker-php-ext-install pdo_mysql bcmath 
pecl install yaf
pecl install redis
pecl install imagick
pecl install mcrypt-1.0.1 # > 7.2
pecl install mongodb 
pecl install swoole 
docker-php-ext-enable imagick yaf mongodb swoole 
docker-php-ext-install pdo_pgsql pdo_sqlite 
docker-php-ext-install mcrypt
docker-php-ext-install gd
docker-php-ext-install pcntl tokenizer xml sockets zip 
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ 
docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" gd 
pecl install -o -f redis 
rm -rf /tmp/pear 
docker-php-ext-enable redis
```

## nginx https

```shell script
# nginx https
cd /etc/nginx/conf.d
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt
openssl genrsa -out server.key 4096
openssl req -new -key server.key -out server.csr
# Common Name (e.g. server FQDN or YOUR name) []:vhall.com
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 3650
openssl genrsa -out client.key 4096
openssl req -new -key client.key -out client.csr
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 3650

```