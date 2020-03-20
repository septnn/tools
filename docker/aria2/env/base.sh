#!/usr/bin/env sh
#=====================================================
# Description: Base file.
# Lisence: MIT
# Version: 1.0
# Author: septnn
#=====================================================

DEBUG=false

# /home/aria2
# ec "this is info"
# ec "this is error" error
ec(){
    level=$2
    if [ "$2"x = "x" ]; then
        level="info"
    fi
    level=$(echo $level | tr '[a-z]' '[A-Z]')
    if [ $DEBUG != true ] && [ $level != "INFO" ]; then
        return 0
    fi
    t=$(date +"%m/%d %H:%M:%S")
    case $level in
        DEBUG)
            echo -e "\033[1;34m$t [DEBUG] $1\033[0m"
        ;;
        ERROR)
            echo -e "\033[1;31m$t [ERROR] $1\033[0m"
        ;;
        *)
            echo -e "$t [\033[1;32mINFO\033[0m] $1"
        ;;
    esac
}