FROM centos:latest
LABEL version = "1.0"
LABEL maintainer = "septnn septnn@sina.com"
LABEL description = "septnn"
MAINTAINER septnn septnn@sina.com
RUN echo "nameserver 114.114.114.114" >> /etc/resolv.conf  \
# 更新源
&& yum clean all \
&& yum install -y wget \
&& cd /etc/yum.repos.d/ \
&& mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup \
&& wget http://mirrors.aliyun.com/repo/Centos-8.repo \
&& yum clean all \
&& yum makecache \
&& yum update -y \
# 语言包
&& yum -y install langpacks-zh_CN.noarch langpacks-en_GB.noarch \
&& echo "LANG=en_US.utf-8" >> /etc/environment \
&& echo "LC_ALL=en_US.utf-8" >> /etc/environment \
&& echo "export LANGUAGE=en_US.utf-8" >> /etc/profile \
&& echo "export LC_ALL=en_US.utf-8" >> /etc/profile \
&& source /etc/profile \
# 编译环境
&& yum install -y gcc-c++ autoconf automake pcre-devel zlib-devel libtool make bison libxml2-devel openssl-devel sqlite-devel libcurl-devel libpng-devel oniguruma libzip-devel \
&& cd /home \
&& wget https://github.com/skvadrik/re2c/archive/1.3.tar.gz \
&& tar xvf 1.3.tar.gz \
&& cd /home/re2c-1.3/ \
&& autoreconf -i -W all \
&& ./configure --prefix=$RE2C_PATH \
&& make && make install \
&& cd /home \
&& wget https://github.com/kkos/oniguruma/archive/v6.9.4.tar.gz \
&& tar xvf v6.9.4.tar.gz \
&& cd /home/oniguruma-6.9.4/ \
&& sh autogen.sh \
&& ./configure --prefix=/usr && make && make install \
# 编译安装
&& echo "cd /home" \
&& cd /home \
&& wget http://nginx.org/download/nginx-1.17.7.tar.gz  \
&& wget https://github.com/php/php-src/archive/php-7.4.1.tar.gz  \
&& tar xvf nginx-1.17.7.tar.gz \
&& tar xvf php-7.4.1.tar.gz \
&& cd /home/nginx-1.17.7 \
&& ./configure \
&& make && make install \
&& cd /home/php-src-php-7.4.1/ \
&& ./buildconf --force \
&& ./configure  --enable-fpm --with-openssl --with-external-pcre --with-zlib --enable-bcmath --with-curl --enable-exif --disable-fileinfo --enable-gd --with-mhash --enable-mbstring --with-pdo-mysql --enable-soap --enable-sockets --enable-mysqlnd --with-zip \
&& make && make install 
EXPOSE 80
# RUN rm -rf /var/lib/yum/history/*.sqlite && rm -rf /var/cache/yum