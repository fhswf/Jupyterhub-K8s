run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name fulp_container <tag of image> jupyter lab --ServerApp.token=''
```