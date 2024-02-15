ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-nocuda:sha-4dd0f7a
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME eml

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

USER $NB_UID

# Install PYthon Libs
RUN pip install \
    matplotlib beautifulsoup4 wikipedia-api nose numpy pandas pydot requests seaborn \
    scikit-learn tensorflow wget csv datetime gzip io math random tarfile time urllib3 \
    && rm -rf /tmp/* $HOME/.cache

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Einfuehrung ML"
LABEL org.opencontainers.image.description="Einfuehrung ML"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER
