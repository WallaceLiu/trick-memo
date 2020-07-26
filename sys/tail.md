linux tail命令用途是依照要求将指定的文件的最后部分输出到标准设备，通常是终端，通俗讲来，就是把某个档案文件的最后几行显示到终端上，假设该档案有更新，tail会自己主动刷新，确保你看到最新的档案内容。
tail命令语法
```
tail [ -f ] [ -c Number | -n Number | -m Number | -b Number | -k Number ] [ File ]
参数解释：
-f 该参数用于监视File文件增长。
-c Number 从 Number 字节位置读取指定文件
-n Number 从 Number 行位置读取指定文件。
-m Number 从 Number 多字节字符位置读取指定文件，比方你的文件假设包括中文字，假设指定-c参数，可能导致截断，但使用-m则会避免该问题。
-b Number 从 Number 表示的512字节块位置读取指定文件。
-k Number 从 Number 表示的1KB块位置读取指定文件。
```
File 指定操作的目标文件名称
上述命令中，都涉及到number，假设不指定，默认显示10行。Number前面可使用正负号，表示该偏移从顶部还是从尾部開始计算。
tail可运行文件一般在/usr/bin/以下。
- 监视filename文件的尾部内容（默认10行，相当于增加参数 -n 10），刷新显示在屏幕上。退出，按下CTRL+C
```
tail -f filename
```
- 显示filename最后20行
```
tail -n 20 filename
```
- 逆序显示filename最后10行
```
tail -r -n 10 filename
```

补充：

跟tail功能相似的命令还有：
cat 从第一行開始显示档案内容。
tac 从最后一行開始显示档案内容。
more 分页显示档案内容。
less 与 more 相似，但支持向前翻页
head 仅仅显示前面几行
tail 仅仅显示后面几行
n 带行号显示档案内容
od 以二进制方式显示档案内容


