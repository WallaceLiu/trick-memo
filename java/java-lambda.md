# iterate
```
Stream.iterate(0.0, n -> n).limit(len).toArray(Double[]::new);
```
# map
```
List<Integer> numbers = Arrays.asList(3, 2, 2, 3, 7, 3, 5);
List<Integer> squaresList = numbers.stream().map( i -> i*i).distinct().collect(Collectors.toList());
```
# filter
```
List<String>strings = Arrays.asList("abc", "", "bc", "efg", "abcd","", "jkl");
int count = strings.stream().filter(string -> string.isEmpty()).count();
```
# limit
```
Random random = new Random();
random.ints().limit(10).forEach(System.out::println);
```
