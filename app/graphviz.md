http://www.graphviz.org

- 1、ModuleNotFoundError: No module named 'graphviz’

> 原因：未安装graphviz组件

- 2、graphviz.backend.ExecutableNotFound: failed to execute [‘dot’, ‘-Tpng’, ‘-O’, ‘tmp’], make sure the Graphviz executables are on your systems’ PATH

> 原因：未在系统中配置graphviz工具的环境变量

Graphviz是AT&T Labs Research开发的图形绘制工具软件，不是python工具。

解决方法：

- 在Conda里安装，而brew可能会报错。

- 手动配置path环境变量。

- 在python terminal内通过pip install graphviz 安装组件。

- 重启一下编译器（pycharm）后，就可以正常使用了。

关于如何在IDE内调用graphviz查看.dot文件, 可以参看：https://blog.csdn.net/az9996/article/details/86564357

参考资料：

https://blog.csdn.net/qq_35608277/article/details/78639957

https://blog.csdn.net/castle_cc/article/details/79978170