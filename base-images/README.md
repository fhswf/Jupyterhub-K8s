# Base Images
Images in this folder are essentially just verions of the original jupyter-docker-stacks repository with special packages installed.
Such extra packages could for example include nvida-cuda libraries.
## Preinstalled packages
The Base images contain the follwing additions unless stated otherwise in the individual readme.
```
VS Code
nbgitpuller
```
## Naming and versions
base images (unless defined differently) come with versions base-{jupyter_variant}-{cuda_variant}.
Here the following Versions are created via github actions:
vscode-minimal-nocuda, vscode-scipy-cuda-cudnn, vscode-minimal-nocuda, vscode-scipy-cuda-cudnn
