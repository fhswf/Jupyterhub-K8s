ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-base:sha-e108ac9
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME compilerbau

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    flex \
    bison \
    libfl-dev \
    libbison-dev \
    graphviz \
    git \
    gcc \
    make \
    clang \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Programmierung fuer KI"
LABEL org.opencontainers.image.description="Programmierung fuer KI"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER
