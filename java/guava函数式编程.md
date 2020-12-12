# Functions[函数]和Predicates[断言]
Guava提供两个基本的函数式接口：

- Function<A, B>，它声明了单个方法B apply(A input)。Function对象通常被预期为引用透明的——没有副作用——并且引用透明性中的”相等”语义与equals一致，如a.equals(b)意味着function.apply(a).equals(function.apply(b))。
- Predicate<T>，它声明了单个方法boolean apply(T input)。Predicate对象通常也被预期为无副作用函数，并且”相等”语义与equals一致。

## Functions、Predicates
Functions提供简便的Function构造和操作方法：

函数|说明
---|---
forMap(Map<A, B>)|-	
compose(Function<B, C>, Function<A, B>)	|-
constant(T)|-
identity()	|-
toStringFunction()|-	

Predicates提供如下函数：
函数|说明
---|---
instanceOf(Class)|-	
assignableFrom(Class)|-	
contains(Pattern)|-
in(Collection)|-
isNull()|-
alwaysFalse()|-
alwaysTrue()|-
equalTo(Object)|-
compose(Predicate, Function)|-
and(Predicate...)|-
or(Predicate...)|-
not(Predicate)|-

## 函数式编程
### 断言

断言的最基本应用就是过滤集合。所有Guava过滤方法都返回”视图”。

集合类型|	过滤方法
---|---
Iterable|	Iterables.filter(Iterable,Predicate)
-|FluentIterable.filter(Predicate)
Iterator|	Iterators.filter(Iterator, Predicate)
Collection|	Collections2.filter(Collection, Predicate)
Set	|Sets.filter(Set, Predicate)
SortedSet|	Sets.filter(SortedSet, Predicate)
Map|	Maps.filterKeys(Map, Predicate)
-|Maps.filterValues(Map, Predicate)
-|Maps.filterEntries(Map, Predicate)
SortedMap|	Maps.filterKeys(SortedMap, Predicate)
-|Maps.filterValues(SortedMap, Predicate)
-|Maps.filterEntries(SortedMap, Predicate)
Multimap|	Multimaps.filterKeys(Multimap,Predicate)
-|Multimaps.filterValues(Multimap,Predicate)
-|Multimaps.filterEntries(Multimap, Predicate)

> List的过滤视图被省略了，因为不能有效地支持类似get(int)的操作。请改用Lists.newArrayList(Collections2.filter(list, predicate))做拷贝过滤。

>除了简单过滤，Guava另外提供了若干用Predicate处理Iterable的工具——通常在Iterables工具类中，或者是FluentIterable的”fluent”（链式调用）方法。

Iterables方法签名|	说明|	另请参见
boolean all(Iterable, Predicate)|是否所有元素满足断言？懒实现：如果发现有元素不满足，不会继续迭代
boolean any(Iterable, Predicate)|是否有任意元素满足元素满足断言？懒实现：只会迭代到发现满足的元素
T find(Iterable, Predicate)|循环并返回一个满足元素满足断言的元素，如果没有则抛出NoSuchElementException
Optional<T> tryFind(Iterable, Predicate)|返回一个满足元素满足断言的元素，若没有则返回Optional.absent()	
indexOf(Iterable, Predicate)|返回第一个满足元素满足断言的元素索引值，若没有返回-1	
removeIf(Iterable, Predicate)|移除所有满足元素满足断言的元素，实际调用Iterator.remove()方法

### 函数
集合类型|	转换方法
---|---
Iterable|	Iterables.transform(Iterable, Function)
-|FluentIterable.transform(Function)
Iterator|	Iterators.transform(Iterator, Function)
Collection|	Collections2.transform(Collection, Function)
List	|Lists.transform(List, Function)
Map*	|Maps.transformValues(Map, Function)
-|Maps.transformEntries(Map, EntryTransformer)
SortedMap*|	Maps.transformValues(SortedMap, Function)
-|Maps.transformEntries(SortedMap, EntryTransformer)
Multimap*|	Multimaps.transformValues(Multimap, Function)
-|Multimaps.transformEntries(Multimap, EntryTransformer)
ListMultimap*	|Multimaps.transformValues(ListMultimap, Function)
-|Multimaps.transformEntries(ListMultimap, EntryTransformer)
Table|	Tables.transformValues(Table, Function)

*Map和Multimap有特殊的方法，其中有个EntryTransformer<K, V1, V2>参数，它可以使用旧的键值来计算，并且用计算结果替换旧值。

*对Set的转换操作被省略了，因为不能有效支持contains(Object)操作——译者注：懒视图实际上不会全部计算转换后的Set元素，因此不能高效地支持contains(Object)。请改用Sets.newHashSet(Collections2.transform(set, function))进行拷贝转换。

假设Person类：
```
package com.baobaotao.web.domain;

public class Person {
	private Integer c1;
	private Integer c2;
	private String c3;
	private String c4;
	private Integer c5;
	private Integer c6;

	public Person(Integer c1, Integer c2, String c3, String c4, Integer c5,
			Integer c6) {
		this.c1 = c1;
		this.c2 = c2;
		this.c3 = c3;
		this.c4 = c4;
		this.c5 = c5;
		this.c6 = c6;
	}

	public Integer getC1() {
		return c1;
	}

	public void setC1(Integer c1) {
		this.c1 = c1;
	}

	public Integer getC2() {
		return c2;
	}

	public void setC2(Integer c2) {
		this.c2 = c2;
	}

	public String getC3() {
		return c3;
	}

	public void setC3(String c3) {
		this.c3 = c3;
	}

	public String getC4() {
		return c4;
	}

	public void setC4(String c4) {
		this.c4 = c4;
	}

	public Integer getC5() {
		return c5;
	}

	public void setC5(Integer c5) {
		this.c5 = c5;
	}

	public Integer getC6() {
		return c6;
	}

	public void setC6(Integer c6) {
		this.c6 = c6;
	}

}

```
示例1：
```
		Function<Double, Double> sqrt = new Function<Double, Double>() {
			public Double apply(Double input) {
				return Math.sqrt(input);
			}
		};

		Double r = sqrt.apply(4.0);
```
```
		Function<Date, String> f = new Function<Date, String>() {
			@Override
			public String apply(Date input) {
				return new SimpleDateFormat("yyyy-MM-dd").format(input);
			}
		};
		System.out.println(f.apply(new Date()));
		assertTrue(true);
```
可以组合Function使用的类包括：

函数|签名
---|---
Ordering|	Ordering.onResultOf(Function)
Predicate|	Predicates.compose(Predicate, Function)
Equivalence|	Equivalence.onResultOf(Function)
Supplier|	Suppliers.compose(Function, Supplier)
Function|	Functions.compose(Function, Function)

示例1：
```
Lists.newArrayList(30, 20, 60, 80, 10);

Ordering.natural().sortedCopy(numbers); //10,20,30,60,80

Ordering.natural().reverse().sortedCopy(numbers); //80,60,30,20,10

Ordering.natural().min(numbers); //10

Ordering.natural().max(numbers); //80

Lists.newArrayList(30, 20, 60, 80, null, 10);

Ordering.natural().nullsLast().sortedCopy(numbers); //10, 20,30,60,80,null

Ordering.natural().nullsFirst().sortedCopy(numbers); //null,10,20,30,60,80
```
此外，ListenableFuture API支持转换ListenableFuture。Futures也提供了接受AsyncFunction参数的方法。AsyncFunction是Function的变种，它允许异步计算值。

签名|
---|
Futures.transform(ListenableFuture, Function)|
Futures.transform(ListenableFuture, Function, Executor)|
Futures.transform(ListenableFuture, AsyncFunction)|
Futures.transform(ListenableFuture, AsyncFunction, Executor)|