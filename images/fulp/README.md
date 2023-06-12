# FulP
Image with Haskell, Prolog (and Python).
Examples on how to use the Prolog-Kernel can be found [here](https://nbviewer.org/github/anbre/prolog-jupyter-kernel/blob/master/notebooks/feature_introduction/swi/using_jupyter_notebooks_with_swi_prolog.ipynb)

## build
```
docker build . -t fulp:local
```
## run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name fulp_container fulp:local jupyter lab --ServerApp.token=''
```
## packages
- SWI-Prolog
- [prolog-kernel](https://github.com/hhu-stups/prolog-jupyter-kernel)
- Haskell (via Stack)
- [iHaskell](https://github.com/IHaskell/IHaskell)
