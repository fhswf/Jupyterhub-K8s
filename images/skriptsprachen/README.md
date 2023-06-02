A basic Image for Learning python.

Contains VSCode, python and an extra bash kernel.

## build
```
docker build . -t script:local
```
## run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name script script:local jupyter lab --ServerApp.token=''
```