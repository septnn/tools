FROM alpine:latest
LABEL maintainer="septnn@163.com"
WORKDIR WORK_PATH
RUN mkdir -p ARIA_DOWNLOAD_PTAH
RUN mkdir -p /root/.config/aria2/
RUN mkdir /run/nginx/
ADD aria2.conf WORK_PATH/aria2.conf
ADD nginx.conf WORK_PATH/nginx.conf
ADD run.sh WORK_PATH/run.sh
ADD complete.sh WORK_PATH/complete.sh
ADD complete-stop.sh WORK_PATH/complete-stop.sh
RUN touch WORK_PATH/aria2.session
RUN chmod +x WORK_PATH/run.sh WORK_PATH/complete.sh
RUN apk --update add aria2 nginx
RUN wget https://github.com/mayswind/AriaNg-DailyBuild/archive/master.zip -O AriaNg.zip && unzip AriaNg.zip && mv AriaNg-DailyBuild-master/ AriaNg && rm -rf AriaNg.zip
RUN ln -s WORK_PATH/nginx.conf /etc/nginx/conf.d/nginx.conf
RUN ln -s WORK_PATH/aria2.conf /root/.config/aria2/aria2.conf
EXPOSE ARIA_START_PORT-ARIA_END_PORT
ENTRYPOINT ["WORK_PATH/run.sh"]