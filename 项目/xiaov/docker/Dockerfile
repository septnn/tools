FROM python:3.7.7-alpine3.10
LABEL maintainer="septnn@163.com"
WORKDIR /home/project
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.3/main/" > /etc/apk/repositories
ADD nginx.conf /home/project/nginx.conf
ADD requirements.txt /home/project/requirements.txt
RUN apk add nginx && rm -f /etc/nginx/nginx.conf && ln -s /home/project/nginx.conf /etc/nginx/nginx.conf
RUN apk add openssl
RUN openssl req -new -newkey rsa:2048 -sha256 -nodes -out server.csr -keyout server.key -subj "/C=CN/ST=BeiJing/L=BeiJing/O=xiaov Inc./OU=Web Security/CN=192.168.99.100"
RUN openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
RUN apk del openssl
# RUN pip install -r /home/project/requirements.txt -i http://pypi.douban.com/simple/
RUN mkdir /home/project/www
EXPOSE 8140-8150
# ENTRYPOINT ["/home/project/run.sh"]