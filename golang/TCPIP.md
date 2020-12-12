# server.go
```
package main

import (
	"fmt"
	"net"
	"os"
	"path/filepath"
)

// 处理每个TCPIP连接
func handler(conn net.Conn, messages chan string) {

	fmt.Println("connection is connected from ...", conn.RemoteAddr().String())

	buf := make([]byte, 1024)
	for {
		length, err := conn.Read(buf)
		if err != nil {
			fmt.Println(fmt.Sprintf("Connection,%s", err.Error()))
			os.Exit(-1)
		}

		if length > 0 {
			buf[length] = 0
		}
		//fmt.Println("Rec[",conn.RemoteAddr().String(),"] Say :" ,string(buf[0:lenght]))
		messages <-  string(buf[0:length])
	}
}

// 处理回显
func echo(userConn *map[string]net.Conn, messages chan string) {

	for {
		msg := <-messages
		fmt.Println(msg)

		for key, value := range *userConn {
			fmt.Println("connection is connected from ...", key)
			_, err := value.Write([]byte(msg))
			if err != nil {
				fmt.Println(err.Error())
				delete(*userConn, key)
			}
		}
	}
}

var userConn = make(map[string]net.Conn) // 保存每个连接
var messages = make(chan string, 10)  // 消息通道，用于在服务端回显

func main() {

	if len(os.Args) != 2 {
		fmt.Printf("usage: %s <Server Port>\n", filepath.Base(os.Args[0]))
		fmt.Printf("usage: %s <Server IP Address>:<Server Port>\n", filepath.Base(os.Args[0]))
		fmt.Printf("    eg: chatServer 8888\n")
		fmt.Printf("    eg: chatServer 192.168.0.74:8888\n")
		os.Exit(0)
	}

	addr, err := net.ResolveTCPAddr("tcp4", fmt.Sprintf(":%s", os.Args[1]))
	if err != nil {
		fmt.Println(fmt.Sprintf("ResolveTCPAddr,%s", err.Error()))
		os.Exit(-1)
	}

	listen, err := net.ListenTCP("tcp", addr)
	if err != nil {
		fmt.Println(fmt.Sprintf("ListenTCP,%s", err.Error()))
		os.Exit(-1)
	}

	go echo(&userConn, messages) // 广播线程

	for {
		fmt.Println("Server Listening ...")
		conn, err := listen.Accept()
		if err != nil {
			fmt.Println(fmt.Sprintf("Server Accept,%s", err.Error()))
			os.Exit(-1)
		}

		fmt.Println("Server Accepting ...")
		userConn[conn.RemoteAddr().String()] = conn //

		go handler(conn, messages)
	}
}

```
# client.go
```
package main

import (
	"fmt"
	"net"
	"os"
	"path/filepath"
	"resolve/util"
)

// 客户端发送线程
func chatSend(conn net.Conn) {

	var input string
	username := conn.LocalAddr().String()
	for {

		fmt.Scanln(&input)
		if input == "/quit" {
			fmt.Println("ByeBye..")
			conn.Close()
			os.Exit(0)
		}

		lens, err := conn.Write([]byte(username + " Say :::" + input))
		fmt.Println(lens)
		if err != nil {
			fmt.Println(err.Error())
			conn.Close()
			break
		}
	}
}

func main() {

	if len(os.Args) != 2 {
		fmt.Printf("usage: %s <Server IP Address>:<Server Port>\n", filepath.Base(os.Args[0]))
		fmt.Printf("    eg: chatClient 127.0.0.1:8888\n")
		os.Exit(0)
	}

	tcpAddr, err := net.ResolveTCPAddr("tcp4", os.Args[1])
	if err != nil {
		fmt.Println(fmt.Sprintf("ResolveTCPAddr,%s",err.Error()))
		os.Exit(-1)
	}

	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	if err != nil {
		fmt.Println(fmt.Sprintf("DialTCP,%s",err.Error()))
		os.Exit(-1)
	}

	go chatSend(conn)

	buf := make([]byte, 1024) //开始客户端轮训

	for {

		lenght, err := conn.Read(buf)
		if err != nil {
			fmt.Println(fmt.Sprintf("Connection,%s",err.Error()))
			os.Exit(-1)
		}

		fmt.Println(string(buf[0:lenght]))
	}
}

```