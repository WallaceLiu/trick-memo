# go test
### 测试所有的文件

将对当前目录下的所有*_test.go文件进行编译并自动运行测试。
```
$ go test
```
### 测试某个文件
```
$ go test –file <你的文件.go>
```
### 测试某个方法
```
$ go test -run="Test_<你的方法名>"
```
### benchmark性能测试

用例文件mysql_b_test.go(文件名必须是*_b_test.go的类型，*代表要测试的文件名，函数名必须以Benchmark开头如：BenchmarkXxx或Benchmark_xxx)。
```
package mysql

import (
    "testing"
)

func Benchmark_findByPk(b *testing.B) {
    for i := 0; i < b.N; i++ { //use b.N for looping
        findByPk(1)
    }
}
```
- 进行所有go文件的benchmark测试
```
$ go test -bench=".*" 或 go test . -bench=".*"
```
- 对某个go文件进行benchmark测试
```
$ go test mysql_b_test.go -bench=".*"
```
