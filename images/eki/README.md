
# DeepML
A Test Image for working with quantized ai models using brevitas finn and other toolchains. Build on top of the deepml image.
This Image also contains user defineable startup hooks.

## build
```
docker build . -t eki:local
```
## run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name eki eki:local jupyter lab --ServerApp.token=''
```