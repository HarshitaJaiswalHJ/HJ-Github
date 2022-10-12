Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=print('Hi how are u?)
        
SyntaxError: unterminated string literal (detected at line 1)
a=print('Hi how are u?')
        
Hi how are u?
#Here a is not initialized with print function
        
def myfun()
SyntaxError: expected ':'
def myfun():
    print ('This is first fun')

    
myfun()
This is first fun
#This is no input no output function
a=myfun()
This is first fun
print(a)
None
def second():
    return 'abc'

second()
'abc'
b=second()
print(b)
abc
#this is no input but output function
def third(x):
    print ('HELLO')

    
third('abc')
HELLO
#this is input but no output function
def fourth(x):
    return x*10

fourth(5)
50
#this is input and output function
def fourth(x):
    print('hi')
    print('hello')
    print('how are you?')
    return x*10

fourth(10)
hi
hello
how are you?
100

= RESTART: C:/Users/jaisw/OneDrive/Desktop/ML with python Training/Day 6/pr6.py

= RESTART: C:/Users/jaisw/OneDrive/Desktop/ML with python Training/Day 6/pr6.py
hi
hello

= RESTART: C:/Users/jaisw/OneDrive/Desktop/ML with python Training/Day 6/pr6.py
hi
hello

= RESTART: C:/Users/jaisw/OneDrive/Desktop/ML with python Training/Day 6/pr6.py

= RESTART: C:/Users/jaisw/OneDrive/Desktop/ML with python Training/Day 6/pr6.py
hi
hello

=== RESTART: C:/Users/jaisw/OneDrive/Desktop/ML with python Training/Day 6/pr6.py ===
hi
hello
50
def five(x,y,z):
    return x+y+z
five (4,2,2)
SyntaxError: invalid syntax
def five(x,y,z):
    return x+y+z

five(4,2,2)
8
def seven (x,y,z=1)
SyntaxError: expected ':'
def seven (x,y,z=1):
    return x+y+z

seven(4,8)
13
#this is default argument function
def seven (x=1,y,z=1):
    return x+y+z
SyntaxError: non-default argument follows default argument
#default values must be assigned all at right in the perenthesis
def eight (*x):
    return x

eight()
()
eight(2)
(2,)
#*args always returns a tuple
def nine (**x):
    return x

nine()
{}
#**kwargs always returns a dictionary
nine(name='bipul',email='bipul@gmail.com')
{'name': 'bipul', 'email': 'bipul@gmail.com'}
nine(n1=0,n2=[11,10,20],n3=['ab','xy'])
{'n1': 0, 'n2': [11, 10, 20], 'n3': ['ab', 'xy']}
def birthday(harshita)
SyntaxError: expected ':'
def birthday(name):
    print ('Happy birthday to you')
    print ('Happy birthday to you')
    print ('Happy birthday dear {name}')
    print ('Happy birthday to you')

    
birthday('Harshita')
Happy birthday to you
Happy birthday to you
Happy birthday dear {name}
Happy birthday to you
def birthday(name):
    print ('Happy birthday to you')
    print ('Happy birthday to you')
    print (f'Happy birthday dear {name}')
    print ('Happy birthday to you')

    
birthday('Harshita')
Happy birthday to you
Happy birthday to you
Happy birthday dear Harshita
Happy birthday to you
birthday('Giya')
Happy birthday to you
Happy birthday to you
Happy birthday dear Giya
Happy birthday to you
birthday('Giya')
Happy birthday to you
Happy birthday to you
Happy birthday dear Giya
Happy birthday to you
def birthday(name,date):
    print ('Happy birthday to you')
    print ('Happy birthday to you')
    print (f'Happy birthday dear {name}')
    print ('Happy birthday to you')
    print (f'Dated:{date}')

    
birthday('Palak')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    birthday('Palak')
TypeError: birthday() missing 1 required positional argument: 'date'
birthday('Palak','4 december')
Happy birthday to you
Happy birthday to you
Happy birthday dear Palak
Happy birthday to you
Dated:4 december
birthday('Giya','21 september')
Happy birthday to you
Happy birthday to you
Happy birthday dear Giya
Happy birthday to you
Dated:21 september
myadd= lambda x,y,z:x+y+z
myadd(5,9,7)
21
#x,y,z are the arguments and x+y+z is the return value
import math
math.pi
3.141592653589793
math.sqrt(4)
2.0
math.pow(2,3)
8.0
math.factorial(5)
120
import math as m
m.pi
3.141592653589793
from math import sqrt
sqrt(12345)
111.1080555135405
import datetime as dt
aaj_ki_date=dt.date.today()
print(aaj_ki_date)
2022-09-19
import calender
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
import calendar
print(calendar.calender(2002))
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print(calendar.calender(2002))
AttributeError: module 'calendar' has no attribute 'calender'. Did you mean: 'calendar'?
import calendar

import calendar
print(calendar.calendar(2002))
                                  2002

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                   1  2  3
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
28 29 30 31               25 26 27 28               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31

print(calendar.month(2002,11))
   November 2002
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30

