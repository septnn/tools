# wechaty

> 基于wechaty + nginx
> 简陋的文档，懒得写，凑活看

## 安装

### 第一种启动容器

1. 有个docker
2. `docker pull septnn/wechaty:1.0`
3. `docker run --name wechaty -itd -p 8040:8040 --cap-add=SYS_PTRACE --dns=114.114.114.114 septnn/wechaty:1.0`
4. 访问`http://192.168.99.100:8040`

### 第二种构建一个

1. 有个docker
2. `git clone https://github.com/septnn/tools.git`
3. `cd docker/wechaty`
4. `sh build.sh`
5. 访问`http://192.168.99.100:8040`

## 开发环境

### 额外需要安装的依赖

- apk add gcc g++ cmake ninja re2c
- pip install scikit-build mypy flake8 pylint pycodestyle pytest pytype
