FROM jupyterhub/k8s-hub:2.0.0

ENV PYTHONUNBUFFERED=1

COPY . ./

USER root

RUN mkdir -p /usr/local/etc/jupyterhub/jupyterhub_config.d

COPY _static_extra_config.py /usr/local/etc/jupyterhub/jupyterhub_config.d/_static_extra_config.py

USER ${NB_USER}

RUN pip install .

RUN pip install \
    nbgitpuller 
