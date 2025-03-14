ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-nocuda:sha-622f43f
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME skriptsprachen

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

USER $NB_UID

# Install PYthon Libs
RUN pip install \
    chess musicbrainzngs wikipedia-api PyPDF2 beautifulsoup4 matplotlib mock nose numpy openpyxl requests yfinance \
    && rm -rf /tmp/* $HOME/.cache

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Skriptsprachen"
LABEL org.opencontainers.image.description="Skriptsprachen"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER
