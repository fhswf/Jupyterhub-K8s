**[Technical Overview](#technical-overview)** |
**[Installation](#installation)** |
**[Configuration](#configuration)** |
**[Deployment](#deployment)** |
**[License](#license-mit)**

# [Jupyterhub on K8s with GPU support](https://github.com/fhswf/jupyterhub)
<!---
[![Docker Image CI](https://github.com/fhswf/jupyterhub/actions/workflows/docker-image-ci.yml/badge.svg?branch=main)](https://github.com/fhswf/jupyterhub/actions/workflows/docker-image-ci.yml)
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/fhswf/jupyterhub/issues)
[![GitHub Tags](https://img.shields.io/github/v/tag/fhswf/jupyterhub?style=plastic)](https://github.com/fhswf/jupyterhub/tags)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
-->
A customized version of the standard [zero-to-jupyterhub-k8s Project](https://github.com/jupyterhub/zero-to-jupyterhub-k8s).

## Technical Overview
### Authenticators
We are using a custom multi authenticator to allow for multiple authentication methods. The following authenticators are used:

| Authenticator | Description |
| - | - |
| [Keycloak (Generic OAuth)](https://github.com/jupyterhub/oauthenticator/blob/main/oauthenticator/generic.py) | Login with SSO and standard account login |
| [LTI Authenticator](https://github.com/jupyterhub/ltiauthenticator) | Login with Moodle |

### Custom Images
Custom Images are already supported by the official [helm chart from Jupyter](https://hub.jupyter.org/helm-chart/).
Default configuration values can be found in the repository [here](https://github.com/jupyterhub/zero-to-jupyterhub-k8s/tree/main/jupyterhub).
(Nivida-based) GPU Images need to be build with CUDA and are not available from the offcial Jupyter, hence we build them ourself.
Current Base Images can be found here (TODO).

## Deployment
Deploy via the official helm chart using our config:
```
TODO
```

## License
This Repository [MIT](https://github.com/fhswf/Jupyterhub-K8s/blob/main/LICENSE)
Jupyter [BSD 3](https://github.com/jupyter/jupyter/blob/master/LICENSE)
