#!/bin/bash
set -e

if [[ ! -f "$HOME/PICO" ]] ; then
    echo "cping /opt/PICO";
    cp -r  /home/jovyan/PICO $HOME/PICO
else
    echo "/opt/PICO found in $HOME";
fi