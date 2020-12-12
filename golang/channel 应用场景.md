[golang 中文文档](http://docscn.studygolang.com/doc/)

channel 是 golang 里相当有趣的一个功能，在我使用 golang 编码的经验里，大部分事件都会是在享受 channel 和 goroutine 配合的乐趣。所以本文主要介绍 channel 的一些有趣的用法。

Go编程语言规范里关于 channel（信道）的描述：

> 信道提供了一种机制，它在两个并发执行的函数之间进行同步，并通过传递（与该信道元素类型相符的）值来进行通信。

事实上，可以认为 channel 是一个管道或者先进先出队列，非常简单且轻量。channel 并不是 Golang 首创的。它同样作为内置功能出现在其他语言中。在大多数情况下，它是一个又大、又笨、又复杂的消息队列系统的一个功能。

下面就来一起找点乐子吧！

# 最常见的方式：生产者/消费者

生产者产生一些数据将其放入 channel；然后消费者按照顺序，一个一个的从 channel 中取出这些数据进行处理。这是最常见的 channel 的使用方式。当 channel 的缓冲用尽时，生产者必须等待（阻塞）。换句话说，若是 channel 中没有数据，消费者就必须等待了。

这个例子的源代码在这里。最好下载到本地运行。
```
package main

import (
	"fmt"
	"time"
)

// 生产者
func producer(c chan int64, max int) {
	defer close(c)

	for i := 0; i < max; i++ {
		c <- time.Now().UnixNano()
	}
}
// 消费者
func consumer(c chan int64) {
	var v int64
	ok := true

	for ok {
		if v, ok = <-c; ok {
			fmt.Println(v)
		}
	}
}

func main() {
	var c = make(chan int64, 10)

	go producer(c, 10)

	go consumer(c)

	time.Sleep(time.Second * 10) // 主协程等待足够时间
}
```
结果：
```
1484793678703593129
1484793678703594919
1484793678703595378
1484793678703595430
1484793678703595511
1484793678703595564
1484793678703595619
1484793678703595671
1484793678703595749
1484793678703595802
```
# 自增长 ID 生成器
当生让产者可以顺序的生成整数。它就是一个自增长 ID 生成器。我将这个功能封装成了一个包。并将其代码托管在这里。使用示例可以参考这里的代码。
```
package main

import (
	"fmt"
	"time"
)

type AutoInc struct {
	start, step int
	queue       chan int
	running     bool
}

func New(start, step int) (ai *AutoInc) {
	ai = &AutoInc{
		start:   start,
		step:    step,
		running: true,
		queue:   make(chan int, 4),
	}

	go ai.process()
	return

}

func (ai *AutoInc) process() {
	defer func() { recover() }()
	for i := ai.start; ai.running; i = i + ai.step {
		ai.queue <- i
	}
}

func (ai *AutoInc) Id() int {
	return <-ai.queue
}

func (ai *AutoInc) Close() {
	ai.running = false
	close(ai.queue)
}

func main() {
	i := New(0, 1)

	go i.process()

	fmt.Println(i.Id())
	fmt.Println(i.Id())
	fmt.Println(i.Id())
	fmt.Println(i.Id())

	time.Sleep(10 * time.Second)
}
```
结果：
```
0
1
2
3
```
# 信号量
信号量也是channel的一个有趣的应用。这里有一个来自“effective go”的例子。你应当读过了吧？如果还没有，现在就开始读吧……

我在 Gearman 服务的 API 包 gearman-go 中使用了信号量。在 worker/worker.go 的 232 行，在并行的 Worker.exec 的数量达到 Worker.limit 时，将被阻塞。
```
var sem = make(chan int, MaxOutstanding)

func handle(r *Request) {
    sem <- 1 // 等待放行；
    process(r)
    // 可能需要一个很长的处理过程；
    <-sem // 完成，放行另一个过程。
}

func Serve(queue chan *Request) {
    for {
        req := <-queue
        go handle(req) // 无需等待 handle 完成。
    }
}
```
# 随机序列生成器
当然可以修改自增长 ID 生成器。让生产者生成随机数放入 channel。不过这挺无聊的，不是吗？

这里是随机序列生成器的另一个实现。灵感来自语言规范。它会随机的生成 0/1 序列：
```
func producer(c chan int64, max int) {
    defer close(c)
    for i := 0; i < max; i++ {
        select { // randomized select
        case c <- 0:
        case c <- 1:
        }
    }
}
```
# 超时定时器
当一个 channel 被 read/write 阻塞时，它会被永远阻塞下去，直到 channel 被关闭，这时会产生一个 panic。channel 没有内建用于超时的定时器。并且似乎也没有计划向 channel 添加一个这样的功能。但在大多数情况下，我们需要一个超时机制。例如，由于生产者执行的时候发生了错误，所以没有向 channel 放入数据。消费者会被阻塞到 channel 被关闭。每次出错都关闭 channel？这绝对不是一个好主意。

这里有一个解决方案：
```
package main

import (
	"fmt"
	"time"
)

func main() {
	c := make(chan int64, 5)

	defer close(c)

	timeout := make(chan bool)

	defer close(timeout)

	go func() {
		time.Sleep(1 * time.Second)
		timeout <- true //向超时队列中放入标志
	}()

	select {
	case <-timeout: // 超时
		fmt.Println("timeout...")
	case <-c: // 收到数据
		fmt.Println("Read a date.")
	}
}
```
你注意到 select 语句了吗？哪个 channel 先有数据，哪个分支先执行。因此……还需要更多的解释吗？

这同样被使用在gearman-go 的客户端 API 实现中，第 238 行。

在本文的英文版本发布后，@mjq 提醒我说可以用 time.After。在项目中，这确实是更好的写法。我得向他道谢！同时我也阅读了 src/time/sleep.go 第 74 行，time.After 的实现。其内部实现与上面的代码完全一致。
