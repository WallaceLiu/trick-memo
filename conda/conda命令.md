# 管理conda
## 检查conda版本:
```
$ conda --version
conda 4.3.16
$
```
## 升级当前版本的conda
```
$ conda update conda
```
# 管理环境
## 创建并激活环境
### 创建一个新环境
```
$ conda create --name snowflake biopython
```
该命令将为Biopython创建一个名为“snowflake”环境。位置在$Anaconda/envs/snowflakes。
可以指定python版本，如“conda create --name snowflake python=版本号”。
### 激活这个环境
- Linux，OS X
```
source activate snowflakes
```
- Windows
```
activate snowflake
```
> 新环境默认安装在你conda目录下的envs文件目录下。但也可以指定其他路径。通过conda create -h了解更多信息。

> 如果没有指定python版本，则会安装我们最初安装conda时所装的那个python版本。
## 列出所有的环境
```
$ conda info --envs
# conda environments:
#
tensorflow               /Applications/anaconda/envs/tensorflow
root                  *  /Applications/anaconda

$ conda info -e
# conda environments:
#
tensorflow               /Applications/anaconda/envs/tensorflow
root                  *  /Applications/anaconda

$
```
> 星号表示当前活动的环境。
## 切换到另一个环境
- Linux，OS X
```
source activate snowflakes
```
- Windows
```
activate snowflakes
```
如果要从当前工作环境切换到系统根目录时，键入：
- Linux，OS X
```
source deactivate
```
- Windows:
```
deactivate
```
## 复制一个环境
通过克隆snowflakes来创建一个称为flowers的副本。
```
conda create -n flowers --clone snowflakes
```
## 删除一个环境
```
conda remove -n flowers 
```
# 管理Python
## 安装一个不同版本的python
现在假设你需要python3来编译程序，但你不想覆盖掉你的python2.7，你可以创建并激活一个名为snakes的环境，并通过下面的命令来安装最新版本的python3：
```
conda create -n snakes python=3
```
## 检查新环境中的python版本
确保snakes环境中运行的是python3：
```
python --version
```
## 使用不同版本的python
为了使用不同版本的python，你可以切换环境，通过简单的激活它就可以，让我们看看如何返回默认版本
- Linux，OS X
```
source activate - snowflakes
```
- Windows
```
activate snowflakes
```
## 注销环境
当你完成了在snowflakes环境中的工作室，注销掉该环境并转换你的路径到先前的状态：
- Linux，OS X
```
source deactivate
```
- Windows
```
deactivate
```
# 管理包
- conda管理python包非常方便，可以在指定的python环境中安装包，且自动安装所需要的依赖包，避免了很多拓展包冲突兼容问题。
- 不建议使用easy_install安装包。大部分包都可以使用conda安装，无法使用conda和anaconda.org安装的包可以通过pip命令安装
- 使用合适的源可以提升安装的速度
## 查看已安装包
```
conda list
```
## 向指定环境中安装包
### 使用Conda命令安装包
在指定环境中安装这个Beautiful Soup包，有两种方式:
- 直接用 -n 指定安装环境
```
conda install --name bunnies beautifulsoup4
```
> 必须告诉conda你要安装环境的名字，否则它将会被安装到当前环境中。
- 先激活环境，再用conda install命令安装
```
activate bunnies
conda install beautifulsoup4
```
### 从Anaconda.org安装包
如果不能使用conda安装包，那么在Anaconda.org网站查找。查找一个叫“bottleneck”的包，Anaconda.org会列出所有可用版本，下载最频繁的那个版本。会链接到Anaconda.org详情页显示下载的具体命令：
```
conda install--channel https：//conda .anaconda.ort/pandas bottleneck
```
### 通过pip命令来安装包
对于那些无法通过conda安装或者从Anaconda.org获得的包，我们通常可以用pip命令来安装包。
可以上pypi网站查询要安装的包，查好以后输入pip install命令就可以安装这个包了。
我们激活想要放置程序的python环境，然后通过pip安装一个叫“See”的程序。
- Linux，OS X
```
source activate bunnies
```
- Windows
```
activate bunnies
```
- 所有平台：
```
pip install see
```
> pip只是一个包管理器，不能为你管理环境，甚至不能升级python，因为它不像conda一样把python当做包来处理。但是它可以安装一些conda安装不了的包。
### 文件安装
如果上面这些方法通通不管用！！！那就只能下载源码安装了，比如exe文件（双击安装）或者whl文件（pip安装）等等。还有在github上找到源码，使用python setup.py install命令安装
> Tips:不建议使用setuptools 的easy_install，非常不方便管理，也不好卸载
有些时候，Anaconda和pip下载的速度慢，访问不稳定怎么办？换个源呗，清华大学的源就很不错，当然，你可以自己google一些好用的源
对于包管理工具，了解这么多就够了，比较喜欢追根究底的童鞋可以移步包管理工具解惑
> 提示：在任何时候你可以通过在命令后边跟上-help来获得该命令的完整文档。
**
eg:
```
conda update --help
 ```
> 小技巧：很多跟在–后边常用的命令选项，可以被略写为一个短线加命令首字母。所以–name选项和-n的作用是一样的。通过conda -h或conda –-help来看大量的缩写。
# 移除包、环境、conda
## 移除包
假设你决定不再使用商业包IOPro。你可以在bunnies环境中移除它。
```
conda remove -n bunnies iopro
```
## 移除环境
我们不再需要snakes环境了，所以输入以下命令：
```
conda remove -n snakes --all
```
## 删除conda
- Linux，OS X：
移除Anaconda 或 Miniconda 安装文件夹
```
rm -rf ~/miniconda 
```
或
```
rm -rf ~/anaconda
```
- Windows：
去控制面板，点击“添加或删除程序”，选择“Python2.7（Anaconda）”或“Python2.7（Miniconda）”并点击删除程序。
