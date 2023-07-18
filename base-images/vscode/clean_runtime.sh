#!/bin/bash
if [[ -d "$HOME/.local/share/jupyter/runtime" ]] ; then
    rm -f $HOME/.local/share/jupyter/runtime/kernel-*.json $HOME/.local/share/jupyter/runtime/nbserver-*.html $HOME/.local/share/jupyter/runtime/nbserver-*.json;
else
    rm -f /home/jovyan/.local/share/jupyter/runtime/kernel-*.json /home/jovyan/.local/share/jupyter/runtime/nbserver-*.html /home/jovyan/.local/share/jupyter/runtime/nbserver-*.json;
fi
echo "done cleaning left over kernel connectors"