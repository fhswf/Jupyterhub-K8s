
FROM ghcr.io/fhswf/jupyterhub-docker-stacks/scipy-notebook:latest

LABEL maintainer="FH SWF"

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    tzdata \
    gfortran \
    gcc \
    scilab \
    pari-gp \
    libpari-dev \
    libgmp-dev \
    htop \
    wget \
    curl \
    iputils-ping \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

RUN pip install -U jupyterhub \
    pip install nbgitpuller ipywidgets \
    pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117 \
    pip install transformers datasets metrics tokenizers \
    pip install spacy \
    pip install nltk \
    pip install gensim \
    pip install rasa \
    pip install scikit-learn 

USER root

ENV LD_LIBRARY_PATH=${CONDA_DIR}/lib/:${LD_LIBRARY_PATH}
RUN echo LD_LIBRARY_PATH="${LD_LIBRARY_PATH}" >> /etc/environment 
ENV CPATH=$CONDA_DIR/include
RUN echo CPATH="${CPATH}" >> /etc/environment

USER $NB_UID

ENV CPATH=$CONDA_DIR/include:$CPATH

# the label fhswf.jupyterhub.runtime has to be present for runtime detection of available images 
LABEL fhswf.jupyterhub.runtime="NVIDIA-GPU"
LABEL fhswf.jupyterhub.namelabel="Jupyter NLP"
LABEL fhswf.jupyterhub.description="Custom JupyterLab image for natural language processing."
LABEL org.opencontainers.image.description="Custom JupyterLab image for natural language processing."
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
