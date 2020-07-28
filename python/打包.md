# 打包pyc
```python
# -*- coding: utf-8 -*-
import zipfile
import os


def ziplib():
    """
    将线上运行代码打包
    :return:
    """
    dir = os.path.dirname(__file__)
    lib_path = os.path.join(dir, '../core')

    # set it as save file path
    zip_path = './core.zip'
    zf = zipfile.PyZipFile(zip_path, mode='w')

    try:
        zf.debug = 3
        # This method will compile the module.py into module.pyc
        zf.writepy(lib_path)
        return zip_path
    finally:
        zf.close()


ziplib()

```
# 打包py
zip -rq 命令。
```bash
#!/bin/bash
# for ubuntu
home=/home/hehongjie
# for mac
#home=/Users/hehongjie1
params=("core.zip" "./core/")
libFolder=${home}/Dev/PyLib
for ((i=0;i<${#params[*]};i+=2))
do
    echo Starting zip ${params[i]}
    zipFile=${params[i]}
    zipSource=${params[i+1]}
    rm ${zipFile}
    zip -rq ${zipFile} ${zipSource}
    rm ${libFolder}/${zipFile}
    cp ${zipFile} ${libFolder}/
    echo Finish zip ${params[i]}
    echo
done
```