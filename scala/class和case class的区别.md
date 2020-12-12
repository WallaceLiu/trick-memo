case class，就是个普通的class，但与普通的class略有区别，其最重要的特性就是支持模式匹配。

如下：

- case class初始化时可以省略new，普通类一定需要加new。
```
class c1()

case class c2()
```
使用：
```
val o1=new c1
val o2=c2
```
- case class的toString的实现更漂亮。
```
println(o1 toString) // c1@523884b2
println(o2 toString) // c2
```
- case class 默认实现了 equals 和 hashCode。
```
val o11=new c1
val o12=new c2

println(o11 hashCode) // 1379435698
println(o12 hashCode) // 892529689
println(o11 equlas(o12)) // false

val o21=c2
val o22=c2

println(o21 hashCode) // 1757676444
println(o22 hashCode) // 1757676444
println(o21 equlas(o22)) // true
```
- case class默认可序列化，也就是实现了Serializable。
```
val baos = new ByteArrayOutputStream
val oss = new ObjectOutputStream(baos)

oss.writeObject(o21)
```
如果对o11，调用writeObject，就会报错“java.io.NotSerializableException:”
- 自动从scala.Product中继承一些函数，如apply方法。
- case class 构造函数的参数是public级别，可以直接访问。
```
class c1(name: String)

case class c2(name: String)
```
c1的name不能从外部访问，但是c2可以。
- 支持模式匹配。

**case class最重要的特性应该就是支持模式匹配。这也是我们定义case class的唯一理由。**

Scala官方也说：It makes only sense to define case classes if pattern matching is used to decompose data structures.

来看下面的例子：
```
//构造器模式必须将类定义为case class
case class Person(name:String,age:Int)

object ConstructorPattern {
  def main(args: Array[String]): Unit = {
      val p=new Person("少年",27)
      def constructorPattern(p:Person)=p match {
        case Person(name,age) => "Person"
        case _ => "Other"
      }
  }
}
```