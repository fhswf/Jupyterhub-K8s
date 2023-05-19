FROM ghcr.io/fhswf/jupyterhub-k8s/scipy-notebook-cuda

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN mamba install --yes \
    'tensorflow' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"