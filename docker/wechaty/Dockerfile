FROM python:3.7.7-alpine3.10
LABEL maintainer="septnn@163.com"
WORKDIR /home/project
ADD nginx.conf /home/project/nginx.conf
ADD requirements.txt /home/project/requirements.txt
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple/
# RUN rm -f /etc/nginx/nginx.conf
# RUN ln -s /home/project/nginx.conf /etc/nginx/nginx.conf
EXPOSE 8050
# ENTRYPOINT ["/home/project/run.sh"]