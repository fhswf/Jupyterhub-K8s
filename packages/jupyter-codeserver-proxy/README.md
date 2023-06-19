## Description
A simple start command for jupyter-server-proxy to launch [code-server](https://github.com/coder/code-server) inside jupyterlab.

## Install
We have not published this package to pypi, but you can install it with pip directly from github:
```
pip install git+https://github.com/fhswf/Jupyterhub-K8s.git@main#subdirectory=packages/jupyter-codeserver-proxy
```
Using pip and requirements.txt, simple put the above link into the file:
```
package-one==1.9.4
git+https://github.com/fhswf/Jupyterhub-K8s.git@main#subdirectory=packages/jupyter-codeserver-proxy
package-three==2.0.0
numpy
...
```
## copy right notice
Note that this package is a modification of exsisting server proxies for vscode that also exsist on github.
For example [this](https://github.com/betatim/vscode-binder/tree/master/jupyter_vscode_proxy), which was published under BSD-3.
