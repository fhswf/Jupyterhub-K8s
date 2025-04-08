FROM jupyterhub/k8s-hub:3.2.1 
# hub 4.0.2
# FROM jupyterhub/k8s-hub:2.0.1-0.dev.git.6026.h0e7347d

# latest version for jupyterhub 3.1.1  2.0.1-0.dev.git.6026.h0e7347d7
# latest version for jupyterhub 3.0.0  2.0.1-0.dev.git.5939.h617bec32
ENV PYTHONUNBUFFERED=1

USER root

# ensure extra dir for configs and templates
# note that this folder is loaded only by the jupyterhub_config from z2jh
# other distributions might have different locations for this
RUN mkdir -p /usr/local/etc/jupyterhub/jupyterhub_config.d
RUN mkdir -p /opt/jupyterhub/hub/templates

# extra configs for general execution
COPY general_extra_config.py /usr/local/etc/jupyterhub/jupyterhub_config.d/40_general_extra_config.py
RUN  chmod +x /usr/local/etc/jupyterhub/jupyterhub_config.d/40_general_extra_config.py
# extra config for ananake fork
# COPY lti_auth_extension.py /usr/local/etc/jupyterhub/jupyterhub_config.d/50_lti_auth_extension.py
# RUN  chmod +x /usr/local/etc/jupyterhub/jupyterhub_config.d/50_lti_auth_extension.py

USER ${NB_USER}

ADD https://api.github.com/repos/fhswf/Jupyterhub-K8s/git/refs/heads/develop Jupyterhub-K8s.version.json
ADD https://api.github.com/repos/fhswf/jupyterhub-announcement/git/refs/heads/main jupyterhub-announcement.version.json

RUN pip install \
    oauthenticator \
    jupyterhub-ltiauthenticator \
    kubernetes \
    git+https://github.com/fhswf/Jupyterhub-K8s.git@develop#subdirectory=packages/multiauthenticator \
    nbgitpuller PyJWT \
    git+https://github.com/fhswf/jupyterhub-announcement.git@main 

# ADD https://api.github.com/repos/fhswf/ngshare/git/refs/heads/master ngshare.version.json
# RUN pip install --no-deps git+https://github.com/fhswf/ngshare.git@master

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
