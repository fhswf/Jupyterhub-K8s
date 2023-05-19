FROM ghcr.io/fhswf/Jupyterhub-K8s/scipy-notebook-cuda

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# pytorch1x should also work on pytorch2 
RUN conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.7 -c pytorch -c nvidia


LABEL fhswf.jupyterhub.runtime="CPU"
LABEL fhswf.jupyterhub.namelabel="Generic vscode-server example"
LABEL fhswf.jupyterhub.description="Generic vscode-server example for jupyterhub"
LABEL org.opencontainers.image.description="Generic vscode-server example for jupyterhub"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"