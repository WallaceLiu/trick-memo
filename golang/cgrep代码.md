# cgrep 01
```
package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"log"
	"os"
	"regexp"
	"runtime"
)

var workers = runtime.NumCPU()

type Result struct {
	filename string
	lino     int
	line     string
}

type Job struct {
	filename string
	results  chan<- Result
}

// 对每个文件执行该方法
func (job Job) Do(lineRx *regexp.Regexp) {

	file, err := os.Open("/Users/cap/IdeaProjects/goworkspace/hellogo/src/cgrep01/" + job.filename)
	if err != nil {
		log.Printf("error: %s\n", err)
		return
	}

	defer file.Close()
	reader := bufio.NewReader(file)
	for lino := 1; ; lino++ {
		line, err := reader.ReadBytes('\n')
		line = bytes.TrimRight(line, "\n\r")
		if lineRx.Match(line) {
			job.results <- Result{job.filename, lino, string(line)}
		}
		if err != nil {
			if err != io.EOF {
				log.Printf("error:%d: %s\n", lino, err)
			}
			break
		}
	}
}

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU()) // Use all the machine's cores

	if lineRx, err := regexp.Compile(`\w+`); err != nil {
		log.Fatalf("invalid regexp: %s\n", err)
	} else {
		grep(lineRx, []string{"t1.dat", "t2.dat"})

		fmt.Println("done.")
	}
}

func grep(lineRx *regexp.Regexp, filenames []string) {

	jobs := make(chan Job, workers)
	results := make(chan Result, minimum(1000, len(filenames)))
	done := make(chan struct{}, workers)

	go addJobs(jobs, filenames, results) // Executes in its own goroutine

	for i := 0; i < workers; i++ {
		go doJobs(done, lineRx, jobs) // Each executes in its own goroutine
	}

	go awaitCompletion(done, results) // Executes in its own goroutine

	processResults(results) // Blocks until the work is done


}

func addJobs(jobs chan<- Job, filenames []string, results chan<- Result) {
	for _, filename := range filenames {
		jobs <- Job{filename, results}
	}
	close(jobs)
}

func doJobs(done chan<- struct{}, lineRx *regexp.Regexp, jobs <-chan Job) {
	for job := range jobs {
		job.Do(lineRx)
	}
	done <- struct{}{}
}

func awaitCompletion(done <-chan struct{}, results chan Result) {
	for i := 0; i < workers; i++ {
		<-done
	}
	close(results)
}

func processResults(results <-chan Result) {
	for result := range results {
		fmt.Printf("%s:%d:%s\n", result.filename, result.lino, result.line)
	}
}

func minimum(x int, ys ...int) int {
	for _, y := range ys {
		if y < x {
			x = y
		}
	}
	return x
}
```
# cgrep 02
```
// Copyright © 2011-12 Qtrac Ltd.
//
// This program or package and any associated files are licensed under the
// Apache License, Version 2.0 (the "License"); you may not use these files
// except in compliance with the License. You can get a copy of the License
// at: http://www.apache.org/licenses/LICENSE-2.0.
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// The approach taken here was inspired by an example on the gonuts mailing
// list by Roger Peppe.

package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"log"
	"os"
	"regexp"
	"runtime"
)

var workers = runtime.NumCPU()

type Result struct {
	filename string
	lino     int
	line     string
}

type Job struct {
	filename string
	results  chan<- Result
}

func (job Job) Do(lineRx *regexp.Regexp) {
	file, err := os.Open("/Users/cap/IdeaProjects/goworkspace/hellogo/src/cgrep02/" + job.filename)
	if err != nil {
		log.Printf("error: %s\n", err)
		return
	}
	defer file.Close()
	reader := bufio.NewReader(file)
	for lino := 1; ; lino++ {
		line, err := reader.ReadBytes('\n')
		line = bytes.TrimRight(line, "\n\r")
		if lineRx.Match(line) {
			job.results <- Result{job.filename, lino, string(line)}
		}
		if err != nil {
			if err != io.EOF {
				log.Printf("error:%d: %s\n", lino, err)
			}
			break
		}
	}
}

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU()) // Use all the machine's cores

	if lineRx, err := regexp.Compile(`\w+`); err != nil {
		log.Fatalf("invalid regexp: %s\n", err)
	} else {
		grep(lineRx, []string{"t1.dat", "t2.dat","t3.dat"})

		fmt.Println("done")
	}
}

func grep(lineRx *regexp.Regexp, filenames []string) {
	jobs := make(chan Job, workers) // 8
	results := make(chan Result, minimum(1000, len(filenames)))
	done := make(chan struct{}, workers) // 8

	go addJobs(jobs, filenames, results)

	for i := 0; i < workers; i++ {
		go doJobs(done, lineRx, jobs)
	}

	waitAndProcessResults(done, results)
}

func addJobs(jobs chan<- Job, filenames []string, results chan<- Result) {
	for _, filename := range filenames {
		jobs <- Job{filename, results} // 添加不进去时，会阻塞
	}
	close(jobs) // 所有文件添加到jobs后，并且被取出去，会关闭jobs通道
}

func doJobs(done chan<- struct{}, lineRx *regexp.Regexp, jobs <-chan Job) {
	for job := range jobs {
		//fmt.Println("do ",job)
		job.Do(lineRx)
	}
	done <- struct{}{}
}

func waitAndProcessResults(done <-chan struct{}, results <-chan Result) {
	for working := workers; working > 0; {
		select { // Blocking
		case result := <-results:
			fmt.Printf("waitAndProcessResults Blocking %s:%d:%s 111111111\n", result.filename, result.lino,
				result.line)
		case <-done:
			fmt.Println("DONE...")
			working--
		}
	}
DONE:
	for {
		select { // Nonblocking
		case result := <-results:
			fmt.Printf("waitAndProcessResults Nonblocking %s:%d:%s\n", result.filename, result.lino,
				result.line)
		default:
		fmt.Println("DONE")
			break DONE
		}
	}
}

func minimum(x int, ys ...int) int {
	for _, y := range ys {
		if y < x {
			x = y
		}
	}
	return x
}
```
# cgrep 03
```
// Copyright © 2011-12 Qtrac Ltd.
//
// This program or package and any associated files are licensed under the
// Apache License, Version 2.0 (the "License"); you may not use these files
// except in compliance with the License. You can get a copy of the License
// at: http://www.apache.org/licenses/LICENSE-2.0.
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// The approach taken here was inspired by an example on the gonuts mailing
// list by Roger Peppe.

package main

import (
	"bufio"
	"bytes"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"regexp"
	"runtime"
	"time"
)

var workers = runtime.NumCPU()

type Result struct {
	filename string
	lino     int
	line     string
}

type Job struct {
	filename string
	results  chan<- Result
}

func (job Job) Do(lineRx *regexp.Regexp) {
	file, err := os.Open("/Users/cap/IdeaProjects/goworkspace/hellogo/src/cgrep03/" + job.filename)
	if err != nil {
		log.Printf("error: %s\n", err)
		return
	}
	defer file.Close()
	reader := bufio.NewReader(file)
	for lino := 1; ; lino++ {
		line, err := reader.ReadBytes('\n')
		line = bytes.TrimRight(line, "\n\r")
		if lineRx.Match(line) {
			job.results <- Result{job.filename, lino, string(line)}
		}
		if err != nil {
			if err != io.EOF {
				log.Printf("error:%d: %s\n", lino, err)
			}
			break
		}
	}
}

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU()) // Use all the machine's cores
	log.SetFlags(0)

	// 超时 指针？
	var timeoutOpt *int64 = flag.Int64("timeout", 0, "seconds (0 means no timeout)")
	flag.Parse()
	if *timeoutOpt < 0 || *timeoutOpt > 240 {
		log.Fatalln("timeout must be in the range [0,240] seconds")
	}

	if lineRx, err := regexp.Compile(`\w+`); err != nil {
		log.Fatalf("invalid regexp: %s\n", err)
	} else {
		var timeout int64 = 1e9 * 60 * 10 // 10 minutes!
		if *timeoutOpt != 0 {
			timeout = *timeoutOpt * 1e9
		}

		//
		grep(timeout, lineRx, []string{"t1.dat", "t2.dat"})
	}
}

func grep(timeout int64, lineRx *regexp.Regexp, filenames []string) {
	jobs := make(chan Job, workers)                             // 任务，CPU核数
	results := make(chan Result, minimum(1000, len(filenames))) // 结果，文件列表大小和1000，取最小的
	done := make(chan struct{}, workers)                        // 完成

	go addJobs(jobs, filenames, results)

	for i := 0; i < workers; i++ {
		go doJobs(done, lineRx, jobs)
	}

	waitAndProcessResults(timeout, done, results)
}

// 一个协程，把文件列表的文件添加到job中
//
func addJobs(jobs chan<- Job, filenames []string, results chan<- Result) {
	for _, filename := range filenames {
		jobs <- Job{filename, results}
	}

	close(jobs)
}

// 另一个协程，处理文件
func doJobs(done chan<- struct{}, lineRx *regexp.Regexp, jobs <-chan Job) {
	for job := range jobs {
		job.Do(lineRx)
	}

	done <- struct{}{} // 处理完后，写入完成channel
}

// 等待所有任务完成
func waitAndProcessResults(timeout int64, done <-chan struct{},
	results <-chan Result) {
	finish := time.After(time.Duration(timeout))
	for working := workers; working > 0; {
		select { // Blocking
		case result := <-results:
			fmt.Printf("%s:%d:%s\n", result.filename, result.lino,
				result.line)
		case <-finish:
			fmt.Println("timed out")
			return // Time's up so finish with what results there were
		case <-done:
			working--
		}
	}
	for {
		select { // Nonblocking
		case result := <-results:
			fmt.Printf("%s:%d:%s\n", result.filename, result.lino,
				result.line)
		case <-finish:
			fmt.Println("timed out")
			return // Time's up so finish with what results there were
		default:
			return
		}
	}
}

func minimum(x int, ys ...int) int {
	for _, y := range ys {
		if y < x {
			x = y
		}
	}
	return x
}
```