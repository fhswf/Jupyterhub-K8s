**[Technical Overview](#technical-overview)** |
**[Installation](#installation)** |
**[Configuration](#configuration)** |
**[Deployment](#deployment)** |
**[License](#license-mit)**

# Jupyterhub on Kubernetes with GPU support and Multiauthentication

<!---
[![Docker Image CI](https://github.com/fhswf/jupyterhub/actions/workflows/docker-image-ci.yml/badge.svg?branch=main)](https://github.com/fhswf/jupyterhub/actions/workflows/docker-image-ci.yml)
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/fhswf/jupyterhub/issues)
[![GitHub Tags](https://img.shields.io/github/v/tag/fhswf/jupyterhub?style=plastic)](https://github.com/fhswf/jupyterhub/tags)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
-->
A customized version of the standard [zero-to-jupyterhub-k8s Project](https://github.com/jupyterhub/zero-to-jupyterhub-k8s) used for educational student workspaces, where they can experiment with Deep Learning frameworks and develop python notebooks.
This is an update to our older Jupyterhub with GPU support using Docker Swarm. The old project can be found [here](https://github.com/fhswf/jupyterhub). Note that K8s takes more effort to deploy and manage, so if you are looking for a simpler way to use GPUs with Jupyterhub take a look.

## Technical Overview
### Authenticators
We are using a custom multi authenticator to allow for multiple authentication methods. The following authenticators are used:

| Authenticator | Description |
| - | - |
| [Keycloak (Generic OAuth)](https://github.com/jupyterhub/oauthenticator/blob/main/oauthenticator/generic.py) | Login with SSO and standard account login |
| [LTI Authenticator](https://github.com/jupyterhub/ltiauthenticator) | Login with Moodle |

### Kubernetes and GPUs
For GPU usage in the cluster, the GPUs have to be advertised as allocatable ressources. We recommend the GPU-feature-discovery tool or the GPU-operator from NVIDIA.

### Shared Storage
Local storage for cluster users, requires a storage class to be present in the cluster. In order to share data between users, a network storage such as nfs can be used and mounted int every pod. Your storage provider/system should be able to handle multiple users. Note that a lot of python applications, specifically ML stuff, can be quite demanding, both in Terms of IOps and throughput. 

# Images
Custom Images are already supported by the official [helm chart from Jupyter](https://hub.jupyter.org/helm-chart/).
Default configuration values can be found in the repository [here](https://github.com/jupyterhub/zero-to-jupyterhub-k8s/tree/main/jupyterhub).
(NVIDIA-based) GPU Images need to be build with CUDA and are not available from the official Jupyter, hence we be build them ourselfs.
### Lab images
Primary folder for launchables by the hub: images
Please create a subfolder for each lab/image/profile/course you want to use.
In theory al images that are based on the original base image from the jupyterhub project will work and as the hub in basicly just a proxy, most dockerized web services can be deployed with jupyterhub. 
### CI Dockerbuild
Automated image building can be achieved with githubactions.
Currently builds for Dockerfiles under images are automated.
See[ /.github/workflows/build_images.yml](https://github.com/fhswf/Jupyterhub-K8s/blob/main/.github/workflows/build_images.yml)
### Usage in the hub
For a new or updated image to be usable, a profile for the kubernetes spawner has to be created and inserted into the helm chart values.yaml for jupyterhub in the [deployment repository](https://github.com/fhswf/kicluster-deployments/blob/main/jupyterhub/helm/values.yaml)
An example profile could look like this:
```
hub:
  singleuser:
    profileList:
    - display_name: "NLP environment"
      description: "Comes with Transformers, NLTK, Spacy, Gensim, and more"
      kubespawner_override:
        http_timeout: 120
        start_timeout: 300
        image: ghcr.io/fhswf/jupyterhub-k8s/jupyter_nlp:sha-cdbfbd0
        extra_resource_limits:
          nvidia.com/gpu: "1"
```
New versions of images tagged with a latest tag are not always synced. To better control image versions we recommend updating the sha-tag manually.
We are looking into better ways for a complete cicd solution.
## License
This Repository [MIT](https://github.com/fhswf/Jupyterhub-K8s/blob/main/LICENSE)
Jupyter [BSD 3](https://github.com/jupyter/jupyter/blob/master/LICENSE)
