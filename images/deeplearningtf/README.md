
# DeepML
A rather large image with all the tools and libraries for AI Research, Deeplearning, Machine Learning, Natural Language Processing and Datascience.

This Version does only support Tensorflow as the compute backend.

## build
```
docker build . -t deeplearningtf:local
```
## run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name deeplearningtf deeplearningtf:local jupyter lab --ServerApp.token=''
```
## packages
- General
    - scikit-learn (for machine learning)
    - ipywidgets (for interactive widgets)
    - nbgitpuller (for git integration)