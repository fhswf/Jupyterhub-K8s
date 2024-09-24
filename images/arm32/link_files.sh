#!/bin/bash
set -e

if [[ ! -f "$HOME/PICO" ]] ; then
    echo "linking /opt/PICO";
    ln -s  /opt/PICO/ $HOME/PICO
else
    echo "/opt/PICO found in $HOME";
fi