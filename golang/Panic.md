# 示例1
```
package main

import (
	"fmt"
)

func main() {
	defer func() {
		fmt.Println("c")
		if err := recover(); err != nil {
			fmt.Println(err)
		}
		fmt.Println("d")
	}()
	f()
}

func f() {
	fmt.Println("a")
	panic(555)
	fmt.Println("b")
	fmt.Println("f")
}
```
输出：
```
a
c
555
d
```
# 示例2
```
package main

// 模拟 try catch 例子
func Try(f func(), handler func(interface{})) {
	defer func() {
		if err := recover(); err != nil {
			handler(err)
		}
	}()
	f()
}

func main() {
	Try(func() {
		panic("foo")
	}, func(e interface{}) {
		print(e)
	})
}
```
输出：
```
(0x56220,0xc42000a100)
```
# 示例3
```
package main

import (
	"fmt"
)

func f() {
	defer func() {
		fmt.Println("inner func defer")
	}()
	fmt.Println("A")
	panic(3)
	//panic方法后的方法、defer定义的方法都无法执行，也包括函数f()后面的任何方法以及defer定义的方法
	defer func() {
		fmt.Println("inner func defer 1")
	}()
	//以下2个不能执行
	fmt.Println("b")
	fmt.Println("c")
}
func main() {
	fmt.Println("Hello World!")
	defer func() {
		fmt.Println("FUCK——1")
	}()
	defer func() {
		fmt.Println("d")
		if err := recover(); err != nil {
			fmt.Println(err)
		}
		fmt.Println("e")
	}()
	defer func() {
		fmt.Println("FUCK——2")
	}()
	f()
	//在f()函数以后的defer函数也不能执行
	defer func() {
		fmt.Println("FUCK——3")
	}()
}
```
输出：
```
Hello World!
A
inner func defer
FUCK——2
d
3
e
FUCK——1
```
# 示例4
```
package main

import (
	"fmt"
)

func f() {
	defer func() {
		fmt.Println("inner func defer")
		if err := recover(); err != nil {
			fmt.Println(err, " fuck")
		}
	}()

	fmt.Println("A")

	panic(3)

	defer func() {
		fmt.Println("inner func defer 1")
	}()

	//以下2个不能执行
	fmt.Println("b")
	fmt.Println("c")
}

func main() {
	fmt.Println("Hello World!")

	defer func() {
		fmt.Println("FUCK——1")
	}()

	defer func() {
		fmt.Println("d")
		if err := recover(); err != nil {
			fmt.Println(err)
		}
		fmt.Println("e")
	}()

	defer func() {
		fmt.Println("FUCK——2")
	}()

	f()

	//在f()函数以后的defer函数也不能执行
	defer func() {
		fmt.Println("FUCK——3")
	}()
}
```
输出：
```
Hello World!
A
inner func defer
3  fuck
FUCK——3
FUCK——2
d
e
FUCK——1
```