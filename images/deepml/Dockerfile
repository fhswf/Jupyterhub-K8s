FROM ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-cuda-devel:sha-d11cf9b

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

# In the Ubuntu 16.04 images, cudnn is placed in system paths. Move them to
# /usr/local/cuda
RUN cp -P /usr/include/cudnn.h /usr/local/cuda/include
RUN cp -P /usr/lib/x86_64-linux-gnu/libcudnn* /usr/local/cuda/lib64
    
# Installs TensorRT
RUN apt-get update \
    && apt-get install nvinfer-runtime-trt-repo-ubuntu1604-5.0.2-ga-cuda10.0 \
    && apt-get update \
    && apt-get install -y --no-install-recommends libnvinfer5=5.0.2-1+cuda10.0 libnvinfer-dev=5.0.2-1+cuda10.0

## Install Tensorflow deps
# this is not required for devel packages
#RUN conda install -c conda-forge cudatoolkit=11.7.0
#RUN conda install -c "nvidia/label/cuda-11.7.0" cuda-nvcc

# Install PyTorch
RUN pip install \
    torch==2.0.0+cu117 torchvision==0.15.1+cu117 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu117 \
    && rm -rf /tmp/* $HOME/.cache

# Install Huggingface libraries
RUN pip install \
    nvidia-cudnn-cu11==8.5.0.96 tensorflow==2.11.* mysql-connector-python keras-tuner pymysql \
    librosa gradio wandb Cython flair nemo_toolkit[all] \
    transformers datasets metrics tokenizers evaluate adapter-transformers diffusers[torch] accelerate \
    spacy nltk gensim jiwer audiofile \
    && rm -rf /tmp/* $HOME/.cache

# see here: https://github.com/tensorflow/tensorflow/issues/58681
# bugfix for ${CUDA_DIR}/nvvm/libdevice.

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="deepml-cuda"
LABEL ki.fh-swf.de.jupyterhub.description="Multipurpose Deep Learning image with cuda"
LABEL org.opencontainers.image.description="Multipurpose Deep Learning image with cuda"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"