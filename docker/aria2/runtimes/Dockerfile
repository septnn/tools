FROM alpine:latest
LABEL maintainer="septnn@163.com"
WORKDIR /home/aria2
RUN mkdir -p /home/aria2/download
RUN mkdir -p /root/.config/aria2/
RUN mkdir /run/nginx/
ADD aria2.conf /home/aria2/aria2.conf
ADD nginx.conf /home/aria2/nginx.conf
ADD run.sh /home/aria2/run.sh
ADD complete.sh /home/aria2/complete.sh
ADD complete-stop.sh /home/aria2/complete-stop.sh
RUN touch /home/aria2/aria2.session
RUN chmod +x /home/aria2/run.sh /home/aria2/complete.sh
RUN apk --update add aria2 nginx
RUN wget https://github.com/mayswind/AriaNg-DailyBuild/archive/master.zip -O AriaNg.zip && unzip AriaNg.zip && mv AriaNg-DailyBuild-master/ AriaNg && rm -rf AriaNg.zip
RUN ln -s /home/aria2/nginx.conf /etc/nginx/conf.d/nginx.conf
RUN ln -s /home/aria2/aria2.conf /root/.config/aria2/aria2.conf
EXPOSE 8030-8130
ENTRYPOINT ["/home/aria2/run.sh"]