# build
```
docker build . -t tf:local
```
# run
```
docker run --rm -p 8888:8888 -v $PWD:/home/jovyan/pwd --name tf tf:local jupyter lab --ServerApp.token=''
```
# packages
```
keras
keras-preprocessing
keras-tuner
matplotlib
mysql-connector-python
numpy
pandas
scikit-learn
seaborn
sqlalchemy
pymysql
tensorboard
tensorflow
sklearn
scipy
and more ....
```