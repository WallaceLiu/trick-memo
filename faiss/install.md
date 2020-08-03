```shell script
conda create -n myfaiss  python=3.7
conda install -n myfaiss mkl
conda install -n myfaiss faiss-cpu -c pytorch # cpu
conda install -n myfaiss faiss-gpu -c pytorch # gpu
```
