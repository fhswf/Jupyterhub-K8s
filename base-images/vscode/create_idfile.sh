#!/bin/bash
set -e

if [[ ! -f "$HOME/.id" ]] ; then
    echo "no id found in $HOME, creating from env NB_USER";
    echo $NB_USER > $HOME/.id
    chmod 0444 $HOME/.id
else
    echo ".id found in $HOME";
fi