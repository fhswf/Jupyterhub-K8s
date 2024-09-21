ARG JUPYTER_VARIANT

FROM jupyter/${JUPYTER_VARIANT}-notebook:lab-3.6.3 as nocuda

ARG JUPYTER_VARIANT
ENV BUILD_JUPYTER_VARIANT=$JUPYTER_VARIANT
ENV BUILD_IMAGE_NAME vscode-${BUILD_JUPYTER_VARIANT}

LABEL maintainer "Fachhochschule Südwestfalen"
LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="jupyter/${BUILD_JUPYTER_VARIANT}-notebook"
LABEL ki.fh-swf.de.jupyterhub.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook"
LABEL org.opencontainers.image.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"

###############
#  vscode 
###############
#FROM ${CUDA_VARIANT}

USER root

### VS-Code install 
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    htop \
    git \
    build-essential gcc g++ gnupg2 make less cmake \
    wget curl jq moreutils \
    openssh-client \
    iputils-ping \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


#  Code Server server-proxy/vscode-proxy from https://coder.com/docs/code-server/latest
ENV CODE_VERSION=4.21.0

ENV CODE_BUILTIN_EXTENSIONS_DIR=/usr/lib/code-server/lib/vscode/extensions/
ENV PATH=/opt/code-server/bin:$PATH \
    CS_DISABLE_GETTING_STARTED_OVERRIDE=1

ENV CODE_EXTENSIONSDIR='/home/$NB_USER/.local/share/code-server-$BUILD_IMAGE_NAME/extensions/'
ENV CODE_USERDATADIR='/home/$NB_USER/.local/share/code-server-$BUILD_IMAGE_NAME/'

#ENV SERVICE_URL=https://open-vsx.org/vscode/gallery 
#ENV ITEM_URL=https://open-vsx.org/vscode/item

# maybe create a image specific folder for vs code extensions inside $HOME and install extension at runtime via script
RUN cd /tmp \
    && curl -fsSL https://code-server.dev/install.sh | sh \
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
    jupyterlab-lsp \
    jupyter-server-proxy \
    git+https://github.com/fhswf/Jupyterhub-K8s.git@heller-dev#subdirectory=packages/jupyter_vscodeserver_proxy  \
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


# ---------------------------------
# Huggingface Chat UI
# ---------------------------------

RUN pip install \
jupyterlab-lsp \
jupyter-server-proxy \
git+https://github.com/fhswf/Jupyterhub-K8s.git@heller-dev#subdirectory=packages/huggingface_chat_ui  \
jedi-language-server \
nbgitpuller \
&& rm -rf /tmp/* $HOME/.cache

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash \
&& nvm install latest \
&& nvm use latest \
&& git clone https://github.com/huggingface/chat-ui \
&& cd chat-ui \
&& npm install

# ---------------------------------

# git LFS and other extras
RUN apt-get update \
    && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash \
    && apt-get install -y --no-install-recommends \
    git-lfs zlib1g-dev \
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

LABEL ki.fh-swf.de.jupyterhub.namelabel="vscode-${BUILD_JUPYTER_VARIANT}"
LABEL ki.fh-swf.de.jupyterhub.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook VS Code."
LABEL org.opencontainers.image.description="Based on the original jupyterlab ${BUILD_JUPYTER_VARIANT}-notebook VS Code."
