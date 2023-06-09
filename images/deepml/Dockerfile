FROM ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-cuda-cudnn:sha-d39be35

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

# Install Tensorflow deps
RUN conda install -c conda-forge cudatoolkit=11.7.0

# Install PyTorch
RUN pip install \
    torch==2.0.0+cu117 torchvision==0.15.1+cu117 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu117 \
    && rm -rf /tmp/* $HOME/.cache

# Install Huggingface libraries
RUN pip install \
    nvidia-cudnn-cu11==8.5.0.96 tensorflow==2.11.* mysql-connector-python keras-tuner pymysql \
    librosa gradio wandb Cython flair nemo_toolkit[all] \
    transformers datasets metrics tokenizers evaluate adapter-transformers diffusers[torch] accelerate \
    spacy nltk gensim rasa jiwer audiofile \
    && rm -rf /tmp/* $HOME/.cache


LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="deepml-cuda"
LABEL ki.fh-swf.de.jupyterhub.description="Multipurpose Deep Learning image with cuda"
LABEL org.opencontainers.image.description="Multipurpose Deep Learning image with cuda"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"