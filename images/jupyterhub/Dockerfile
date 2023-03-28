FROM jupyterhub/k8s-hub:latest

ENV PYTHONUNBUFFERED=1

COPY . ./

RUN mkdir -p /usr/local/etc/jupyterhub/jupyterhub_config.d

COPY jupyterhub_extra_config.py /usr/local/etc/jupyterhub/jupyterhub_config.d/jupyterhub_extra_config.py

RUN pip install .

RUN pip install \
    nbgitpuller \
    nb_conda_kernels
