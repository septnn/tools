#!/usr/bin/env sh
#=====================================================
# Description: After Aria2 download error.
# Lisence: MIT
# Version: 2.0
# Author: septnn
#=====================================================

# TODO 文件处理

DOWNLOAD_PATH=ARIA_DOWNLOAD_PTAH

FILE_PATH=$3
REMOVE_DOWNLOAD_PATH=${FILE_PATH#${DOWNLOAD_PATH}/}
TOP_PATH=${DOWNLOAD_PATH}/${REMOVE_DOWNLOAD_PATH%%/*}

if [ $2 -eq 0 ]; then
    exit 0
elif [ -e "${FILE_PATH}.aria2" ]; then
    rm -vf "${FILE_PATH}.aria2" "${FILE_PATH}"
elif [ -e "${TOP_PATH}.aria2" ]; then
    rm -vrf "${TOP_PATH}.aria2" "${TOP_PATH}"
fi