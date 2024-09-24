ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-minimal-nocuda:sha-e9575c4
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME eml

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt update && apt install cmake gcc-arm-none-eabi build-essential -y  \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="arm32"
LABEL org.opencontainers.image.description="arm32"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER
