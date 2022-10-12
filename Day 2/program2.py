Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="Python"
b=10
id(a)
2540824117808
id(b)
2540818989584
print(a,b)
Python 10
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
length(keyword.kwlist)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    length(keyword.kwlist)
NameError: name 'length' is not defined
len(keyword.kwlist)
35
_="hello"
#This is possible
"""Hii"""
'Hii'
a,b,c=20,50,55
print(a,b,c)
20 50 55
x=y=z=100
5and6
SyntaxError: invalid decimal literal
2<5 and 10<100
True
2>5 or 10<100
True
