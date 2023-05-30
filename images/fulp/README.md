run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name fulp_container ghcr.io/fhswf/jupyterhub-k8s/fulp:develop jupyter lab --ServerApp.token=''
```
