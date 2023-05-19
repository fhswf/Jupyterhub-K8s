FROM ghcr.io/fhswf/jupyterhub-k8s/scipy-notebook-cuda

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# pytorch1x should also work on pytorch2 
RUN conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.7 -c pytorch -c nvidia

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="torch-notebook-cuda"
LABEL ki.fh-swf.de.jupyterhub.description="PyTorch with cuda"
LABEL org.opencontainers.image.description="PyTorch with cuda"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"