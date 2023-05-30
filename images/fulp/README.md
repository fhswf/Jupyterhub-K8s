run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name fulp_container harbor.ki.fh-swf.de/ghcr.io/fhswf/jupyterhub-k8s/fulp:sha-b34e38e jupyter lab --ServerApp.token=''
```