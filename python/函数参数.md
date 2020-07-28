以下是调用函数时可使用的正式参数类型：

- 必需参数
- 关键字参数
- 默认参数
- 不定长参数

### 必需参数

"必需参数"应以正确的顺序传入函数。调用时的数量必须和声明时的一样。
```
def printme( str ):
   "打印任何传入的字符串"
   print (str);
   return;
 
printme();
```
抛出异常：
```
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    printme();
TypeError: printme() missing 1 required positional argument: 'str'
```

### 关键字参数

“关键字参数”使用关键字参数来确定传入的参数值。允许函数调用时参数的顺序与声明时不一致。
```
def printme( str ):
   "打印任何传入的字符串"
   print (str);
   return;
 
printme( str = "菜鸟教程");
```
结果：
```
菜鸟教程
```
以下实例中演示了函数参数的使用不需要使用指定顺序：
```
def printinfo( name, age ):
   print ("名字: ", name);
   print ("年龄: ", age);
   return;
 
printinfo( age=50, name="runoob" );
```
结果：
```
名字:  runoob
年龄:  50
```
### 默认参数

调用函数时，如果没有传递参数，则会使用默认参数。
```
def printinfo( name, age = 35 ):
   print ("名字: ", name);
   print ("年龄: ", age);
   return;
 
printinfo( age=50, name="runoob" );
print ("------------------------")
printinfo( name="runoob" );
```
结果：
```
名字:  runoob
年龄:  50
------------------------
名字:  runoob
年龄:  35
```
### 不定长参数

你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
```
def functionname([formal_args,] *var_args_tuple ):
   function_suite
   return [expression]
```
加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
```
def printinfo( arg1, *vartuple ):
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;
 
printinfo( 10 );
printinfo( 70, 60, 50 );
```
结果：
```
输出:
10
输出:
70
60
50
```