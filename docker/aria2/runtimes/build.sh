#!/usr/bin/env bash
#====================================================
# Description: Build docker images.
# Lisence: MIT
# Version: 1.0
# Author: septnn
#=====================================================

# Source base.
BASE_FILE='./base.sh'
source $BASE_FILE

ec 'Building containers.'

set -v
docker stop aria2
docker rm aria2
docker rmi $(docker images septnn/aria2:2.0 -q)
docker build -t septnn/aria2:2.0 .
docker run --name aria2 -itd \
-p 8030-8130:8030-8130 \
--cap-add=SYS_PTRACE \
--dns=114.114.114.114 \
septnn/aria2:2.0
set +v