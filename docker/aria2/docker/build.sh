#!/usr/bin/env sh
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
docker stop CONTAINER_NAME
docker rm CONTAINER_NAME
docker rmi $(docker images CONTAINER -q)
docker build -t CONTAINER .
ec 'Build is complete.'
# ec 'Docker running.'
# docker run --name CONTAINER_NAME -itd \
# -p ARIA_START_PORT-ARIA_END_PORT:ARIA_START_PORT-ARIA_END_PORT \
# --cap-add=SYS_PTRACE \
# --dns=114.114.114.114 \
# CONTAINER
set +v