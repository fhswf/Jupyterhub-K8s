FROM jupyter/minimal-notebook

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# Devdepenedencies
RUN apt-get update --yes && \
    apt-get install --yes --quiet --no-install-recommends \
    curl \
    iputils-ping \
	build-essential \
    make \
    cmake \
    g++ \
    clang \
    htop \
    libopencv-dev \
    npm\
    && \
    apt-get --quiet clean && rm -rf /var/lib/apt/lists/*

#  Code Server server-proxy/vscode-proxy from https://coder.com/docs/code-server/latest
ENV CODE_VERSION=4.12.0
RUN curl -fOL https://github.com/coder/code-server/releases/download/v$CODE_VERSION/code-server_${CODE_VERSION}_amd64.deb \
    && dpkg -i code-server_${CODE_VERSION}_amd64.deb \
    && rm -f code-server_${CODE_VERSION}_amd64.deb
RUN /opt/conda/bin/conda install -c conda-forge jupyter-server-proxy
RUN /opt/conda/bin/conda install -c conda-forge jupyter-vscode-proxy

# X11 desktop env, warning this is unstable!
#RUN apt-get update --yes --quiet && \
#    apt-get install --yes --quiet \
#    dbus-x11 xfce4 xfce4-panel xfce4-session xfce4-settings xorg xubuntu-icon-theme && \
#    apt-get remove --yes --quiet light-locker && \
#    apt-get clean --quiet && rm -rf /var/lib/apt/lists/*
#RUN /opt/conda/bin/conda install -c manics websockify && \
#    pip install git+https://github.com/yuvipanda/jupyter-desktop-server.git
 
# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}

LABEL fhswf.jupyterhub.runtime="CPU"
LABEL fhswf.jupyterhub.namelabel="Generic vscode-server example"
LABEL fhswf.jupyterhub.description="Generic vscode-server example for jupyterhub"
LABEL org.opencontainers.image.description="Generic vscode-server example for jupyterhub"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"