ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/deepml:sha-dbf2e1e
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME eki

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Install apt prerequisits
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    # for torch vision and huggingface nlp
    libsndfile1 ffmpeg \
    # deps for nvidia nemo_toolkit 
    libsndfile1 sox libfreetype6 swig libavdevice-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# python wheels that get autocompiled when installed
RUN pip install multidict \
    && rm -rf /tmp/* $HOME/.cache \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

USER $NB_UID

# Install PyTorch
RUN pip install \
    torch==2.0.0+cu117 torchvision==0.15.1+cu117 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu117 \
    && rm -rf /tmp/* $HOME/.cache

COPY userscripts.sh /usr/local/bin/before-notebook.d/999_userscripts.sh
RUN  chmod +x /usr/local/bin/before-notebook.d/999_userscripts.sh

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Image for AI Model Quantization"
LABEL org.opencontainers.image.description="Image for AI Model Quantization"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER

LABEL ki.fh-swf.de.jupyterhub.project="eki-transformer"
