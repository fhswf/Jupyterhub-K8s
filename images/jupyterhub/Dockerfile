FROM jupyterhub/k8s-hub:2.0.0

ENV PYTHONUNBUFFERED=1

USER root

RUN mkdir -p /usr/local/etc/jupyterhub/jupyterhub_config.d

USER ${NB_USER}

RUN pip install \
    oauthenticator \
    jupyterhub-ltiauthenticator \
    git+https://github.com/fhswf/Jupyterhub-K8s.git@develop#subdirectory=packages/multiauthenticator \
    nbgitpuller 

LABEL fhswf.kicluster="test-label-content"
