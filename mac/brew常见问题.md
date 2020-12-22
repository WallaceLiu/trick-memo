# 一直卡在Updating Homebrew
## 1
运行命令brew install node，结果界面一直卡在Updating Homebrew...上，有两种解决办法
方法一：直接关闭brew每次执行命令时的自动更新（推荐）
vim ~/.bash_profile

- 新增一行
export HOMEBREW_NO_AUTO_UPDATE=true

## 方法二：替换brew源
cd "$(brew --repo)"
git remote set-url origin https://mirrors.ustc.edu.cn/brew.git

- 替换homebrew-core.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
brew update


# 备用地址-1
cd "$(brew --repo)"
git remote set-url origin https://git.coding.net/homebrew/homebrew.git
brew update


# 备用地址-2
cd "$(brew --repo)"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/brew.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew-core.git
brew update


如果备用地址都不行，那就只能再换回官方地址了
#重置brew.git
cd "$(brew --repo)"
git remote set-url origin https://github.com/Homebrew/brew.git

#重置homebrew-core.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://github.com/Homebrew/homebrew-core.git



清空dns缓存

sudo killall -HUP mDNSResponder
sudo killall mDNSResponderHelper
sudo dscacheutil -flushcache

#  cakebrew
程序，省事


# 安装java

可以使用brew安装很多应用，比如java，idea，iterms，sublime

brew tap caskroom/versions 将会安装新的brew仓库源
brew cask install java 将会安装jdk的最新版本，jdk内嵌jre
brew cask install java8 安装jdk8的最新版本


注意：使用brew install java 是找不到java的安装源的.
