golang有两个非常大的特性，那就是goruntime与channel，这两个特性直接将开发人员从并发和线程同步中解放了出来，使高并发和线程同步之间代码的编写变得异常简单，并且占用资源少，同步传输效率高。

资源占用方面，goroutine 会从4096字节的初始栈内存占用开始按需增长或缩减内存占用。

程序创建了10万0，1个无缓冲channel, 10万个goruntime。

数据在goruntime中从第一个channel流向最后一个channel，每流入一次数值增1。
```
package main

import (
	"fmt"
	"time"
)

func chanFlow(left, right chan int, bufferLen int) {
	// 增加1
	if bufferLen <= 0 {
		left <- 1 + <-right
	} else {
		for i := 0; i < bufferLen; i++ {
			left <- 1 + <-right
		}
	}
}

func main() {
	cnt := 2 //100000
	var left chan int = nil
	lastChan := make(chan int)
	right := lastChan

	begin := time.Now()

	fmt.Println("begin at:", begin)
	for i := 0; i < cnt; i++ {
		left, right = right, make(chan int) // left 指向 right，right 指向新channel
		go chanFlow(left, right, 0)
	}
	right <- 0
	result := <-lastChan

	end := time.Now()
	fmt.Println("end   at:", end, time.Since(begin))
	fmt.Println(result)
}
```
结果：
```
begin at: 2017-01-19 11:41:23.181150907 +0800 CST
end   at: 2017-01-19 11:41:23.832569003 +0800 CST 651.418195ms
```
半秒多。

上面的例子中使用的是无缓冲的channel，把代码修改为带1000个单位缓冲的channel再试试看，代码如下：
```
package main

import (
	"fmt"
	"time"
)

func chanFlow2(left, right chan int, bufferLen int) {
	if bufferLen <= 0 {
		left <- 1 + <-right
	} else {
		for i := 0; i < bufferLen; i++ {
			left <- 1 + <-right
		}
	}
}
func main() {
	nruntime := 100000
	chanBuffer := 1000
	result := make([]int, 0, 100)
	lastChan := make(chan int, chanBuffer)
	var left chan int = nil
	right := lastChan
	begin := time.Now()
	fmt.Println("begin at:", begin)
	for i := 0; i < nruntime; i++ {
		left, right = right, make(chan int, chanBuffer)
		go chanFlow2(left, right, chanBuffer)
	}
	for i := 0; i < chanBuffer; i++ {
		right <- 0
	}
	for i := 0; i < chanBuffer; i++ {
		result = append(result, <-lastChan)
	}
	end := time.Now()
	fmt.Println("end   at:", end, time.Since(begin))
	fmt.Println(result)
}

```
结果：
```
begin at: 2017-01-19 11:46:01.303385369 +0800 CST
end   at: 2017-01-19 11:46:04.82743168 +0800 CST 3.524047873s
```
而在实际生产中，更多的需要传递的数据是字符串，那么现在把代码再修改一下试试，代码如下：
```
package main

import (
	"crypto/rand"
	"encoding/base64"
	"fmt"
	"io"
	"time"
)

func chanFlow3(left, right chan string, bufferLen int) {
	if bufferLen <= 0 {
		left <- <-right
	} else {
		for i := 0; i < bufferLen; i++ {
			left <- <-right
		}
	}
}

func genString() string {
	b := make([]byte, 32)
	if _, err := io.ReadFull(rand.Reader, b); err != nil {
		return ""
	} else {
		return base64.URLEncoding.EncodeToString(b)
	}
}

func main() {
	nruntime := 100000
	chanBuffer := 1000
	result := make([]string, 0, 100)
	lastChan := make(chan string, chanBuffer)
	dataForChan := make([]string, 0, chanBuffer)
	for i := 0; i < chanBuffer; i++ {
		dataForChan = append(dataForChan, genString())
	}
	var left chan string = nil
	right := lastChan
	begin := time.Now()
	fmt.Println("begin at:", begin)
	for i := 0; i < nruntime; i++ {
		left, right = right, make(chan string, chanBuffer)
		go chanFlow3(left, right, chanBuffer)
	}

	for i := 0; i < chanBuffer; i++ {
		right <- dataForChan[i]
	}
	for i := 0; i < chanBuffer; i++ {
		result = append(result, <-lastChan)
	}
	end := time.Now()
	fmt.Println("end   at:", end, time.Since(begin))
	fmt.Println(result)
}

```
结果：
```
begin at: 2017-01-19 11:50:22.894522162 +0800 CST
end   at: 2017-01-19 11:50:27.755387488 +0800 CST 4.860865517s
```
4秒，1000个44字节的随机字符串在10万个goruntime中穿过了10万0，1个channel。

而1万个44字节的随机字符串在1万个goruntime中穿过了1万0，1个channel耗时约为5秒。

以上可以看出，golang中数据在goruntime中通过channel同步的效率非常高。
