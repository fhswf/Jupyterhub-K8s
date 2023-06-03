FROM ghcr.io/fhswf/jupyterhub-k8s/vscode-minimal-nocuda:sha-d39be35

RUN pip install bash_kernel \
    && python -m bash_kernel.install \
    && rm -rf /tmp/* $HOME/.cache

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="deepml-notebook-cuda"
LABEL ki.fh-swf.de.jupyterhub.description="Multipurpose DeepLearning Image with cuda"
LABEL org.opencontainers.image.description="Multipurpose DeepLearning Image with cuda"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"