ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-nocuda:sha-b613e07
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME=pki

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

USER $NB_UID

# Install PYthon Libs
RUN python -m pip install --no-cache-dir \
    ipyturtle3==0.1.4 \
    jupyturtle \
    wikipedia-api==0.8.1 \
    beautifulsoup4==4.12.2 \
    nose==1.3.7 \
    geojson \
    && rm -rf /tmp/* "$HOME/.cache"

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Programmierung fuer KI"
LABEL org.opencontainers.image.description="Programmierung fuer KI"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER
