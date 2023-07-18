#!/bin/bash
# looks for .sh scripts to source and runs them
run-user-hooks () {
    if [[ ! -d "${1}" ]] ; then
        return
    fi
    echo "${0}: running user hooks in ${1}"
    for f in "${1}/"*; do
        case "${f}" in
            *.sh)
                echo "${0}: running script ${f}"
                # shellcheck disable=SC1090
                source "${f}" > "$HOME/.startup-hooks/$BUILD_IMAGE_NAME/logs/${f}"
                ;;
            *)
                echo "${0}: ignoring non shell script ${f}"
                ;;
        esac
    done
    echo "${0}: done running user hooks in ${1}"
}

run-user-hooks $HOME/.startup-hooks/$BUILD_IMAGE_NAME
