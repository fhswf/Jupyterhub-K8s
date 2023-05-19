FROM ghcr.io/fhswf/Jupyterhub-K8s/scipy-cuda

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN mamba install --yes \
    'tensorflow' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"