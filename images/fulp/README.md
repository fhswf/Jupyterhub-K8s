# build
```
docker build . -t fulp:local
```
# run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name fulp_container fulp:local jupyter lab --ServerApp.token=''
```
