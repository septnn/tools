FROM php:7.0.33-fpm
LABEL maintainer="septnn@163.com"
WORKDIR /var/www/html
RUN apt-get update -y
RUN apt install -y imagemagick libmagick++-dev libmcrypt-dev
RUN export LD_RUN_PATH=/usr/local/lib/ && export LD_LIBRARY_PATH=/usr/local/lib/
RUN pecl install yaf redis imagick mongodb  swoole
RUN docker-php-ext-install bcmath
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install mcrypt
RUN docker-php-ext-install gd
RUN docker-php-ext-install pcntl
RUN docker-php-ext-install tokenizer
RUN docker-php-ext-install xml
RUN docker-php-ext-install sockets
RUN docker-php-ext-install zip
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN rm -rf /tmp/pear
ENV TZ="Asia/Shanghai"
EXPOSE 9000