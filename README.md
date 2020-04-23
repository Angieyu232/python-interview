# Learning Python The Soft Way



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
Python has six built-in types of sequences, but the most common ones are *list* and *tuple*.

The function of list and tuple is pretty much identicy, except for
- tuple use parentheses (()) instead of square brackets ([])
- tuple is immutable, meaning, you can't assign a value tuple[3] = newValue


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

### Package
A package is a collection of modules

- installing from a list of packages:
    > pip install -r requirement.txt
- list outdated packages:
    > pip list --outdated
- upgrade a package:
    > pip install --upgrade packageName
- pip uninstall a package
    > pip uninstall packageName


python install all package globally, to make a package installed locally, a virtual environment is needed

## Virtual Environments

Virtualenv allow you to install packages into an isolated folder. This allows you to better manage versions.

<folder_name>/bin/activate

#### Usage
1. To open up a virtual env in your project
```console
$ cd my-project/
$ virtualenv venv
```
2. after the venv/ folder been created , need to activate with
```console
source venv/bin/activate
```
3. The terminal console should have a **(venv)** before your Username %
```console
(venv) username@YourLaptopName %
```
4. install virtual local packages
```
pip install -r requirements.txt
```
5. To deactivate: Just run **deactivate**


#### Notes on Virtual Env

**Important**: Remember to add venv to your project's .gitignore file so you don't include all of that in your source code.

It is preferable to install big packages (like Numpy), or packages you always use (like IPython) globally.
All the rest can be installed in a virtualenv.



### Setting Up Environment Variable with Python project
Avoid display your keys and password and sentitive information by storing environmental variable.
There are two common ways of storing these variables
1. set the global env in your shell, depends on what shell you use, zsh shell stores in ~/.zshenv
2. use dotenv and store things in a .env file in the project folder and add .env in gitignore

- import os
- os.getenv()
- from dotenv import load_dotenv

**Reference Microsoft's Python Beginner Course**
