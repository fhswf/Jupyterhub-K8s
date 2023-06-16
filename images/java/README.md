# build
```
docker build . -t java:local
```
# run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name java java:local jupyter lab --ServerApp.token=''
```
# packages
