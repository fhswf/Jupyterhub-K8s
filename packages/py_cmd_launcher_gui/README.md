## What
Simple flask server to launch a system command. Used to API-ify container run scripts.
This is not for usage in an unsave production setup, as there is not auth or encryption.
Please only use this for internal networks such as contained kubernets pods, without external excess.

## Install
We have not published this package to pypi, but you can install it with pip directly from github:
```
pip install git+https://github.com/fhswf/Jupyterhub-K8s.git@main#subdirectory=packages/py_cmd_launcher
```
Using pip and requirements.txt, simple put the above link into the file:
```
package-one==1.9.4
git+https://github.com/fhswf/Jupyterhub-K8s.git@main#subdirectory=packages/py_cmd_launcher
package-three==2.0.0
numpy
...
```