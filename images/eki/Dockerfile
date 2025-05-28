ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/deepml:sha-7908d3e
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME eki

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

COPY userscripts.sh /usr/local/bin/before-notebook.d/999_userscripts.sh
RUN  chmod +x /usr/local/bin/before-notebook.d/999_userscripts.sh

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Image for AI Model Quantization"
LABEL org.opencontainers.image.description="Image for AI Model Quantization"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER

LABEL ki.fh-swf.de.jupyterhub.project="eki-transformer"
