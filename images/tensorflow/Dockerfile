FROM ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-cuda-cudnn:sha-d39be35

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN conda install -c conda-forge cudatoolkit=11.7.0

RUN python3 -m pip install nvidia-cudnn-cu11==8.5.0.96 tensorflow==2.11.* mysql-connector-python keras-tuner pymysql \
    && rm -rf /tmp/* $HOME/.cache

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="tf-notebook-cuda"
LABEL ki.fh-swf.de.jupyterhub.description="Tensorflow/Keras with cuda"
LABEL org.opencontainers.image.description="Tensorflow/Keras with cuda"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"