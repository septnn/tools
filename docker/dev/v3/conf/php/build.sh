docker stop php-fpm
docker rm php-fpm
docker rmi $(docker images php:1.0-fpm-septnn -q)
docker build -t php:1.0-fpm-septnn .
docker run --name php-fpm -itd -p 9000:9000 \
--add-host='application-ssd-api:192.168.99.100' \
--add-host='application-tos-api:192.168.99.100' \
--add-host='tos-api.juewei.com:192.168.99.100' \
--add-host='service-aos-api:192.168.99.100' \
--add-host='service-osp-api:192.168.99.100' \
--add-host='service-ssd-activity:192.168.99.100' \
--add-host='service-ssd-misc:192.168.99.100' \
--add-host='service-ssd-order:192.168.99.100' \
--add-host='service-ssd-sku:192.168.99.100' \
--add-host='service-ssd-stat:192.168.99.100' \
--add-host='service-ssd-mbi:192.168.99.100' \
--dns=114.114.114.114 \
-v /c/Users/JWD/Documents/git:/home/git -v /c/Users/JWD/Documents/git/github/septnn/tools/docker/dev/v3/conf/php:/usr/local/etc php:1.0-fpm-septnn