# wxbot

> 基于itchat + nginx
> 简陋的文档，懒得写，凑活看

## 安装

### 第一种启动容器

1. 有个docker
2. `docker pull septnn/wxbot:1.0`
3. `docker run --name wxbot -itd -p 8040:8040 --cap-add=SYS_PTRACE --dns=114.114.114.114 septnn/wxbot:1.0`
4. 访问`http://192.168.99.100:8040`

### 第二种构建一个

1. 有个docker
2. `git clone https://github.com/septnn/tools.git`
3. `cd docker/wxbot`
4. `sh build.sh`
5. 访问`http://192.168.99.100:8040`
