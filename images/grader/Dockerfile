ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-nocuda:sha-f7a5a4b
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME grader

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# note that follwing packages after nbgrader are just dependencies of it
RUN pip install --no-deps \          
    ngshare_exchange nbgrader==0.8.5 rapidfuzz hatchling>=1.10.0 editables pathspec trove-classifiers \
    && rm -rf /tmp/* $HOME/.cache

COPY nbgrader_config.py /etc/jupyter/nbgrader_config.py
RUN chmod -R 777 /etc/jupyter

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Image for nbgrader admins"
LABEL org.opencontainers.image.description="Image for nbgrader admins"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER