# Learning Python

#### Basic build-in

- Numeric Types — int, float, complex
- // --> floor quotient of x and y
- divmod(x, y) --> (x//y, x%y)
- both x ** y and pow(x, y) --> x to the power y
- enumerate(iterable which is a sequence structure, start=an index)
- format()
```
>>> print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))
returns: 6 bananas cost $1.74
```

### Basic structures
Python has six built-in types of sequences, but the most common ones are lists and tuples.

 #### List:
```python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
del list1[2]
```

 #### Tuple: an immutable sequence of Python objects, just like list
 ```python
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
```
#### Dict: key value pair, key must be unique

```python
values = {'jan': 1, 'feb':2, 'mar':3}
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary
```





--------------

### Notes

```python
str1 = "welcome"
str2 = "welcome"
print(id(str1),  id(str2))
str1 += " alice"
if str1 == str2:
    print('str1 == str2')
else:
    print('str1 != str2')
print(id(str1), id(str2))
```

- String concatenation doesn't modify the original string object instead it creates a new string object.

- Anonymous Functions = Lambda expression = lambda functions = a function that without a name


### For loops

[For loops](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) takes each item in an array or collection in order, and assigns it to the variable you define.

``` python
names = ['Christopher', 'Susan']
for name in names:
    print(name)
```

### While loops

[While loops](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) perform an operation as long as a condition is true.

``` python
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    name = names[index]
    print(name)
    index = index + 1
```

### Module

- import a module as namespace:
    > import modulename
- import all into current namespace:
    > from modulename import *
- import specific items into current namespace
    > from modulename import specific






