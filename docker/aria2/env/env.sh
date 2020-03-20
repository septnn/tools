#!/usr/bin/env sh
#====================================================
# Description: Initialize profile.
# Lisence: MIT
# Version: 1.0
# Author: septnn
#=====================================================

# Source base.
BASE_FILE='./base.sh'
source $BASE_FILE

ENV_FILE='./.env'
source $ENV_FILE

ec 'Start initializing profile. The configuration is as follows:'

cat $ENV_FILE | while read i;do
    head=${i:0:1}
    if [ $head == "#" ]; then
        continue
    fi
    key=${i%=*}
    value=${i#*=}
    ec "Key:$key Value:$value" debug
    set -v
    sed -i "s|$key|$value|g" `find ./*`
    set +v
done
