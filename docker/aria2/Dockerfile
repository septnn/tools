FROM alpine:latest
LABEL maintainer="septnn@163.com"
WORKDIR /home/aria2
RUN mkdir -p /home/aria2/.aria2/
ADD aria2.conf /home/aria2/.aria2/aria2.conf
ADD nginx.conf /home/aria2/.aria2/nginx.conf
ADD run.sh /home/aria2/.aria2/run.sh
RUN chmod +x /home/aria2/.aria2/run.sh
RUN apk --update add aria2 nginx
RUN wget https://github.com/mayswind/AriaNg-DailyBuild/archive/master.zip -O AriaNg.zip && unzip AriaNg.zip && mv AriaNg-DailyBuild-master/ AriaNg
RUN ln -s /home/aria2/.aria2/nginx.conf /etc/nginx/conf.d/nginx.conf && mkdir /run/nginx/
RUN mkdir -p /root/.config/aria2/ && ln -s /home/aria2/.aria2/aria2.conf /root/.config/aria2/aria2.conf && touch /home/aria2/.aria2/aria2.session
EXPOSE 8030
EXPOSE 8031
EXPOSE 8032
ENTRYPOINT ["/home/aria2/.aria2/run.sh"]
# CMD ["/home/aria2/.aria2/run.sh"]