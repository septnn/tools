#!/usr/bin/env sh
#====================================================
# Description: Installer.
# Lisence: MIT
# Version: 1.0
# Author: septnn
#=====================================================

# Source base.
BASE_FILE='./env/base.sh'
source $BASE_FILE

echo "Debug:"$DEBUG

ec 'Create runtimes dir.'
# 创建运行时文件夹
mkdir -p ./runtimes
ec 'Copy configuration file to runtimes.'
# 复制初始文件
cp -r .env runtimes/
cp -r env/* runtimes/
cp -r docker/* runtimes/
cp -r nginx/* runtimes/
cd runtimes
# 初始化配置
/usr/bin/env sh env.sh
# 构建镜像
/usr/bin/env sh build.sh
# 删除执行时文件
ec 'Delete runtimes file.'
cd ../
rm -rf ./runtimes/
ec 'Installation is complete.'
