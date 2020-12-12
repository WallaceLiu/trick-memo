### 部署到linux操作系统，amd64架构
```
$CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build 你的go程序.go
```
> make.bash中用到的环境变量：
> - GOROOT_FINAL：Go源码的根目录，这个变量的是在gcc的时候使用的，如果你设置了这个，gcc的-D参数就是你设置的
> - GOHOSTARCH：Go所在的宿主机器的CPU架构，也就是你自己机器的CPU架构。
> - GOARCH：安装包和工具所在的机器的架构，也就是你想部署机器的CPU架构。
> - GOOS：安装包和工具所在的机器的操作系统。
> - GO_GCFLAGS：是否要在编译的时候需要带上5g/6g/8g的参数
> - GO_LDFLAGS：是否要在链接的时候带上5l/6l/8l的参数
> - CGO_ENABLED：是否能使用cgo