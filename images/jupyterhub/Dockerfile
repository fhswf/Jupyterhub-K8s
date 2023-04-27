FROM jupyterhub/k8s-hub:2.0.1-0.dev.git.6105.hb969fa50

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
