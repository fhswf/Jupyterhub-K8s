ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-cuda-devel:sha-bb4d64b
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME deepml

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

# This step might be required for alternative installs.
# copy libcudnn to /usr/local/cuda 
# RUN cp -P /usr/include/cudnn.h /usr/local/cuda/include
# RUN cp -P /usr/lib/x86_64-linux-gnu/libcudnn* /usr/local/cuda/lib64

# Install TensorRT
# our current configuration does not support any tensorrt version
# we have to upgrade cuda
#ENV TRT_VERSION 8.4.3.1-1+cuda11.6
#ENV LIBINFER_VERSION 8.4.3-1+cuda11.6
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends \
#    libnvinfer-plugin8=${LIBINFER_VERSION} \
#    libnvonnxparsers8=${LIBINFER_VERSION} \
#    libnvparsers8=${LIBINFER_VERSION} \
#    libnvinfer-plugin-dev=${LIBINFER_VERSION} \
#    libnvparsers-dev=${LIBINFER_VERSION} \
#    libnvonnxparsers-dev=${LIBINFER_VERSION} \
#    libcudnn8-dev=8.5.0.96-1+cuda11.7 \
#    libnvinfer8=${LIBINFER_VERSION} \ 
#    tensorrt-dev=${TRT_VERSION} \
#    libnvinfer-dev=${LIBINFER_VERSION} \
#    && apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Install PyTorch
RUN pip install \
    torch==2.0.0+cu117 torchvision==0.15.1+cu117 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu117 \
    && rm -rf /tmp/* $HOME/.cache

# Install Huggingface tensorflow and other libraries
RUN pip install \
    nvidia-cudnn-cu11==8.5.0.96 tensorflow==2.11.* mysql-connector-python keras-tuner pymysql \
    librosa gradio wandb Cython flair \ 
    transformers datasets tokenizers evaluate adapter-transformers diffusers[torch] accelerate \
    spacy nltk gensim jiwer audiofile opencv-python tiktoken \
    && rm -rf /tmp/* $HOME/.cache

# optional stuff not included currently
# nemo_toolkit[all] 

# see here: https://github.com/tensorflow/tensorflow/issues/58681
# bugfix for ${CUDA_DIR}/nvvm/libdevice.

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Multipurpose Deep Learning image with cuda"
LABEL org.opencontainers.image.description="Multipurpose Deep Learning image with cuda"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER