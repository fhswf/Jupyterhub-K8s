FROM jupyter/minimal-notebook as minimal-cuda-base

LABEL maintainer "Fachhochschule Südwestfalen"

USER root

ENV NVARCH x86_64
ENV CUDA_VERSION 11.7.1
ENV NVIDIA_REQUIRE_CUDA "cuda>=12.1 brand=tesla,driver>=450,driver<451 brand=tesla,driver>=470,driver<471 brand=unknown,driver>=470,driver<471 brand=nvidia,driver>=470,driver<471 brand=nvidiartx,driver>=470,driver<471 brand=geforce,driver>=470,driver<471 brand=geforcertx,driver>=470,driver<471 brand=quadro,driver>=470,driver<471 brand=quadrortx,driver>=470,driver<471 brand=titan,driver>=470,driver<471 brand=titanrtx,driver>=470,driver<471 brand=tesla,driver>=510,driver<511 brand=unknown,driver>=510,driver<511 brand=nvidia,driver>=510,driver<511 brand=nvidiartx,driver>=510,driver<511 brand=geforce,driver>=510,driver<511 brand=geforcertx,driver>=510,driver<511 brand=quadro,driver>=510,driver<511 brand=quadrortx,driver>=510,driver<511 brand=titan,driver>=510,driver<511 brand=titanrtx,driver>=510,driver<511 brand=tesla,driver>=515,driver<516 brand=unknown,driver>=515,driver<516 brand=nvidia,driver>=515,driver<516 brand=nvidiartx,driver>=515,driver<516 brand=geforce,driver>=515,driver<516 brand=geforcertx,driver>=515,driver<516 brand=quadro,driver>=515,driver<516 brand=quadrortx,driver>=515,driver<516 brand=titan,driver>=515,driver<516 brand=titanrtx,driver>=515,driver<516 brand=tesla,driver>=525,driver<526 brand=unknown,driver>=525,driver<526 brand=nvidia,driver>=525,driver<526 brand=nvidiartx,driver>=525,driver<526 brand=geforce,driver>=525,driver<526 brand=geforcertx,driver>=525,driver<526 brand=quadro,driver>=525,driver<526 brand=quadrortx,driver>=525,driver<526 brand=titan,driver>=525,driver<526 brand=titanrtx,driver>=525,driver<526"
ENV NV_CUDA_COMPAT_PACKAGE cuda-compat-12-1


RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg2 curl ca-certificates && \
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/${NVARCH}/3bf863cc.pub | apt-key add - && \
    echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/${NVARCH} /" > /etc/apt/sources.list.d/cuda.list && \
    apt-get purge --autoremove -y curl \
    && rm -rf /var/lib/apt/lists/*


# For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-cudart-11-7 \
    ${NV_CUDA_COMPAT_PACKAGE} \
    && rm -rf /var/lib/apt/lists/*

# Required for nvidia-docker v1
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf \
    && echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

# use compat package
# ENV LD_LIBRARY_PATH=/usr/local/cuda/compat:$LD_LIBRARY_PATH

ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64

COPY NVIDIA_LICENSE /

# trigger for nvidia-container-runtime 
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

FROM minimal-cuda-base as minimal-cuda-runtime

ENV NV_CUDA_LIB_VERSION 11.7.1-1

ENV NV_NVTX_VERSION 11.7.91-1
ENV NV_LIBNPP_VERSION 11.7.4.75-1
ENV NV_LIBNPP_PACKAGE libnpp-11-7=${NV_LIBNPP_VERSION}
ENV NV_LIBCUSPARSE_VERSION 11.7.4.91-1

ENV NV_LIBCUBLAS_PACKAGE_NAME libcublas-11-7
ENV NV_LIBCUBLAS_VERSION 11.10.3.66-1
ENV NV_LIBCUBLAS_PACKAGE ${NV_LIBCUBLAS_PACKAGE_NAME}=${NV_LIBCUBLAS_VERSION}

ENV NV_LIBNCCL_PACKAGE_NAME libnccl2
ENV NV_LIBNCCL_PACKAGE_VERSION 2.13.4-1
ENV NCCL_VERSION 2.13.4-1
ENV NV_LIBNCCL_PACKAGE ${NV_LIBNCCL_PACKAGE_NAME}=${NV_LIBNCCL_PACKAGE_VERSION}+cuda11.7

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-11-7=${NV_CUDA_LIB_VERSION} \
    ${NV_LIBNPP_PACKAGE} \
    cuda-nvtx-11-7=${NV_NVTX_VERSION} \
    libcusparse-11-7=${NV_LIBCUSPARSE_VERSION} \
    ${NV_LIBCUBLAS_PACKAGE} \
    ${NV_LIBNCCL_PACKAGE} \
    && rm -rf /var/lib/apt/lists/*

# Keep apt from auto upgrading the cublas and nccl packages. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold ${NV_LIBCUBLAS_PACKAGE_NAME} ${NV_LIBNCCL_PACKAGE_NAME}

FROM minimal-cuda-base as minimal-cuda-cudnn

ENV NV_CUDNN_VERSION 8.5.0.96
ENV NV_CUDNN_PACKAGE_NAME "libcudnn8"

ENV NV_CUDNN_PACKAGE "libcudnn8=$NV_CUDNN_VERSION-1+cuda11.7"

LABEL com.nvidia.cudnn.version="${NV_CUDNN_VERSION}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    ${NV_CUDNN_PACKAGE} \
    && apt-mark hold ${NV_CUDNN_PACKAGE_NAME} \
    && rm -rf /var/lib/apt/lists/*

ENV LD_LIBRARY_PATH=${CONDA_DIR}/lib/:${LD_LIBRARY_PATH}
RUN echo LD_LIBRARY_PATH="${LD_LIBRARY_PATH}" >> /etc/environment 
ENV CPATH=$CONDA_DIR/include
RUN echo CPATH="${CPATH}" >> /etc/environment

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    htop \
    wget \
    curl \
    openssh-client \
    iputils-ping \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#  Code Server server-proxy/vscode-proxy from https://coder.com/docs/code-server/latest
ENV CODE_VERSION=4.12.0
ENV CODE_BUILTIN_EXTENSIONS_DIR=/opt/code-server/lib/vscode/extensions

ENV PATH=/opt/code-server/bin:$PATH \
    CS_DISABLE_GETTING_STARTED_OVERRIDE=1

RUN mkdir -m 1777 /opt/code-server \
    && cd /tmp \
    && curl -fOL https://github.com/coder/code-server/releases/download/v${CODE_VERSION}/code-server_${CODE_VERSION}_amd64.deb \
    && curl -sL https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg -o vscode.svg \
    && dpkg -i code-server_${CODE_VERSION}_amd64.deb \
    && rm -f code-server_${CODE_VERSION}_amd64.deb \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension GitHub.copilot \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension ms-python.python \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension ms-python.vscode-pylance \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension ms-toolsai.jupyter \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension VisualStudioExptTeam.vscodeintellicode \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension ms-toolsai.vscode-jupyter-cell-tags \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension ms-vscode-remote.remote-ssh \ 
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension redhat.vscode-yaml \ 
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension donjayamanne.githistory \ 
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension alefragnani.project-manager \ 
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension humao.rest-client \ 
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension esbenp.prettier-vscode \ 
    ## Create folders temp and tmp for Jupyter extension
    && cd /opt/code-server/lib/vscode/extensions/ms-toolsai.jupyter-* \
    && mkdir -m 1777 temp \
    && mkdir -m 1777 tmp \
    && rm -rf /tmp/* \
       $HOME/.config \
       $HOME/.local

RUN /opt/conda/bin/conda install -c conda-forge jupyter-server-proxy
RUN /opt/conda/bin/conda install -c conda-forge jupyter-vscode-proxy

RUN pip install nbgitpuller scilab-kernel \
    && rm -rf /tmp/* $HOME/.cache

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="minimal-notebook-cuda"
LABEL ki.fh-swf.de.jupyterhub.description="Based on the original jupyterlab minimal-notebook with cuda and cudnn."
LABEL org.opencontainers.image.description="Based on the original jupyterlab minimal-notebook with cuda and cudnn."
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
