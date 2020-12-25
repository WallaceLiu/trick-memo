# 将会安装新的brew仓库源
```shell script
brew tap caskroom/versions
```
 
brew cask install java 将会安装jdk的最新版本，jdk内嵌jre
brew cask install java8 安装jdk8的最新版本

# 搜索java版本信息
```shell script
brew cask search java 
brew cask info java
brew cask install java
```
# 安装
最好翻墙，不然很麻烦
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```