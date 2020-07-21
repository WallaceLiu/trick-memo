# 简化
### 简化集合创建
```
Map<String, Map<String, String>> map = new HashMap<String, Map<String, String>>();

List<List<Map<String, String>>> list = new ArrayList<List<Map<String, String>>>();
```
简化：
```
Map<String, Map<String, String>> map = Maps.newHashMap();
List<List<Map<String, String>>> list = Lists.newArrayList();
List<Person> personList = Lists.newLinkedList();
Set<Person> personSet = Sets.newHashSet();
Map<String, Person> personMap = Maps.newHashMap();
Integer[] intArrays = ObjectArrays.newArray(Integer.class, 10);
```
### 集合初始化
```
Set<String> set = new HashSet<String>();
set.add("one");
set.add("two");
set.add("three");
```
简化：
```
Set<String> set = Sets.newHashSet("one", "two", "three");
List<String> list = Lists.newArrayList("one", "two", "three");
Map<String, String> map = ImmutableMap.of("ON", "TRUE", "OFF", "FALSE");
List<Person> personList2 = Lists.newArrayList(new Person(1, 1, "a",
"46546", 1, 20), new Person(2, 1, "a", "46546", 1, 20));
Set<Person> personSet2 = Sets.newHashSet(new Person(1, 1, "a", "46546",
1, 20), new Person(2, 1, "a", "46546", 1, 20));
Map<String, Person> personMap2 = ImmutableMap.of("hello", new Person(1,
1, "a", "46546", 1, 20), "fuck", new Person(2, 1, "a", "46546",1, 20));
```
# 新集合类型
### MultiMap
一种key可以重复的map，子类有ListMultimap和SetMultimap，对应的通过key分别得到list和set

```
Multimap<String, Person> customersByType = ArrayListMultimap.create();
customersByType.put("abc", new Person(1, 1, "a", "46546", 1, 20));
customersByType.put("abc", new Person(1, 1, "a", "46546", 1, 30));
customersByType.put("abc", new Person(1, 1, "a", "46546", 1, 40));
customersByType.put("abc", new Person(1, 1, "a", "46546", 1, 50));
customersByType.put("abcd", new Person(1, 1, "a", "46546", 1, 50));
customersByType.put("abcde", new Person(1, 1, "a", "46546", 1, 50));

for (Person person : customersByType.get("abc")) {
	System.out.println(person.getC6());
}
```
### MultiSet
不是集合，可以增加重复的元素，并且可以统计出重复元素的个数，例子如下：
```
Multiset<Integer> multiSet = HashMultiset.create();
multiSet.add(10);
multiSet.add(30);
multiSet.add(30);
multiSet.add(40);

System.out.println(multiSet.count(30)); // 2
System.out.println(multiSet.size()); // 4
```
### Table
相当于有两个key的map，不多解释
```
Table<Integer, Integer, Person> personTable = HashBasedTable.create();
personTable.put(1, 20, new Person(1, 1, "a", "46546", 1, 20));
personTable.put(0, 30, new Person(2, 1, "ab", "46546", 0, 30));
personTable.put(0, 25, new Person(3, 1, "abc", "46546", 0, 25));
personTable.put(1, 50, new Person(4, 1, "aef", "46546", 1, 50));
personTable.put(0, 27, new Person(5, 1, "ade", "46546", 0, 27));
personTable.put(1, 29, new Person(6, 1, "acc", "46546", 1, 29));
personTable.put(0, 33, new Person(7, 1, "add", "46546", 0, 33));
personTable.put(1, 66, new Person(8, 1, "afadsf", "46546", 1, 66));

// 1,得到行集合
Map<Integer, Person> rowMap = personTable.row(0);
int maxAge = Collections.max(rowMap.keySet());
```
### BiMap
是一个一一映射，可以通过key得到value，也可以通过value得到key； 
```
BiMap<Integer, String> biMap = HashBiMap.create();
biMap.put(1, "hello");
biMap.put(2, "helloa");
biMap.put(3, "world");
biMap.put(4, "worldb");
biMap.put(5, "my");
biMap.put(6, "myc");
int value = biMap.inverse().get("my");
System.out.println("my --" + value);
```
### ClassToInstanceMap
有的时候，你的map的key并不是一种类型，他们是很多类型，你想通过映射他们得到这种类型，guava提供了ClassToInstanceMap满足了这个目的。
 
除了继承自Map接口，ClassToInstaceMap提供了方法 T getInstance(Class<T>) 和 T putInstance(Class<T>, T),消除了强制类型转换。
 
该类有一个简单类型的参数，通常称为B，代表了map控制的上层绑定，例如：
 
ClassToInstanceMap<Number> numberDefaults = MutableClassToInstanceMap.create();
numberDefaults.putInstance(Integer.class, Integer.valueOf(0));
从技术上来说，ClassToInstanceMap<B> 实现了Map<Class<? extends B>, B>，或者说，这是一个从B的子类到B对象的映射，这可能使得ClassToInstanceMap的泛型轻度混乱，但是只要记住B总是Map的上层绑定类型，通常来说B只是一个对象。
guava提供了有用的实现， MutableClassToInstanceMap 和 ImmutableClassToInstanceMap.
重点：像其他的Map<Class,Object>,ClassToInstanceMap 含有的原生类型的项目，一个原生类型和他的相应的包装类可以映射到不同的值；
```
ClassToInstanceMap<Person> classToInstanceMap = MutableClassToInstanceMap
.create();

Person person = new Person(1, 20, "abc", "46464", 1, 100);

classToInstanceMap.putInstance(Person.class, person);

// System.out.println("string:"+classToInstanceMap.getInstance(String.class));
// System.out.println("integer:" +
// classToInstanceMap.getInstance(Integer.class));

Person person1 = classToInstanceMap.getInstance(Person.class);
```
涉及：
```
import com.google.common.base.Functions;
import com.google.common.base.Predicate;
import com.google.common.collect.ArrayListMultimap;
import com.google.common.collect.BiMap;
import com.google.common.collect.ClassToInstanceMap;
import com.google.common.collect.Collections2;
import com.google.common.collect.HashBasedTable;
import com.google.common.collect.HashBiMap;
import com.google.common.collect.HashMultiset;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableMultiset;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import com.google.common.collect.Multimap;
import com.google.common.collect.Multiset;
import com.google.common.collect.MutableClassToInstanceMap;
import com.google.common.collect.ObjectArrays;
import com.google.common.collect.Ordering;
import com.google.common.collect.Sets;
import com.google.common.collect.Table;
```