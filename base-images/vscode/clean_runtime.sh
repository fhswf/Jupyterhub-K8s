#!/bin/bash
# cd cd /home/$NB_USER/.local/share/jupyter/runtime
cd cd $HOME/.local/share/jupyter/runtime

if [ $? -eq 0 ]; then
    rm kernel-*.json nbserver-*.html nbserver-*.json;
else
    cd cd /home/jovyan/.local/share/jupyter/runtime;
    if [ $? -eq 0 ]; then
        rm kernel-*.json nbserver-*.html nbserver-*.json;
    fi
fi