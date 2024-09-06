#!/bin/bash
set -e

# works for command: docker run --user 5000:100 --group-add root --group-add 1000 -e NB_USER="myuser" ...
if [[ -w /etc/passwd ]] && [[ -w /home ]]; then
    if [[ "${NB_USER}" != "jovyan" ]]; then
         _log "creating enw home for user ${NB_USER}"
        mkdir -p /home/${NB_USER};
        cp /etc/passwd /tmp/passwd;
        sed -i '/jovyan:x:1000:100/d' /tmp/passwd
        echo "creating passwd entry ${NB_USER}:x:$(id -u):$(id -g):,,,:/home/${NB_USER}:/bin/bash";
        echo "${NB_USER}:x:$(id -u):$(id -g):,,,:/home/${NB_USER}:/bin/bash" >> /tmp/passwd;
        cat /tmp/passwd > /etc/passwd;
        rm /tmp/passwd;
        if  [[ $HOME !=  "/home/${NB_USER}" ]]; then
            export HOME=/home/${NB_USER}
        fi
        if [[ ${PWD}/ == "/home/jovyan/"* ]]; then
            new_wd="/home/${NB_USER}/${PWD:13}"
            echo "Changing working directory to ${new_wd}"
            cd "${new_wd}"
        fi
        # snippets taken from the docker-stacks start.sh that do not get executed atm.
        # note that file system permissions for /home/${NB_USER} have to be checked/corercted with a privilieged initContainer.
        export XDG_CACHE_HOME="/home/${NB_USER}/.cache"
    fi
else
    echo "WARNING: unable to fix missing /etc/passwd entry because we don't have write permission. Try setting gid=0 with \"--user=$(id -u):0\"."
fi