
# DeepML
A rather large image with all the tools and libraries for AI Research, Deeplearning, Machine Learning, Natural Language Processing and Datascience.

Comes with common used packages like Tensorflow, Keras, PyTorch, Scipy, SK-Learn and Huggingface Libaries. See below for a full package list.
This image contains CUDA/CUDNN and is meant to be launched with the nvidia-container-runtime. 

## build
```
docker build . -t deepml:local
```
## run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name deepml deepml:local jupyter lab --ServerApp.token=''
```
## packages
- Transformers
    - [transformers](https://huggingface.co/transformers/) 
    - [datasets](https://huggingface.co/datasets/) 
    - [metrics](https://huggingface.co/metrics/)
    - tokenizers
- NLP
    - [nltk](https://www.nltk.org/) 
    - [gensim](https://radimrehurek.com/gensim/) 
    - [spacy](https://spacy.io/) 
    - [rasa](https://rasa.com/)
- General
    - torch 
    - torchvision 
    - torchaudio 
    - scikit-learn (for machine learning)
    - ipywidgets (for interactive widgets)
    - nbgitpuller (for git integration)