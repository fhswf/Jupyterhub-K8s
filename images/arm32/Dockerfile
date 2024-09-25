ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-minimal-nocuda:sha-e9575c4
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME eml

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN apt update && apt install -y \
    cmake gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib g++ \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/PICO
RUN fix-permissions /opt/PICO

COPY link_files.sh /usr/local/bin/before-notebook.d/90_link_files.sh
RUN  chmod +x /usr/local/bin/before-notebook.d/90_link_files.sh

USER $NB_UID

RUN cd /opt/PICO && git clone https://github.com/fhswf/PICO-CAM-A.git
RUN mkdir /opt/PICO/PICO-CAM-A/build && cd /opt/PICO/PICO-CAM-A/build && cmake -D PICO_SDK_FETCH_FROM_GIT=1 ..
#RUN cd /opt/PICO/PICO-CAM-A/build && make

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="arm32"
LABEL org.opencontainers.image.description="arm32"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER
