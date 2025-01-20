Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
A=5
print(type(A))
<class 'int'>
b=5.0
print(type(b))
<class 'float'>
c=2+4j
print(type(c))
<class 'complex'>
s="hello world"
print(s)
hello world
a=["man",1,2,3,4,5]
print(a)
['man', 1, 2, 3, 4, 5]
z=(1,2,3,4,5)
\
  
print(z)
(1, 2, 3, 4, 5)
z[1]=2
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    z[1]=2
TypeError: 'tuple' object does not support item assignment
a[1]=2
print(a)
['man', 2, 2, 3, 4, 5]
d=dict({1:'apple',2:'man',3:'bandage'})
print(d)
{1: 'apple', 2: 'man', 3: 'bandage'}
s=set(["a'
       
SyntaxError: unterminated string literal (detected at line 1)
s=set(["a
       
SyntaxError: unterminated string literal (detected at line 1)
s=set(["a","b"])
       
print(s)
       
{'a', 'b'}
fs=frozenset(["e","f"])
       
print(fs)
       
frozenset({'e', 'f'})
s[0]="s"
       
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s[0]="s"
TypeError: 'set' object does not support item assignment
fs[0]="s"
       
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fs[0]="s"
TypeError: 'frozenset' object does not support item assignment
print(type(true))
       
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(type(true))
NameError: name 'true' is not defined. Did you mean: 'True'?
print(type(True))
       
<class 'bool'>
print(type(False))
       
<class 'bool'>
def dist(x1,y1,x2,y2):
    return(((x2 - x1)**2 +(y2-y1)**2)**0.5)
print( dist(3,4,4,3))
SyntaxError: invalid syntax
def dist(x1,y1,x2,y2):
    return(((x2 - x1)**2 +(y2-y1)**2)**0.5)
print(dist(3,4,4,3))
SyntaxError: invalid syntax
import math
a=int(input("Enter first value"))
b=int(input("Enter second value"))
c=math.sqrt(a**2+b**2)
print("Distance=",c)
SyntaxError: multiple statements found while compiling a single statement
import math
a=int(input("enter first value"))
enter first value 5
b=int(input("enter second value"))
enter second value 6
c=math.sqrt(a**2+b**2)
print("distance=",c)
distance= 7.810249675906654

import sys
a=int(sys.argv[1])
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a=int(sys.argv[1])
IndexError: list index out of range
python script.py 10

SyntaxError: invalid syntax
a=int(sys.argv[0])
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a=int(sys.argv[0])
ValueError: invalid literal for int() with base 10: ''
a,b = sys.argv[1:2]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a,b = sys.argv[1:2]
ValueError: not enough values to unpack (expected 2, got 0)
summ = sum(float(i) for i in sys.argv[1:])
print("sum is", summ)

sum is 0
summ = sum(float(i) for i in sys.argv[3:4])
print("sum is", summ)
sum is 0
python hello.py 10 20
SyntaxError: invalid syntax
hello.py 10 20
SyntaxError: invalid syntax
import sys
add.py
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    add.py
NameError: name 'add' is not defined

============================= RESTART: C:/Users/student/Desktop/add.py ============================
Traceback (most recent call last):
  File "C:/Users/student/Desktop/add.py", line 2, in <module>
    a=int(sys.argv[1])
IndexError: list index out of range
python add.py 3 4
SyntaxError: invalid syntax
