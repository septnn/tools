# Aria2 + AriaNg

> 简陋的文档，懒得写，凑活看

## 安装

### 第一种启动容器

1. 有个docker
2. `docker pull septnn/aria2`
3. `docker run --name aria2 -itd -p 8030:8030 -p 8031:8031 -p 8032:8032 --cap-add=SYS_PTRACE --dns=114.114.114.114 -v $PWD:ARIA_DOWNLOAD_PTAH -v $PWD:ARIA_DOWNLOAD_PTAH/dht.dat septnn/aria2`
   1. 备注ARIA_DOWNLOAD_PTAH在.env配置可以找到
4. 访问`http://192.168.99.100:8030`
5. 修改AriaNg的rpc配置，`192.168.99.100:8031`

### 第二种构建一个

1. 有个docker
2. `git clone https://github.com/septnn/tools.git`
3. `cd docker/aria2`
4. `sh install.sh`
5. `docker run --name aria2 -itd -p 8030:8030 -p 8031:8031 -p 8032:8032 --cap-add=SYS_PTRACE --dns=114.114.114.114 -v $PWD:ARIA_DOWNLOAD_PTAH -v $PWD:ARIA_DOWNLOAD_PTAH/dht.dat septnn/aria2`
6. 访问`http://192.168.99.100:8030`
7. 修改AriaNg的rpc配置，`192.168.99.100:8031`
