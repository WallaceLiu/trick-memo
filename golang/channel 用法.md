# Golang并发基础理论
Golang在并发设计方面参考了C.A.R Hoare的CSP，即Communicating Sequential Processes并发模型理论。但就像John Graham-Cumming所说的那样，多数Golang程序员或爱好者仅仅停留在“知道”这一层次，理解CSP理论的并不多，毕竟多数程序员是搞工程 的。不过要想系统学习CSP的人可以从[这里](http://www.usingcsp.com/)下载到CSP论文的最新版本。

[维基百科](http://en.wikipedia.org/wiki/Communicating_sequential_processes)中概要罗列了CSP模型与另外一种并发模型Actor模型的区别。

Actor模型广义上讲与CSP模型很相似。但两种模型就提供的原语而言，又有一些根本上的不同之处：
- CSP模型处理过程是匿名的，而Actor模型中的Actor则具有身份标识。
- CSP模型的消息传递在收发消息进程间包含了一个交会点，即发送方只能在接收方准备好接收消息时才能发送消息。相反，actor模型中的消息传递是异步的，即消息的发送和接收无需在同一时间进行，发送方可以在接收方准备好接收消息前将消息发送出去。这两种方案可以认为是彼此对偶的。在某种意义下，基于交会点的系统可以通过构造带缓冲的通信的方式来模拟异步消息系统。而异步系统可以通过构造带消息/应答协议的方式来同步发送方和接收方来模拟交会点似的通信方式。
- CSP使用显式的Channel用于消息传递，而Actor模型则将消息发送给命名的目的Actor。这两种方法可以被认为是对偶的。某种意义下，进程可 以从一个实际上拥有身份标识的channel接收消息，而通过将actors构造成类Channel的行为模式也可以打破actors之间的名字耦合。

# Go Channel基本操作语法
Go Channel的基本操作语法如下：
```
c := make(chan bool) //创建一个无缓冲的bool型Channel
c <- x        //向一个Channel发送一个值
<- c          //从一个Channel中接收一个值
x = <- c      //从Channel c接收一个值并将其存储到x中
x, ok = <- c  //从Channel接收一个值，如果channel关闭了或没有数据，那么ok将被置为false
```
++**不带缓冲的Channel兼具通信和同步两种特性，颇受青睐。**++

# Channel用作信号(Signal)的场景
### 等待一个事件(Event)

等待一个事件，有时候通过close一个Channel就足够了。例如：
```
package main

import "fmt"

func main() {
	fmt.Println("Begin doing something!")
	c := make(chan bool)
	go func() {
		fmt.Println("Doing something…")
		close(c)
		//c <- true
	}()
	<-c // channle 里无数据，会一直阻塞在这里
	fmt.Println("Done!")
}
```
主协程通过“<-c”来等待子协程中的“事件完成”，子协程通过关闭channel将促发这一事件。

当然，也可以通过向Channel写入一个bool值作为事件通知。

++**主协程在channel c上没有任何数据可读的情况下会阻塞等待。**++

根据《Go memory model》中关于close channel与recv from channel的order的定义：
> The closing of a channel happens before a receive that returns a zero value because the channel is closed.

结果：
```
Begin doing something!
Doing something…
Done!
```
如果将close(c)换成“c<-true”，则根据《Go memory model》中的定义：
> A receive from an unbuffered channel happens before the send on that channel completes.

"<-c"要先于"c<-true"完成，但也不影响日志的输出顺序，输出结果仍为上面三行。

### 协同多个Goroutines
close channel还可以用于协同多个Goroutines。

下面例子，创建100个Worker协程，这些协程被创建后都阻塞在"<-start"上，直到我们在主协程中给出开工的信号："close(start)"，这些goroutines才开始真正的并发运行起来。
```
package main

import "fmt"

func worker(start chan bool, index int) {
	<-start
	fmt.Println("This is Worker:", index)
}
func main() {
	start := make(chan bool)
	for i := 1; i <= 100; i++ {
		go worker(start, i)
	}
	close(start)
	select {} //deadlock we expected
}
```
### Select
- select的基本操作

select是Go语言特有的操作，可以同时在多个channel上进行发送/接收操作。下面是select的基本操作。
```
	select {
	case x := <-somechan:
		// … 使用x进行一些操作
	case y, ok := <-someOtherchan:
		// … 使用y进行一些操作，
		// 检查ok值判断someOtherchan是否已经关闭
	case outputChan <- z:
		// … z值被成功发送到Channel上时
	default:
		// … 上面case均无法通信时，执行此分支
	}
```
- 惯用法：for/select

实际中很多对select进行一次evaluation，常常将其与for {}结合，并选择适当时机从for{}中退出。
```
for {
        select {
        case x := <- somechan:
            // … 使用x进行一些操作
        case y, ok := <- someOtherchan:
            // … 使用y进行一些操作，
            // 检查ok值判断someOtherchan是否已经关闭
        case outputChan <- z:
            // … z值被成功发送到Channel上时
        default:
            // … 上面case均无法通信时，执行此分支
        }
}
```
示例：
```
package main

import (
	"fmt"
)

func main() {
	length := 5
	c := make(chan int, length)

	for i := 0; i < length; i++ {
		select {
		case c <- 1:
		case c <- 2:
		case c <- 3:
		}
	}

	for i := 0; i < length; i++ {
		fmt.Printf("%v\n", <-c)
	}
}
```
- 终结workers

下面是一个常见的终结子worker协程的方法，每个worker goroutine通过select监视一个die channel来及时获取main goroutine的退出通知。
```
package main

import (
	"fmt"
	"time"
)

func worker(die chan bool, index int) {
	fmt.Println("Begin: This is Worker:", index)
	for {
		select {
		case <-die:
			fmt.Println("Done: This is Worker:", index)
			return
		}
	}
}

func main() {
	die := make(chan bool)
	for i := 1; i <= 100; i++ {
		go worker(die, i)
	}

	time.Sleep(time.Second * 5)
	close(die)
	select {}
}
```
- 终结验证

有时，终结一个worker后，主协程想确认worker协程是否真正退出了，可采用下面这种方法：
```
package main

import (
	"fmt"
)

func worker(die chan bool) {
	fmt.Println("Begin: This is Worker")
	for {
		select {
		case <-die:
			fmt.Println("Done: This is Worker")
			die <- true // 子协程告诉主协程
			return
		}
	}
}

func main() {
	die := make(chan bool)
	go worker(die)
	die <- true // 主协程告诉子协程
	<-die
	fmt.Println("Worker goroutine has been terminated")
}
```
结果：
```
Begin: This is Worker
Done: This is Worker
Worker goroutine has been terminated
```
- 关闭的Channel永远不会阻塞

在一个已经关闭了的channel上读写的结果：
```
package main

import "fmt"

func main() {
	cb := make(chan bool)
	close(cb)

	x := <-cb
	fmt.Printf("%#v\n", x)

	x, ok := <-cb
	fmt.Printf("%#v %#v\n", x, ok)

	ci := make(chan int)
	close(ci)

	y := <-ci
	fmt.Printf("%#v\n", y)

	cb <- true
}

```
结果：
```
false
false false
0
panic: runtime error: send on closed channel
```
在一个已经close的非缓存 的channel上执行读操作，回返回channel对应类型的零值，比如bool型channel返回false，int型channel返回0。

但向close的channel写则会触发panic。

不过无论读写都不会导致阻塞。

- 关闭带缓存的channel

将unbuffered channel换成buffered channel会怎样？我们看下面例子：
```
package main

import "fmt"

func main() {
	c := make(chan int, 3)
	c <- 15
	c <- 34
	c <- 65
	close(c)

	fmt.Printf("%d\n", <-c)
	fmt.Printf("%d\n", <-c)
	fmt.Printf("%d\n", <-c)
	fmt.Printf("%d\n", <-c)
	c <- 1
}

```
结果：
```
15
34
65
0
panic: runtime error: send on closed channel
```
尽管已经close了，但我们依旧可以从中读出关闭前写入的3个值。第四次读取时，则会返回该channel类型的零值。向这类channel写入操作也会触发panic。

- range

range常被用来从channel中读取所有值。下面是一个简单的实例：
```
package main

import "fmt"

func generator(strings chan string) {
	strings <- "Five hour's New York jet lag"
	strings <- "and Cayce Pollard wakes in Camden Town"
	strings <- "to the dire and ever-decreasing circles"
	strings <- "of disrupted circadian rhythm."
	close(strings)
}

func main() {
	strings := make(chan string)

	go generator(strings)

	for s := range strings {
		fmt.Printf("%s\n", s)
	}

	fmt.Printf("\n")
}
```
结果：
```
Five hour's New York jet lag
and Cayce Pollard wakes in Camden Town
to the dire and ever-decreasing circles
of disrupted circadian rhythm.
```
# 隐藏状态
下面通过一个例子来演示一下channel如何用来隐藏状态：
- 例子：唯一的ID服务
```
package main

import "fmt"

func newUniqueIDService() <-chan string {
	id := make(chan string)
	go func() {
		var counter int64 = 0
		for {
			id <- fmt.Sprintf("%x", counter)
			counter += 1
		}
	}()
	return id
}

func main() {
	id := newUniqueIDService()
	
	for i := 0; i < 10; i++ {
		fmt.Println(<-id)
	}
}
```
结果：
```
0
1
2
3
4
5
6
7
8
9
```
newUniqueIDService通过一个channel与main goroutine关联，主协程无需知道uniqueid实现的细节以及当前状态，只需通过channel获得最新id即可。

# 默认情况
我想这里John Graham-Cumming主要是想告诉我们select的default分支的实践用法。
- select  for non-blocking receive
```
idle:= make(chan []byte, 5) //用一个带缓冲的channel构造一个简单的队列
select {
case b = <-idle:  //尝试从idle队列中读取
    …
default:  //队列空，分配一个新的buffer
        makes += 1
        b = make([]byte, size)
}
```
- select for non-blocking send
```
idle:= make(chan []byte, 5) //用一个带缓冲的channel构造一个简单的队列
select {
case idle <- b: //尝试向队列中插入一个buffer
        //…
default: //队列满？
}
```
# Nil Channels
- nil channels阻塞

对一个没有初始化的channel进行读写操作都将发生阻塞，例子如下：
```
package main
func main() {
        var c chan int
        <-c
}
```
```
$go run testnilchannel.go
fatal error: all goroutines are asleep – deadlock!
```
```
package main
func main() {
        var c chan int
        c <- 1
}
```
```
$go run testnilchannel.go
fatal error: all goroutines are asleep – deadlock!
```
- nil channel
在select中很有用，看下面这个例子：
```
//testnilchannel_bad.go
package main
import "fmt"
import "time"
func main() {
        var c1, c2 chan int = make(chan int), make(chan int)
        go func() {
                time.Sleep(time.Second * 5)
                c1 <- 5
                close(c1)
        }()
        go func() {
                time.Sleep(time.Second * 7)
                c2 <- 7
                close(c2)
        }()
        for {
                select {
                case x := <-c1:
                        fmt.Println(x)
                case x := <-c2:
                        fmt.Println(x)
                }
        }
        fmt.Println("over")
}
```
我们原本期望程序交替输出5和7两个数字，但实际的输出结果却是：
```
5
0
0
0

… … 0
```
死循环
再仔细分析代码，原来select每次按case顺序evaluate：
1. 前5s，select一直阻塞；
1. 第5s，c1返回一个5后被close了，“case x := <-c1”这个分支返回，select输出5，并重新select
1. 下一轮select又从“case x := <-c1”这个分支开始evaluate，由于c1被close，按照前面的知识，close的channel不会阻塞，我们会读出这个 channel对应类型的零值，这里就是0；select再次输出0；这时即便c2有值返回，程序也不会走到c2这个分支
1. 依次类推，程序无限循环的输出0

我们利用nil channel来改进这个程序，以实现我们的意图，代码如下：
```
//testnilchannel.go
package main
import "fmt"
import "time"
func main() {
        var c1, c2 chan int = make(chan int), make(chan int)
        go func() {
                time.Sleep(time.Second * 5)
                c1 <- 5
                close(c1)
        }()
        go func() {
                time.Sleep(time.Second * 7)
                c2 <- 7
                close(c2)
        }()
        for {
                select {
                case x, ok := <-c1:
                        if !ok {
                                c1 = nil
                        } else {
                                fmt.Println(x)
                        }
                case x, ok := <-c2:
                        if !ok {
                                c2 = nil
                        } else {
                                fmt.Println(x)
                        }
                }
                if c1 == nil && c2 == nil {
                        break
                }
        }
        fmt.Println("over")
}
```
```
$go run testnilchannel.go
5
7
over
```
可以看出：通过将已经关闭的channel置为nil，下次select将会阻塞在该channel上，使得select继续下面的分支evaluation。
# Timers
- 超时机制Timeout
带超时机制的select是常规的tip，下面是示例代码，实现30s的超时select：
```
func worker(start chan bool) {
        timeout := time.After(30 * time.Second)
        for {
                select {
                     // … do some stuff
                case <- timeout:
                    return
                }
        }
}
```
- 心跳HeartBeart
与timeout实现类似，下面是一个简单的心跳select实现：
```
func worker(start chan bool) {
        heartbeat := time.Tick(30 * time.Second)
        for {
                select {
                     // … do some stuff
                case <- heartbeat:
                    //… do heartbeat stuff
                }
        }
}
```