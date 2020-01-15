FROM php:7.4-fpm
LABEL maintainer="septnn@163.com"
WORKDIR /home/git
RUN echo 'nameserver 114.114.114.114' >> /etc/resolv.conf \
            && apt-get update && apt-get install -y
RUN mkdir /var/log/service \
            && chmod 777 /var/log/service \
            && docker-php-ext-install pdo_mysql
ENV TZ="Asia/Shanghai"
EXPOSE 9000