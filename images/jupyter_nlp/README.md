# Jupter image for NLP

This image is based on the [jupyter/scipy-notebook](https://hub.docker.com/r/jupyter/scipy-notebook/) image and adds the following packages:

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

## Run
    
```bash
docker run -p 8888:8888 -v /path/to/notebooks:/home/jovyan/work jupyter_nlp
```

## Build

```bash
docker build -t jupyter_nlp .
```
