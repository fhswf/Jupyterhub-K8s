ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-minimal-nocuda:sha-56b6463
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME fulp
# Extra arguments to `stack build`. Used to build --fast, see Makefile.
ARG STACK_ARGS=

USER root

#  dependencies for haskell/ihaskell and some usefull tools
RUN apt-get update && apt-get install -yq --no-install-recommends \
        dpkg-dev netbase xz-utils zlib1g-dev libc6-dev \
        build-essential curl gcc g++ gnupg2 make less \
        libtinfo-dev \ 
        libffi-dev \
        libgmp-dev \
        libncurses-dev \
        libzmq3-dev \
        libcairo2-dev \
        libpango1.0-dev \
        libmagic-dev \
        libblas-dev \
        liblapack-dev \
        graphviz \
        gnuplot-nox \
        less \
        && rm -rf /var/lib/apt/lists/*

RUN conda install --quiet --yes \
# ihaskell-widgets needs ipywidgets
# https://github.com/IHaskell/IHaskell/issues/1380
    'ipywidgets=7.7.1' && \
# ihaskell-hvega doesn't need an extension. https://github.com/jupyterlab/jupyter-renderers
#    'jupyterlab-vega3' && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

#############################
# To install ihaskell globally we follow the ihaskell-notebook installation
# from https://github.com/IHaskell/ihaskell-notebook/blob/master/Dockerfile
#
# Main reason IHaskell needs a global preconfigured stack project
##############################

# Stack Linux (generic) Manual download
# https://docs.haskellstack.org/en/stable/install_and_upgrade/#linux-generic
#
# So that we can control Stack version, we do manual install instead of
# automatic install:
#
#    curl -sSL https://get.haskellstack.org/ | sh
#

# The global snapshot package database: STACK_ROOT
ENV STACK_ROOT=/opt/stack
RUN mkdir -p $STACK_ROOT
RUN fix-permissions $STACK_ROOT

# latest stack version as of 2023/05/24
ARG STACK_VERSION="2.11.1"
ARG STACK_BINDIST="stack-${STACK_VERSION}-linux-x86_64"
RUN    cd /tmp \
    && curl -sSL --output ${STACK_BINDIST}.tar.gz https://github.com/commercialhaskell/stack/releases/download/v${STACK_VERSION}/${STACK_BINDIST}.tar.gz \
    && tar zxf ${STACK_BINDIST}.tar.gz \
    && cp ${STACK_BINDIST}/stack /usr/bin/stack \
    && rm -rf ${STACK_BINDIST}.tar.gz ${STACK_BINDIST} \
    && stack --version

# Stack global non-project-specific config stack.config.yaml
# https://docs.haskellstack.org/en/stable/yaml_configuration/#non-project-specific-config
RUN mkdir -p /etc/stack
COPY stack.config.yaml /etc/stack/config.yaml
RUN fix-permissions /etc/stack

# Stack global project stack.yaml
# https://docs.haskellstack.org/en/stable/yaml_configuration/#yaml-configuration
RUN mkdir -p $STACK_ROOT/global-project
COPY global-project.stack.yaml $STACK_ROOT/global-project/stack.yaml
RUN    chown --recursive $NB_UID:users $STACK_ROOT/global-project \
    && fix-permissions $STACK_ROOT/global-project

# fix-permissions for /usr/local/share/jupyter so that we can install
# the IHaskell kernel there. Seems like the best place to install it, see
#      jupyter --paths
#      jupyter kernelspec list
RUN    mkdir -p /usr/local/share/jupyter \
    && fix-permissions /usr/local/share/jupyter \
    && mkdir -p /usr/local/share/jupyter/kernels \
    && fix-permissions /usr/local/share/jupyter/kernels

# Now make a bin directory for installing the ihaskell executable on
# the PATH. This /opt/bin is referenced by the stack non-project-specific
# config.
RUN    mkdir -p /opt/bin \
    && fix-permissions /opt/bin
ENV PATH ${PATH}:/opt/bin

# Specify a git branch for IHaskell (can be branch or tag).
# The resolver for all stack builds will be chosen from
# the IHaskell/stack.yaml in this commit.
# https://github.com/gibiansky/IHaskell/commits/master
# IHaskell 2022-12-19
ARG IHASKELL_COMMIT=1c22a874ac0c8ed019229f4a0cd5a0bfda017357


## vega
# Specify a git branch for hvega
# https://github.com/DougBurke/hvega/commits/main
# hvega 2022-06-16
# hvega-0.12.0.3
# ihaskell-hvega-0.5.0.3

ARG HVEGA_COMMIT=2b453c230294b889564339853de02b0c1829a081

# Clone IHaskell and install ghc from the IHaskell resolver
RUN    cd /opt \
    && curl -L "https://github.com/gibiansky/IHaskell/tarball/$IHASKELL_COMMIT" | tar xzf - \
    && mv *IHaskell* IHaskell \
    && curl -L "https://github.com/DougBurke/hvega/tarball/$HVEGA_COMMIT" | tar xzf - \
    && mv *hvega* hvega \
    && fix-permissions /opt/IHaskell \
    && fix-permissions $STACK_ROOT \
    && fix-permissions /opt/hvega \
    && stack setup \
    && fix-permissions $STACK_ROOT \
    && rm /opt/stack/programs/x86_64-linux/ghc*.tar.xz

# Build IHaskell
#
# Note that we are NOT in the /opt/IHaskell directory here, we are
# installing ihaskell via the paths given in /opt/stack/global-project/stack.yaml
RUN    stack build $STACK_ARGS ihaskell \
    && fix-permissions /opt/IHaskell \
    && fix-permissions $STACK_ROOT

# Install IHaskell.Display libraries
# https://github.com/gibiansky/IHaskell/tree/master/ihaskell-display
#RUN    stack build $STACK_ARGS ihaskell-aeson \
#    && stack build $STACK_ARGS ihaskell-blaze \
#    && stack build $STACK_ARGS ihaskell-charts \
#    && stack build $STACK_ARGS ihaskell-diagrams \
#    && stack build $STACK_ARGS ihaskell-gnuplot \
#    && stack build $STACK_ARGS ihaskell-graphviz \
#    && stack build $STACK_ARGS ihaskell-hatex \
#    && stack build $STACK_ARGS ihaskell-juicypixels \
##   && stack build $STACK_ARGS ihaskell-magic \
#    && stack build $STACK_ARGS ihaskell-plot \
##   && stack build $STACK_ARGS ihaskell-rlangqq \
##   && stack build $STACK_ARGS ihaskell-static-canvas \
#    && stack build $STACK_ARGS ihaskell-widgets \
#    && stack build $STACK_ARGS hvega \
#    && stack build $STACK_ARGS ihaskell-hvega \
#    && fix-permissions $STACK_ROOT \
## Fix for https://github.com/IHaskell/ihaskell-notebook/issues/14#issuecomment-636334824
#    && fix-permissions /opt/IHaskell \
#    && fix-permissions /opt/hvega

# Cleanup
# Clean of IHaskell/.stack-work  causes https://github.com/IHaskell/ihaskell-notebook/issues/5
# in this case user can not build packages based on ihaskell, which for just running hasell does not matter
RUN  rm -rf $(find /opt/IHaskell -type d -name .stack-work)
# clean /opt/hvega ?
    # && rm -rf $(find /opt/hvega -type d -name .stack-work)

# Bug workaround for https://github.com/IHaskell/ihaskell-notebook/issues/9
RUN mkdir -p /home/jovyan/.local/share/jupyter/runtime \
    && fix-permissions /home/jovyan/.local \
    && fix-permissions /home/jovyan/.local/share \
    && fix-permissions /home/jovyan/.local/share/jupyter \
    && fix-permissions /home/jovyan/.local/share/jupyter/runtime

# Install system-level ghc using the ghc which was installed by stack
# using the IHaskell resolver.
RUN mkdir -p /opt/ghc && ln -s `stack path --compiler-bin` /opt/ghc/bin \
    && fix-permissions /opt/ghc
ENV PATH ${PATH}:/opt/ghc/bin

USER $NB_UID
# Install the IHaskell kernel at /usr/local/share/jupyter/kernels, which is
# in `jupyter --paths` data:
RUN stack exec ihaskell -- install --stack --prefix=/usr/local
USER root

#######
# vs code
##########
# vs code haskell needs ghcup, which manages its own install of ghc on the fly (per project)
# this install script could confict with the custom install of ghc/stack and cabal
# RUN BOOTSTRAP_HASKELL_NONINTERACTIVE=1 curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh 
# ghcup binary is all that vscode needs 

#ENV GHCUP_ROOT=/opt/ghcup
#ENV GHCUP_INSTALL_BASE_PREFIX=/opt/ghcup
#ENV GHCUP_USE_XDG_DIRS=1
#ENV GHCUP_SKIP_UPDATE_CHECK=1

#RUN mkdir -p $GHCUP_ROOT
#RUN fix-permissions $GHCUP_ROOT
#RUN curl https://downloads.haskell.org/~ghcup/x86_64-linux-ghcup >> ${GHCUP_ROOT}/ghcup 
#RUN chmod +x ${GHCUP_ROOT}/ghcup  && fix-permissions ${GHCUP_ROOT}/ghcup
#ENV PATH ${PATH}:/opt/ghcup

#USER $NB_UID
#RUN ghcup install hls
#USER root

#### alternate manual install of hls
RUN mkdir -p /tmp/hls && cd /tmp/hls \
    && curl -sSL --output hls.tar.xz https://github.com/haskell/haskell-language-server/releases/download/2.0.0.0/haskell-language-server-2.0.0.0-x86_64-linux-deb11.tar.xz  \
    && tar -xf hls.tar.xz \
    && cp haskell-language-server-2.0.0.0/bin/haskell-language-server-9.4.5 /opt/bin/haskell-language-server-9.4.5 \
    && cp haskell-language-server-2.0.0.0/bin/haskell-language-server-wrapper /opt/bin/haskell-language-server-wrapper \
# copy libs over (yes this is dirty, but somehow libs in ghc lib dir dont work for some reason)
    && mkdir /lib/hls  \
    && cp -r haskell-language-server-2.0.0.0/lib/9.4.5/* /lib/x86_64-linux-gnu/  \
    && cp -r /opt/stack/programs/x86_64-linux/ghc-tinfo6-9.4.5/lib/ghc-9.4.5/lib/x86_64-linux-ghc-9.4.5/* /lib/x86_64-linux-gnu/ \
    && fix-permissions /opt/bin  \
    && cd /tmp && rm -rf /tmp/hls

############
# swi prolog & jupyterextension
############

# RUN apt-get install software-properties-common \
#RUN apt-add-repository ppa:swi-prolog/stable \
#    && apt-get update \
#    && apt-get install swi-prolog \
#    && rm -rf /var/lib/apt/lists/* 

ENV LANG C.UTF-8
RUN set -eux \
    && SWIPL_VER=9.1.10 \
    && SWIPL_CHECKSUM=16c0d014510f5e0c3b427d2842cac89fea0d4c136caabbeb698d578ee8126870 \
    && BUILD_DEPS='make cmake ninja-build gcc g++ wget git autoconf libarchive-dev libgmp-dev libossp-uuid-dev libxext-dev libice-dev libjpeg-dev libxinerama-dev libxft-dev libxpm-dev libxt-dev libpcre2-dev ncurses-dev  libreadline-dev libedit-dev libssl-dev zlib1g-dev libdb-dev unixodbc-dev libgoogle-perftools-dev libyaml-dev' \
    && apt-get update \
    && apt-get install -y --no-install-recommends $BUILD_DEPS \
    # && apt-get install libgoogle-perftools-dev \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /tmp/src \
    && cd /tmp/src \
    && wget -q https://www.swi-prolog.org/download/devel/src/swipl-$SWIPL_VER.tar.gz \
    && echo "$SWIPL_CHECKSUM  swipl-$SWIPL_VER.tar.gz" >> swipl-$SWIPL_VER.tar.gz-CHECKSUM \
    && sha256sum -c swipl-$SWIPL_VER.tar.gz-CHECKSUM \
    && tar -xzf swipl-$SWIPL_VER.tar.gz \
    && mkdir swipl-$SWIPL_VER/build \
    && cd swipl-$SWIPL_VER/build \
    && cmake -DCMAKE_BUILD_TYPE=PGO \
          -DSWIPL_PACKAGES_X=OFF \
	  -DSWIPL_PACKAGES_JAVA=OFF \
	  -DCMAKE_INSTALL_PREFIX=/usr \
      -DSPM_ENABLE_TCMALLOC=OFF \
          .. \
    && make \
    && make install \
    && rm -rf /tmp/src 
    # && apt-get purge -y --auto-remove $BUILD_DEPS 

RUN set -eux \
    && swipl -g "pack_install(log4p,[interactive(false)]) " -t halt \
    && swipl -g "pack_install(prolog_lsp,[interactive(false)]) "  -t halt 

RUN pip install prolog_kernel jupyterlab_prolog_codemirror_extension \
    && python -m prolog_kernel.install --prefix /usr/local \
    && fix-permissions /usr/local/share/jupyter/kernels

# check kernels
RUN jupyter kernelspec list

# vscode extensions
RUN code-server --extensions-dir /usr/lib/code-server/lib/vscode/extensions/ --install-extension haskell.haskell \
    && code-server --extensions-dir /usr/lib/code-server/lib/vscode/extensions/ --install-extension hargettp.pure-prolog-language-support \
    && rm -rf /tmp/* $HOME/.config $HOME/.local $HOME/.cache \
    && fix-permissions $HOME && fix-permissions $CONDA_DIR && fix-permissions /home/$NB_USER

# Switch back to jovyan user
USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Functional and logical programming"
LABEL org.opencontainers.image.description="Functional and logical programming"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER