ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-nocuda:sha-e9575c4
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME grader

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root


RUN pip install --no-deps \          
    #nbgrader==0.8.5 \ # use fork instead
    git+https://github.com/jeflem/nbgrader.git@ananke_0.5 \
    # not sure if we need the kore-extension, does not have extra deps?
    git+https://github.com/marcwit/kore-extension.git@ananke_0.5 \
    # nbgrader dependencies
    rapidfuzz hatchling>=1.10.0 editables pathspec trove-classifiers \
    && rm -rf /tmp/* $HOME/.cache

COPY nbgrader_config.py /etc/jupyter/nbgrader_config.py
RUN chmod -R 777 /etc/jupyter && mkdir "/home/test_course1" && chmod -R 777 "/home/test_course1"

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="DEV Image for nbgrader admins"
LABEL org.opencontainers.image.description="DEV Image for nbgrader admins"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER