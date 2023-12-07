ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-nocuda:sha-5dafa77
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME grader

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN pip install \
    ngshare_exchange\
    && rm -rf /tmp/* $HOME/.cache

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Image for nbgrader admins"
LABEL org.opencontainers.image.description="Image for nbgrader admins"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER