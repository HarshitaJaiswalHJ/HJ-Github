Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="hello"
print(a[0:2])
he
a[-1:-3]
''
a[-1:-3:-1]
'ol'
a[-3:-1:1]
'll'
a[-2:-1:1]
'l'
a[-1:-3]
''
a[-3;-1]
SyntaxError: invalid syntax
a[-3:-1]
'll'
a[-3:0]
''
a="hello world"
a.capitalize()
'Hello world'
#capitalize changes the first letter into upper case
a.title()
'Hello World'
#title changes the first letter OF EACH WORD into upper case
a.center(50)
'                   hello world                    '
a.center(50,'@')
'@@@@@@@@@@@@@@@@@@@hello world@@@@@@@@@@@@@@@@@@@@'
a.count(l)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.count(l)
NameError: name 'l' is not defined
a.count('l')
3
#count counts the frequency of the particular letter
a.lstrip()
'hello world'
a.center(50)
'                   hello world                    '
a.lstrip()
'hello world'
a=a.center(50)
a.lstrip()
'hello world                    '
a.rstrip()
'                   hello world'
a.isupper()
False
a.islower()
True
a.upper()
'                   HELLO WORLD                    '
a.startswith('he"0
             
SyntaxError: unterminated string literal (detected at line 1)
a.startswith('he")
             
SyntaxError: unterminated string literal (detected at line 1)
a.startswith('he')
             
False
a.endswith(d)
             
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.endswith(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
a.endswith("d")
             
False
len(a)
             
50
del a[0]
             
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    del a[0]
TypeError: 'str' object doesn't support item deletion
b="akshat123@gmail.com"
             
b=b.split('@')
             
b
             
['akshat123', 'gmail.com']
'@'.join(b)
             
'akshat123@gmail.com'
#---------------------------------------------------------
             
m=[12,'hi',2.3,500}
             
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
m=[12,'hi',2.3,500]
             
m[1:3]
             
['hi', 2.3]
'hi' in m
             
True
"hello" in m
             
False
28m
             
SyntaxError: invalid decimal literal
2*m
             
[12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500]
m+=['new value']
             
m
             
[12, 'hi', 2.3, 500, 'new value']
m.append('abc')
             
m
             
[12, 'hi', 2.3, 500, 'new value', 'abc']
m.extend(['x','y','kuch bhi'])
             
m
             
[12, 'hi', 2.3, 500, 'new value', 'abc', 'x', 'y', 'kuch bhi']
#extend is used to insert multiple values in the list
             
#append is used to insert exactly one element in the list
             
m.insert(2,"HELLO")
             
m
             
[12, 'hi', 'HELLO', 2.3, 500, 'new value', 'abc', 'x', 'y', 'kuch bhi']
m.pop()
             
'kuch bhi'
m
             
[12, 'hi', 'HELLO', 2.3, 500, 'new value', 'abc', 'x', 'y']
m.pop(0)
             
12
m
             
['hi', 'HELLO', 2.3, 500, 'new value', 'abc', 'x', 'y']
m.clear()
             
m
             
[]
m=[12,'hi',2.3,500]
             
m.reverse()
             
m
             
[500, 2.3, 'hi', 12]
m.sort()
             
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    m.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
m=[12,1,2.3,500]
             
m.sort()
             
m
             
[1, 2.3, 12, 500]
max(m)
             
500
min(m)
             
1
m.index(1)
             
0
############################################################
             
t=52,23,'abc'
             
type(t)
             
<class 'tuple'>
len(t)
             
3
t.index('abc')
             
2
t[:2]
             
(52, 23)
t[0]=42
             
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    t[0]=42
TypeError: 'tuple' object does not support item assignment
#immutable
             
t
             
(52, 23, 'abc')
k=(12,52,85,(5,'abc',5.5),100)
             
type(k)
             
<class 'tuple'>
#k is nested touple
             
k[3][1][1]
             
'b'
t
             
(52, 23, 'abc')
t.append(6)
             
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    t.append(6)
AttributeError: 'tuple' object has no attribute 'append'
#Q.insert an element in the  tuple
############################################################
s={1,2,3,4,4,3}
type(s)