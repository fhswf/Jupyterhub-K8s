FROM jupyterhub/k8s-hub:2.0.0

ENV PYTHONUNBUFFERED=1

USER root

RUN mkdir -p /usr/local/etc/jupyterhub/jupyterhub_config.d

COPY _static_extra_config.py /usr/local/etc/jupyterhub/jupyterhub_config.d/_static_extra_config.py

USER ${NB_USER}

RUN pip install \
    oauthenticator \
    jupyterhub-ltiauthenticator \
    git+https://github.com/fhswf/Jupyterhub-K8s.git@1-multiauth-package#subdirectory=packages/MultiAuthenticator \
    nbgitpuller 