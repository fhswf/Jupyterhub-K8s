FROM ghcr.io/fhswf/Jupyterhub-K8s/scipy-cuda

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# pytorch1x should also work on pytorch2 
RUN conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.7 -c pytorch -c nvidia


