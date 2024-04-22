ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-cuda-devel:sha-4dd0f7a
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME deepml

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Install apt prerequisits
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    # for torch vision and huggingface nlp and opencv
    libsndfile1 ffmpeg libsm6 libxext6 libgl1 \
    # deps for nvidia nemo_toolkit 
    libsndfile1 sox libfreetype6 swig libavdevice-dev \
    && apt-get clean \
    && rm -rf /tmp/* /var/lib/apt/lists/*

# python wheels that get autocompiled when installed
RUN pip install multidict \
    && rm -rf /tmp/* $HOME/.cache \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

# This step might be required for alternative installs.
# copy libcudnn to /usr/local/cuda 
# RUN cp -P /usr/include/cudnn.h /usr/local/cuda/include
# RUN cp -P /usr/lib/x86_64-linux-gnu/libcudnn* /usr/local/cuda/lib64

# Tensor RT is now in vscode base

# JAVA 1.8 for some old projects that need this runtime
ENV JAVA_HOME /opt/java/openjdk
ENV PATH $JAVA_HOME/bin:$PATH   
ENV LC_ALL='en_US.UTF-8'
ENV JAVA_VERSION jdk8u392-b08

RUN wget -O /tmp/openjdk.tar.gz https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u392-b08/OpenJDK8U-jdk_x64_linux_hotspot_8u392b08.tar.gz \
    && mkdir -p "$JAVA_HOME" \
    && tar --extract --file /tmp/openjdk.tar.gz --directory "$JAVA_HOME"  --strip-components 1 --no-same-owner \
    && rm -f /tmp/openjdk.tar.gz ${JAVA_HOME}/lib/src.zip  \
    && find "$JAVA_HOME/lib" -name '*.so' -exec dirname '{}' ';' | sort -u > /etc/ld.so.conf.d/docker-openjdk.conf \
    && ldconfig \
    && java -Xshare:dump

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    maven \
    && apt-get clean \
    && rm -rf /tmp/* /var/lib/apt/lists/*

USER $NB_UID

# prevent TF from allocating all VRAM
ENV TF_FORCE_GPU_ALLOW_GROWTH true

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
