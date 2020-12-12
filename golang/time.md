```
const (
    43        ANSIC       = "Mon Jan _2 15:04:05 2006"
    44        UnixDate    = "Mon Jan _2 15:04:05 MST 2006"
    45        RubyDate    = "Mon Jan 02 15:04:05 -0700 2006"
    46        RFC822      = "02 Jan 06 15:04 MST"
    47        RFC822Z     = "02 Jan 06 15:04 -0700" // RFC822 with numeric zone
    48        RFC850      = "Monday, 02-Jan-06 15:04:05 MST"
    49        RFC1123     = "Mon, 02 Jan 2006 15:04:05 MST"
    50        RFC1123Z    = "Mon, 02 Jan 2006 15:04:05 -0700" // RFC1123 with numeric zone
    51        RFC3339     = "2006-01-02T15:04:05Z07:00"
    52        RFC3339Nano = "2006-01-02T15:04:05.999999999Z07:00"
    53        Kitchen     = "3:04PM"
    54        // Handy time stamps.
    55        Stamp      = "Jan _2 15:04:05"
    56        StampMilli = "Jan _2 15:04:05.000"
    57        StampMicro = "Jan _2 15:04:05.000000"
    58        StampNano  = "Jan _2 15:04:05.000000000"
    59    )
```
示例
```
package main

import (
    "fmt"
    "time"
)

func main() {

    p := fmt.Println

    t := time.Now()
    p(t.Format(time.RFC3339))

    t1, e := time.Parse(time.RFC3339, "2012-11-01T22:08:41+00:00")
    p(t1)
    p(e)

    p(t.Format("3:04PM"))
    p(t.Format("Mon Jan _2 15:04:05 2006"))
    p(t.Format("2006-01-02T15:04:05.999999-07:00"))
    form := "3 04 PM"
    t2, e := time.Parse(form, "8 41 PM")
    p(t2)

    fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n", t.Year(), t.Month(), t.Day(), t.Hour(), t.Minute(), t.Second())

    ansic := "Mon Jan _2 15:04:05 2006"
    _, e = time.Parse(ansic, "8:41PM")
    p(e)

}
```
结果
```
2015-03-26T13:17:25+08:00
2012-11-01 22:08:41 +0000 +0000
<nil>
1:17PM
Thu Mar 26 13:17:25 2015
2015-03-26T13:17:25.012512+08:00
0000-01-01 20:41:00 +0000 UTC
2015-03-26T13:17:25-00:00
parsing time "8:41PM" as "Mon Jan _2 15:04:05 2006": cannot parse "8:41PM" as "Mon"
```