#!/bin/bash
set -e

if [[ ! -f "$HOME/.bashrc" ]] ; then
    echo "no bashrc found in $HOME, restoring defaults";
    cp /etc/skel/.bashrc $HOME;
    cp /etc/skel/.profile $HOME;
    cp /etc/skel/.bash_logout $HOME;
else
    echo "bashrc found in $HOME";
fi