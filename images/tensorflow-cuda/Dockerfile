FROM ghcr.io/fhswf/jupyterhub-k8s/scipy-notebook-cuda

SHELL ["/bin/bash", "-o", "pipefail", "-c"]


# comes from base image, i think...
#conda install -c conda-forge cudatoolkit=11.8.0
#pip install nvidia-cudnn-cu11==8.6.0.163

#CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib

#mkdir -p $CONDA_PREFIX/etc/conda/activate.d
#echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
#echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

## test
#python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
USER root

RUN mamba install --yes \
    'tensorflow' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER $NB_UID

# this might be faster, and also does not require root_
#pip install tensorflow==2.11.*
