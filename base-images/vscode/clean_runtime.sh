#!/bin/bash
# cd cd /home/$NB_USER/.local/share/jupyter/runtime
cd $HOME/.local/share/jupyter/runtime

if [ $? -eq 0 ]; then
    rm kernel-*.json nbserver-*.html nbserver-*.json;
else
    cd /home/jovyan/.local/share/jupyter/runtime;
    if [ $? -eq 0 ]; then
        rm kernel-*.json nbserver-*.html nbserver-*.json;
    fi
fi

cd $HOME
echo "done cleaning left over kernel connectors"