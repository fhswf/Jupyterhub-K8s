#!/bin/bash
set -e

if [[ ! -d "$HOME/PICO" ]] ; then
    echo "cping /opt/PICO";
    cp -R  /opt/PICO/* $HOME/PICO
else
    echo "/opt/PICO found in $HOME";
fi