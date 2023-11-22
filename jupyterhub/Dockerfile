FROM jupyterhub/k8s-hub:2.0.1-0.dev.git.6026.h0e7347d7
# latest version for jupyterhub 3.1.1  2.0.1-0.dev.git.6026.h0e7347d7
# latest version for jupyterhub 3.0.0  2.0.1-0.dev.git.5939.h617bec32
ENV PYTHONUNBUFFERED=1

USER root

RUN mkdir -p /usr/local/etc/jupyterhub/jupyterhub_config.d

COPY announcement_config.py /usr/local/etc/jupyterhub/jupyterhub_config.d/announcement_config.py

USER ${NB_USER}

# https://github.com/rcthomas/jupyterhub-announcement
RUN pip install \
    oauthenticator \
    jupyterhub-ltiauthenticator \
    git+https://github.com/fhswf/Jupyterhub-K8s.git@develop#subdirectory=packages/multiauthenticator \
    nbgitpuller jupyterhub-announcement PyJWT

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
