# build
docker build . -t arm32:local

# run
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name arm32 arm32:local jupyter lab --ServerApp.token=''