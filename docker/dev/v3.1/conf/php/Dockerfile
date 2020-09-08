FROM php:7.4-fpm
LABEL maintainer="septnn@163.com"
WORKDIR /home/git
ADD sources.list /etc/apt/
RUN echo 'nameserver 114.114.114.114' >> /etc/resolv.conf
RUN apt-get update
RUN mkdir /var/log/service \
            && chmod 777 /var/log/service \
            && docker-php-ext-install bcmath pdo_mysql
ENV TZ="Asia/Shanghai"
EXPOSE 9000