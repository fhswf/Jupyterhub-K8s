ARG JUPYTER_VARIANT
ARG CUDA_VARIANT

FROM jupyter/${JUPYTER_VARIANT}-notebook:lab-3.6.3 as nocuda

ARG JUPYTER_VARIANT
ARG CUDA_VARIANT
ENV BUILD_CUDA_VARIANT=$CUDA_VARIANT
ENV BUILD_JUPYTER_VARIANT=$JUPYTER_VARIANT
ENV BUILD_IMAGE_NAME vscode-${BUILD_JUPYTER_VARIANT}-${BUILD_CUDA_VARIANT}

LABEL maintainer "Fachhochschule Südwestfalen"
LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="jupyter/${BUILD_JUPYTER_VARIANT}-notebook"
LABEL ki.fh-swf.de.jupyterhub.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook"
LABEL org.opencontainers.image.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"

###############
#  cuda 
###############
FROM nocuda as cuda

USER root

ENV NVARCH x86_64
ENV CUDA_VERSION 11.7.1

ENV NVIDIA_REQUIRE_CUDA "cuda>=12.5 brand=unknown,driver>=470,driver<471 brand=grid,driver>=470,driver<471 brand=tesla,driver>=470,driver<471 brand=nvidia,driver>=470,driver<471 brand=quadro,driver>=470,driver<471 brand=quadrortx,driver>=470,driver<471 brand=nvidiartx,driver>=470,driver<471 brand=vapps,driver>=470,driver<471 brand=vpc,driver>=470,driver<471 brand=vcs,driver>=470,driver<471 brand=vws,driver>=470,driver<471 brand=cloudgaming,driver>=470,driver<471 brand=unknown,driver>=535,driver<536 brand=grid,driver>=535,driver<536 brand=tesla,driver>=535,driver<536 brand=nvidia,driver>=535,driver<536 brand=quadro,driver>=535,driver<536 brand=quadrortx,driver>=535,driver<536 brand=nvidiartx,driver>=535,driver<536 brand=vapps,driver>=535,driver<536 brand=vpc,driver>=535,driver<536 brand=vcs,driver>=535,driver<536 brand=vws,driver>=535,driver<536 brand=cloudgaming,driver>=535,driver<536 brand=unknown,driver>=550,driver<551 brand=grid,driver>=550,driver<551 brand=tesla,driver>=550,driver<551 brand=nvidia,driver>=550,driver<551 brand=quadro,driver>=550,driver<551 brand=quadrortx,driver>=550,driver<551 brand=nvidiartx,driver>=550,driver<551 brand=vapps,driver>=550,driver<551 brand=vpc,driver>=550,driver<551 brand=vcs,driver>=550,driver<551 brand=vws,driver>=550,driver<551 brand=cloudgaming,driver>=550,driver<551"
ENV NV_CUDA_CUDART_VERSION 12.5.82-1
#ENV NVIDIA_REQUIRE_CUDA "cuda>=12.1 brand=tesla,driver>=450,driver<451 brand=tesla,driver>=470,driver<471 brand=unknown,driver>=470,driver<471 brand=nvidia,driver>=470,driver<471 brand=nvidiartx,driver>=470,driver<471 brand=geforce,driver>=470,driver<471 brand=geforcertx,driver>=470,driver<471 brand=quadro,driver>=470,driver<471 brand=quadrortx,driver>=470,driver<471 brand=titan,driver>=470,driver<471 brand=titanrtx,driver>=470,driver<471 brand=tesla,driver>=510,driver<511 brand=unknown,driver>=510,driver<511 brand=nvidia,driver>=510,driver<511 brand=nvidiartx,driver>=510,driver<511 brand=geforce,driver>=510,driver<511 brand=geforcertx,driver>=510,driver<511 brand=quadro,driver>=510,driver<511 brand=quadrortx,driver>=510,driver<511 brand=titan,driver>=510,driver<511 brand=titanrtx,driver>=510,driver<511 brand=tesla,driver>=515,driver<516 brand=unknown,driver>=515,driver<516 brand=nvidia,driver>=515,driver<516 brand=nvidiartx,driver>=515,driver<516 brand=geforce,driver>=515,driver<516 brand=geforcertx,driver>=515,driver<516 brand=quadro,driver>=515,driver<516 brand=quadrortx,driver>=515,driver<516 brand=titan,driver>=515,driver<516 brand=titanrtx,driver>=515,driver<516 brand=tesla,driver>=525,driver<526 brand=unknown,driver>=525,driver<526 brand=nvidia,driver>=525,driver<526 brand=nvidiartx,driver>=525,driver<526 brand=geforce,driver>=525,driver<526 brand=geforcertx,driver>=525,driver<526 brand=quadro,driver>=525,driver<526 brand=quadrortx,driver>=525,driver<526 brand=titan,driver>=525,driver<526 brand=titanrtx,driver>=525,driver<526"
#ENV NV_CUDA_COMPAT_PACKAGE cuda-compat-12-1

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    gnupg2 curl ca-certificates && \
#    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/${NVARCH}/3bf863cc.pub | apt-key add - && \
#    echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/${NVARCH} /" > /etc/apt/sources.list.d/cuda.list && \
#    apt-get purge --autoremove -y curl \
#    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg2 curl ca-certificates && \
    curl -fsSLO https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/${NVARCH}/cuda-keyring_1.1-1_all.deb && \
    dpkg -i cuda-keyring_1.1-1_all.deb && \
    apt-get purge --autoremove -y curl \
    && rm -rf /var/lib/apt/lists/*

## For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    cuda-cudart-11-7 \
#    ${NV_CUDA_COMPAT_PACKAGE} \
#    && rm -rf /var/lib/apt/lists/*
# For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-cudart-12-5=${NV_CUDA_CUDART_VERSION} \
    cuda-compat-12-5 \
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

USER $NB_UID

# extra nvidia tools (nvidia-ml-py is wrapper for nvml c-library)
RUN pip install nvidia-ml-py \
    && rm -rf /tmp/* $HOME/.cache

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.cuda="${BUILD_CUDA_VARIANT}"
LABEL ki.fh-swf.de.jupyterhub.namelabel="${BUILD_JUPYTER_VARIANT}-${BUILD_CUDA_VARIANT}"
LABEL ki.fh-swf.de.jupyterhub.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook with ${BUILD_CUDA_VARIANT}."
LABEL org.opencontainers.image.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook with ${BUILD_CUDA_VARIANT}."


###############
#  cuda-runtime 
###############
FROM cuda as cuda-runtime

USER root

#ENV NV_CUDA_LIB_VERSION 11.7.1-1
ENV NV_CUDA_LIB_VERSION 12.5.1-1

#ENV NV_NVTX_VERSION 11.7.91-1
#ENV NV_LIBNPP_VERSION 11.7.4.75-1
#ENV NV_LIBNPP_PACKAGE libnpp-11-7=${NV_LIBNPP_VERSION}
#ENV NV_LIBCUSPARSE_VERSION 11.7.4.91-1
ENV NV_NVTX_VERSION 12.5.82-1
ENV NV_LIBNPP_VERSION 12.3.0.159-1
ENV NV_LIBNPP_PACKAGE libnpp-12-5=${NV_LIBNPP_VERSION}
ENV NV_LIBCUSPARSE_VERSION 12.5.1.3-1

#ENV NV_LIBCUBLAS_PACKAGE_NAME libcublas-11-7
#ENV NV_LIBCUBLAS_VERSION 11.10.3.66-1
#ENV NV_LIBCUBLAS_PACKAGE ${NV_LIBCUBLAS_PACKAGE_NAME}=${NV_LIBCUBLAS_VERSION}
ENV NV_LIBCUBLAS_PACKAGE_NAME libcublas-12-5
ENV NV_LIBCUBLAS_VERSION 12.5.3.2-1
ENV NV_LIBCUBLAS_PACKAGE ${NV_LIBCUBLAS_PACKAGE_NAME}=${NV_LIBCUBLAS_VERSION}

#ENV NV_LIBNCCL_PACKAGE_NAME libnccl2
#ENV NV_LIBNCCL_PACKAGE_VERSION 2.13.4-1
#ENV NCCL_VERSION 2.13.4-1
#ENV NV_LIBNCCL_PACKAGE ${NV_LIBNCCL_PACKAGE_NAME}=${NV_LIBNCCL_PACKAGE_VERSION}+cuda11.7
ENV NV_LIBNCCL_PACKAGE_NAME libnccl2
ENV NV_LIBNCCL_PACKAGE_VERSION 2.22.3-1
ENV NCCL_VERSION 2.22.3-1
ENV NV_LIBNCCL_PACKAGE ${NV_LIBNCCL_PACKAGE_NAME}=${NV_LIBNCCL_PACKAGE_VERSION}+cuda12.5

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    cuda-libraries-11-7=${NV_CUDA_LIB_VERSION} \
#    ${NV_LIBNPP_PACKAGE} \
#    cuda-nvtx-11-7=${NV_NVTX_VERSION} \
#    libcusparse-11-7=${NV_LIBCUSPARSE_VERSION} \
#    ${NV_LIBCUBLAS_PACKAGE} \
#    ${NV_LIBNCCL_PACKAGE} \
#    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-12-5=${NV_CUDA_LIB_VERSION} \
    ${NV_LIBNPP_PACKAGE} \
    cuda-nvtx-12-5=${NV_NVTX_VERSION} \
    libcusparse-12-5=${NV_LIBCUSPARSE_VERSION} \
    ${NV_LIBCUBLAS_PACKAGE} \
    ${NV_LIBNCCL_PACKAGE} \
    && rm -rf /var/lib/apt/lists/*

# Keep apt from auto upgrading the cublas and nccl packages. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
#RUN apt-mark hold ${NV_LIBCUBLAS_PACKAGE_NAME} ${NV_LIBNCCL_PACKAGE_NAME}
RUN apt-mark hold ${NV_LIBCUBLAS_PACKAGE_NAME} ${NV_LIBNCCL_PACKAGE_NAME}

LABEL ki.fh-swf.de.jupyterhub.namelabel="${BUILD_JUPYTER_VARIANT}-${BUILD_CUDA_VARIANT}"
LABEL ki.fh-swf.de.jupyterhub.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook with ${BUILD_CUDA_VARIANT}."
LABEL org.opencontainers.image.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook with ${BUILD_CUDA_VARIANT}."
LABEL ki.fh-swf.de.jupyterhub.runtime.cudnn="${NV_CUDNN_VERSION}"

USER $NB_UID

###############
#  cuda-cudnn 
###############
FROM cuda-runtime as cuda-cudnn

USER root

#ENV NV_CUDNN_VERSION 8.5.0.96
#ENV NV_CUDNN_PACKAGE_NAME "libcudnn8"
#ENV NV_CUDNN_PACKAGE "libcudnn8=$NV_CUDNN_VERSION-1+cuda11.7"

ENV NV_CUDNN_VERSION 9.2.1.18-1
ENV NV_CUDNN_PACKAGE_NAME libcudnn9-cuda-12
ENV NV_CUDNN_PACKAGE libcudnn9-cuda-12=${NV_CUDNN_VERSION}

LABEL com.nvidia.cudnn.version="${NV_CUDNN_VERSION}"

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    ${NV_CUDNN_PACKAGE} \
#    && apt-mark hold ${NV_CUDNN_PACKAGE_NAME} \
#    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y --no-install-recommends \
    ${NV_CUDNN_PACKAGE} \
    && apt-mark hold ${NV_CUDNN_PACKAGE_NAME} \
    && rm -rf /var/lib/apt/lists/*


# conda LD_LIBRARY_PATH contains conflicting packages 
#ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${CONDA_DIR}/lib/
RUN echo LD_LIBRARY_PATH="${LD_LIBRARY_PATH}" >> /etc/environment 
ENV CPATH=$CONDA_DIR/include
RUN echo CPATH="${CPATH}" >> /etc/environment

#RUN dpkg -i nv-tensorrt-local-repo-${OS_RELEASE}-${NV_TENSOR_RT_TAG}_1.0-1_amd64.deb
#    && cp /var/nv-tensorrt-local-repo-${OS_RELEASE}-${NV_TENSOR_RT_TAG}/*-keyring.gpg /usr/share/keyrings/
#    && apt-get update
#
#RUN apt-get install tensorrt
#    && apt-get install python3-libnvinfer-dev

LABEL ki.fh-swf.de.jupyterhub.namelabel="${BUILD_JUPYTER_VARIANT}-${BUILD_CUDA_VARIANT}"
LABEL ki.fh-swf.de.jupyterhub.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook with ${BUILD_CUDA_VARIANT}."
LABEL org.opencontainers.image.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook with ${BUILD_CUDA_VARIANT}."
LABEL ki.fh-swf.de.jupyterhub.runtime.cudnn="${NV_CUDNN_VERSION}"

USER $NB_UID

###############
# cuda-devel
###############

FROM cuda-cudnn as cuda-devel

USER root

ENV NV_CUDA_LIB_VERSION "12.5.1-1"

#ENV NV_CUDA_CUDART_DEV_VERSION 11.7.99-1
#ENV NV_NVML_DEV_VERSION 11.7.91-1
#ENV NV_LIBCUSPARSE_DEV_VERSION 11.7.4.91-1
#ENV NV_LIBNPP_DEV_VERSION 11.7.4.75-1
#ENV NV_LIBNPP_DEV_PACKAGE libnpp-dev-11-7=${NV_LIBNPP_DEV_VERSION}
ENV NV_CUDA_CUDART_DEV_VERSION 12.5.82-1
ENV NV_NVML_DEV_VERSION 12.5.82-1
ENV NV_LIBCUSPARSE_DEV_VERSION 12.5.1.3-1
ENV NV_LIBNPP_DEV_VERSION 12.3.0.159-1
ENV NV_LIBNPP_DEV_PACKAGE libnpp-dev-12-5=${NV_LIBNPP_DEV_VERSION}

#ENV NV_LIBCUBLAS_DEV_VERSION 11.10.3.66-1
#ENV NV_LIBCUBLAS_DEV_PACKAGE_NAME libcublas-dev-11-7
#ENV NV_LIBCUBLAS_DEV_PACKAGE ${NV_LIBCUBLAS_DEV_PACKAGE_NAME}=${NV_LIBCUBLAS_DEV_VERSION}
ENV NV_LIBCUBLAS_DEV_VERSION 12.5.3.2-1
ENV NV_LIBCUBLAS_DEV_PACKAGE_NAME libcublas-dev-12-5
ENV NV_LIBCUBLAS_DEV_PACKAGE ${NV_LIBCUBLAS_DEV_PACKAGE_NAME}=${NV_LIBCUBLAS_DEV_VERSION}

#ENV NV_NVPROF_VERSION 11.7.101-1
#ENV NV_NVPROF_DEV_PACKAGE cuda-nvprof-11-7=${NV_NVPROF_VERSION}
ENV NV_CUDA_NSIGHT_COMPUTE_VERSION 12.5.1-1
ENV NV_CUDA_NSIGHT_COMPUTE_DEV_PACKAGE cuda-nsight-compute-12-5=${NV_CUDA_NSIGHT_COMPUTE_VERSION}

ENV NV_NVPROF_VERSION 12.5.82-1
ENV NV_NVPROF_DEV_PACKAGE cuda-nvprof-12-5=${NV_NVPROF_VERSION}

#ENV NV_LIBNCCL_DEV_PACKAGE_NAME libnccl-dev
#ENV NV_LIBNCCL_DEV_PACKAGE_VERSION 2.13.4-1
#ENV NCCL_VERSION 2.13.4-1
#ENV NV_LIBNCCL_DEV_PACKAGE ${NV_LIBNCCL_DEV_PACKAGE_NAME}=${NV_LIBNCCL_DEV_PACKAGE_VERSION}+cuda11.7
ENV NV_LIBNCCL_DEV_PACKAGE_NAME libnccl-dev
ENV NV_LIBNCCL_DEV_PACKAGE_VERSION 2.22.3-1
ENV NCCL_VERSION 2.22.3-1
ENV NV_LIBNCCL_DEV_PACKAGE ${NV_LIBNCCL_DEV_PACKAGE_NAME}=${NV_LIBNCCL_DEV_PACKAGE_VERSION}+cuda12.5

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    libtinfo5 libncursesw5 \
#    cuda-cudart-dev-11-7=${NV_CUDA_CUDART_DEV_VERSION} \
#    cuda-command-line-tools-11-7=${NV_CUDA_LIB_VERSION} \
#    cuda-minimal-build-11-7=${NV_CUDA_LIB_VERSION} \
#    cuda-libraries-dev-11-7=${NV_CUDA_LIB_VERSION} \
#    cuda-nvml-dev-11-7=${NV_NVML_DEV_VERSION} \
#    ${NV_NVPROF_DEV_PACKAGE} \
#    ${NV_LIBNPP_DEV_PACKAGE} \
#    libcusparse-dev-11-7=${NV_LIBCUSPARSE_DEV_VERSION} \
#    ${NV_LIBCUBLAS_DEV_PACKAGE} \
#    ${NV_LIBNCCL_DEV_PACKAGE} \
#    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-cudart-dev-12-5=${NV_CUDA_CUDART_DEV_VERSION} \
    cuda-command-line-tools-12-5=${NV_CUDA_LIB_VERSION} \
    cuda-minimal-build-12-5=${NV_CUDA_LIB_VERSION} \
    cuda-libraries-dev-12-5=${NV_CUDA_LIB_VERSION} \
    cuda-nvml-dev-12-5=${NV_NVML_DEV_VERSION} \
    ${NV_NVPROF_DEV_PACKAGE} \
    ${NV_LIBNPP_DEV_PACKAGE} \
    libcusparse-dev-12-5=${NV_LIBCUSPARSE_DEV_VERSION} \
    ${NV_LIBCUBLAS_DEV_PACKAGE} \
    ${NV_LIBNCCL_DEV_PACKAGE} \
    ${NV_CUDA_NSIGHT_COMPUTE_DEV_PACKAGE} \
    && rm -rf /var/lib/apt/lists/*

# cudnn devel
ENV NV_CUDNN_VERSION 9.2.1.18-1
ENV NV_CUDNN_PACKAGE_NAME libcudnn9-cuda-12
ENV NV_CUDNN_PACKAGE libcudnn9-cuda-12=${NV_CUDNN_VERSION}
ENV NV_CUDNN_PACKAGE_DEV libcudnn9-dev-cuda-12=${NV_CUDNN_VERSION}

RUN apt-get update && apt-get install -y --no-install-recommends \
    ${NV_CUDNN_PACKAGE} \
    ${NV_CUDNN_PACKAGE_DEV} \
    && apt-mark hold ${NV_CUDNN_PACKAGE_NAME} \
    && rm -rf /var/lib/apt/lists/*

# extra Install TensorRT
#ENV NV_TRT_VERSION 8.5.3
ENV NV_TRT_VERSION 10.3.0
# version="10.x.x.x-1+cudax.x"
#ENV NV_TENSOR_RT_TAG 8.5.3-1+cuda11.8 
ENV NV_TENSOR_RT_TAG 10.3.0-1+cuda12.5 
ENV OS_RELEASE ubuntu2204

# easy repo add
RUN apt-get update && apt-get install -y software-properties-common 

## Theese might change unexpectedly
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
RUN mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/7fa2af80.pub
RUN apt-get update && apt-get install -y --no-install-recommends gnupg2 curl ca-certificates
RUN curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x536F8F1DE80F6A35' | gpg --import
RUN curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xA4B469963BF863CC' | gpg --import
RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"
RUN apt-get update
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"
RUN apt-get update

#RUN apt-get install -y libcudnn8-dev=8.5.0.96-1+cuda11.7
#RUN apt-get install -y libnvinfer8=${NV_TENSOR_RT_TAG} \
#    libnvinfer-plugin8=${NV_TENSOR_RT_TAG} \
#    libnvinfer-dev=${NV_TENSOR_RT_TAG} \
#    libnvinfer-plugin-dev=${NV_TENSOR_RT_TAG} \
#    libnvonnxparsers8=${NV_TENSOR_RT_TAG} \
#    libnvonnxparsers-dev=${NV_TENSOR_RT_TAG} \
#    libnvparsers8=${NV_TENSOR_RT_TAG} \
#    libnvparsers-dev=${NV_TENSOR_RT_TAG} \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

RUN apt-get install -y \
    libnvinfer-bin=${version} \
    libnvinfer-dev=${version} \
    libnvinfer-dispatch-dev=${version} \
    libnvinfer-dispatch10=${version} \
    libnvinfer-headers-dev=${version} \
    libnvinfer-headers-plugin-dev=${version} \
    libnvinfer-lean-dev=${version} \
    libnvinfer-lean10=${version} \
    libnvinfer-plugin-dev=${version} \
    libnvinfer-plugin10=${version} \
    libnvinfer-samples=${version} \
    libnvinfer-vc-plugin-dev=${version} \
    libnvinfer-vc-plugin10=${version} \
    libnvinfer10=${version} \
    libnvonnxparsers-dev=${version} \
    libnvonnxparsers10=${version} \
    python3-libnvinfer-dev=${version} \
    python3-libnvinfer-dispatch=${version} \
    python3-libnvinfer-lean=${version} \
    python3-libnvinfer=${version} \
    tensorrt-dev=${version} \
    tensorrt-libs=${version} \
    tensorrt=${version} \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# trick tf to use newer rt version
#RUN ln -s /usr/lib/x86_64-linux-gnu/libnvinfer.so.8 /usr/lib/x86_64-linux-gnu/libnvinfer.so.7 \
#    && ln -s /usr/lib/x86_64-linux-gnu/libnvinfer_plugin.so.8 /usr/lib/x86_64-linux-gnu/libnvinfer_plugin.so.7 \
#    && ln -s /usr/lib/x86_64-linux-gnu/libnvonnxparser.so.8 /usr/lib/x86_64-linux-gnu/libnvonnxparser.so.7 \
#    && ln -s /usr/lib/x86_64-linux-gnu/libnvparsers.so.8 /usr/lib/x86_64-linux-gnu/libnvparsers.so.7
#not sure if still required

# Keep apt from auto upgrading the cublas and nccl packages. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold ${NV_LIBCUBLAS_DEV_PACKAGE_NAME} ${NV_LIBNCCL_DEV_PACKAGE_NAME}
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs

USER $NB_UID

###############
#  vscode 
###############
FROM ${CUDA_VARIANT}

USER root

### VS-Code install 
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    htop \
    build-essential gcc g++ gnupg2 make less cmake \
    wget curl jq moreutils \
    openssh-client \
    iputils-ping \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#  Code Server server-proxy/vscode-proxy from https://coder.com/docs/code-server/latest
ENV CODE_VERSION=v4.92.2

ENV CODE_BUILTIN_EXTENSIONS_DIR=/usr/lib/code-server/lib/vscode/extensions/
ENV PATH=/opt/code-server/bin:$PATH \
    CS_DISABLE_GETTING_STARTED_OVERRIDE=1

ENV CODE_EXTENSIONSDIR='/home/$NB_USER/.local/share/code-server-$BUILD_IMAGE_NAME/extensions/'
ENV CODE_USERDATADIR='/home/$NB_USER/.local/share/code-server-$BUILD_IMAGE_NAME/'

#ENV SERVICE_URL=https://open-vsx.org/vscode/gallery 
#ENV ITEM_URL=https://open-vsx.org/vscode/item

# maybe create a image specific folder for vs code extensions inside $HOME and install extension at runtime via script
RUN cd /tmp \
    && curl -fOL https://github.com/coder/code-server/releases/download/v${CODE_VERSION}/code-server_${CODE_VERSION}_amd64.deb \
    && curl -sL https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg -o vscode.svg \
    && dpkg -i code-server_${CODE_VERSION}_amd64.deb \
    && rm -f code-server_${CODE_VERSION}_amd64.deb \
    && rm -rf /tmp/* $HOME/.config $HOME/.local $HOME/.cache \
    && fix-permissions $HOME && fix-permissions $CONDA_DIR && fix-permissions /home/$NB_USER

RUN code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension ms-python.python \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension ms-toolsai.jupyter \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension ms-toolsai.vscode-jupyter-cell-tags \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension humao.rest-client \
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension redhat.vscode-yaml \ 
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension donjayamanne.githistory \ 
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension alefragnani.project-manager \ 
    && code-server --extensions-dir ${CODE_BUILTIN_EXTENSIONS_DIR} --install-extension esbenp.prettier-vscode \  
    ## Create folders temp and tmp for Jupyter extension, 202 shoueld default to the verison 2023-X.XYZ
    && cd ${CODE_BUILTIN_EXTENSIONS_DIR}/ms-toolsai.jupyter-202* \
    && mkdir -m 1777 temp \
    && mkdir -m 1777 tmp \
    # update defualt values 
    && QUERY='.contributes.configuration.properties."python.condaPath".default="/opt/conda/bin/conda"' \
    && jq $QUERY /usr/lib/code-server/lib/vscode/extensions/ms-python.python-*/package.json | sponge /usr/lib/code-server/lib/vscode/extensions/ms-python.python-*/package.json \
    && QUERY='.contributes.configuration.properties."python.defaultInterpreterPath".default="/opt/conda/bin/python"' \
    && jq $QUERY /usr/lib/code-server/lib/vscode/extensions/ms-python.python-*/package.json | sponge /usr/lib/code-server/lib/vscode/extensions/ms-python.python-*/package.json \
    && rm -rf /tmp/* $HOME/.config $HOME/.local $HOME/.cache \
    && fix-permissions $HOME && fix-permissions $CONDA_DIR && fix-permissions /home/$NB_USER \
    && fix-permissions $CODE_BUILTIN_EXTENSIONS_DIR \
    && cd /tmp 

RUN pip install \
    jupyterlab-lsp==4.3.0 \
    jupyter-server-proxy==4.0.0  \
    git+https://github.com/fhswf/Jupyterhub-K8s.git@main#subdirectory=packages/jupyter_vscodeserver_proxy  \
    jedi-language-server \
    nbgitpuller \
    && rm -rf /tmp/* $HOME/.cache

# only install scilab-kernel for scipy notebooks
RUN if [ "$JUPYTER_VARIANT" = "scipy" ]; \
    then pip install scilab-kernel && rm -rf /tmp/* $HOME/.cache; \
    fi 

# conda tectlive latex lsp
# conda install --channel conda-forge tectonic texlab chktex
# conda install -c conda-forge texlab chktex

# make /home group writable in case we want to move /home/$NB_USER
RUN chmod g+rwx /home
# copy start scripts
COPY rebind_home.sh /usr/local/bin/before-notebook.d/01_rebind_home.sh
RUN  chmod +x /usr/local/bin/before-notebook.d/01_rebind_home.sh
COPY setup_env.sh /usr/local/bin/before-notebook.d/10_setup_env.sh  
RUN  chmod +x /usr/local/bin/before-notebook.d/10_setup_env.sh
COPY clean_runtime.sh /usr/local/bin/before-notebook.d/40_clean_runtime.sh
RUN  chmod +x /usr/local/bin/before-notebook.d/40_clean_runtime.sh
COPY launch_services.sh /usr/local/bin/before-notebook.d/60_launch_services.sh
RUN  chmod +x /usr/local/bin/before-notebook.d/60_launch_services.sh
COPY configure_cuda.sh /usr/local/bin/before-notebook.d/80_configure_cuda.sh
RUN  chmod +x /usr/local/bin/before-notebook.d/80_configure_cuda.sh

# git LFS and other extras
RUN apt-get update \
    && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash \
    && apt-get install -y --no-install-recommends \
    git-lfs zlib1g-dev git-core bash-completion \
    libncurses-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# user 
USER $NB_UID

RUN pip install bash_kernel \
    && python -m bash_kernel.install --prefix /opt/conda \
    && rm -rf /tmp/* $HOME/.cache

## npm language servers:
RUN npm install -g --save-dev \
    bash-language-server \
    pyright \
    sql-language-server \
    typescript-language-server \
    unified-language-server \
    vscode-css-languageserver-bin \
    vscode-html-languageserver-bin \
    yaml-language-server \
    vscode-json-languageserver-bin \
    && rm -rf /tmp/* $HOME/.cache

RUN npm config set cache /opt/conda/npm-cache --global

LABEL ki.fh-swf.de.jupyterhub.namelabel="vscode-${BUILD_JUPYTER_VARIANT}-${BUILD_CUDA_VARIANT}"
LABEL ki.fh-swf.de.jupyterhub.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook VS Code and ${BUILD_CUDA_VARIANT}."
LABEL org.opencontainers.image.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook VS Code and ${BUILD_CUDA_VARIANT}."
