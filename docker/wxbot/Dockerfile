FROM alpine:latest
LABEL maintainer="septnn@163.com"
WORKDIR /home/wxbot
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.3/main/" > /etc/apk/repositories
#ADD wxbot.conf /home/wxbot/wxbot.conf
ADD nginx.conf /home/wxbot/nginx.conf
ADD run.sh /home/wxbot/run.sh
ADD run.py /home/wxbot/run.py
RUN chmod +x /home/wxbot/run.sh /home/wxbot/run.py
RUN apk --no-cache add python py-pip nginx
RUN python -m pip install --upgrade pip -i "https://pypi.doubanio.com/simple/"
RUN pip install itchat -i "https://pypi.doubanio.com/simple/"
RUN rm -f /etc/nginx/nginx.conf
RUN ln -s /home/wxbot/nginx.conf /etc/nginx/nginx.conf
EXPOSE 8040
# ENTRYPOINT ["/home/wxbot/run.sh"]