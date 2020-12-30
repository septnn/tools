FROM php:7.3.25-fpm
LABEL maintainer="septnn@163.com"
WORKDIR /var/www/html
RUN apt-get update -y
RUN apt install -y imagemagick libmagick++-dev libmcrypt-dev
RUN export LD_RUN_PATH=/usr/local/lib/ && export LD_LIBRARY_PATH=/usr/local/lib/
#RUN wget http://curl.haxx.se/ca/cacert.pem && mv cacert.pem /usr/local/openssl/cert.pem

RUN curl -L -o ./yaf.tar.gz https://github.com/laruence/yaf/archive/yaf-3.2.5.tar.gz
RUN tar -zxvf yaf.tar.gz && rm yaf.tar.gz
RUN docker-php-ext-configure /var/www/html/yaf-yaf-3.2.5
RUN docker-php-ext-install /var/www/html/yaf-yaf-3.2.5 && rm -rf /var/www/html/yaf-yaf-3.2.5
RUN curl -L -o ./redis.tar.gz https://github.com/phpredis/phpredis/archive/4.3.0.tar.gz
RUN tar -zxvf redis.tar.gz && rm redis.tar.gz
RUN docker-php-ext-configure /var/www/html/phpredis-4.3.0
RUN docker-php-ext-install /var/www/html/phpredis-4.3.0 && rm -rf /var/www/html/phpredis-4.3.0
# RUN curl -L -o ./imagick.tar.gz http://pecl.php.net/get/imagick-3.4.4.tgz
# RUN tar -zxvf imagick.tar.gz && rm imagick.tar.gz
# RUN docker-php-ext-configure /var/www/html/imagick-3.4.4
# RUN docker-php-ext-install /var/www/html/imagick-3.4.4 && rm -rf /var/www/html/imagick-3.4.4
RUN curl -L -o ./mcrypt.tar.gz https://pecl.php.net/get/mcrypt-1.0.4.tgz
RUN tar -zxvf mcrypt.tar.gz && rm mcrypt.tar.gz
RUN docker-php-ext-configure /var/www/html/mcrypt-1.0.4
RUN docker-php-ext-install /var/www/html/mcrypt-1.0.4 && rm -rf /var/www/html/mcrypt-1.0.4
RUN apt install -y libzip-dev
RUN docker-php-ext-install bcmath pdo_mysql zip
RUN docker-php-ext-install pcntl tokenizer
RUN docker-php-ext-install xml sockets
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd
RUN rm -rf /tmp/pear
ENV TZ="Asia/Shanghai"
EXPOSE 9001