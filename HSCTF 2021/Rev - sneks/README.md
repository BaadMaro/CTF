# Challenge Name: sneks

![date](https://img.shields.io/badge/date-17.06.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![reverse category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![value](https://img.shields.io/badge/value-403-blue.svg)  


## Description

https://www.youtube.com/watch?v=0arsPXEaIUY

- [sneks.pyc](sneks.pyc)
- [output.txt](output.txt)  


## Detailed solution

Starting by checking the challenge file  
  
```
┌──(kali㉿kali)-[~]
└─$ file sneks.pyc
sneks.pyc: python 3.8 byte-compiled
``` 

It's a pyc file, a compiled bytecode of Python code

We need to decompile it to get the source code. i'll use the Python byte-code decompiler uncompyle6

https://pypi.org/project/uncompyle6/

``` 
uncompyle6 sneks.pyc
# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: sneks.py
# Compiled at: 2021-05-19 20:21:59
# Size of source mod 2**32: 600 bytes
``` 
```python
import sys

def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    x = f(n >> 1)
    y = f(n // 2 + 1)
    return g(x, y, not n & 1)


def e(b, j):
    return 5 * f(b) - 7 ** j


def d(v):
    return v << 1


def g(x, y, l):
    if l:
        return h(x, y)
    return x ** 2 + y ** 2


def h(x, y):
    return x * j(x, y)


def j(x, y):
    return 2 * y - x


def main():
    if len(sys.argv) != 2:
        print('Error!')
        sys.exit(1)
    inp = bytes(sys.argv[1], 'utf-8')
    a = []
    for i, c in enumerate(inp):
        a.append(e(c, i))
    else:
        for c in a:
            print((d(c)), end=' ')


if __name__ == '__main__':
    main()
```  
We need to create a reverse script to decrypt output and get our flag 

For the input i'm gonna do a quick edit and replace space with new line [snek-output.txt](snek-output.txt)

```python
import sys
import string

file = open("sneak-output.txt", "r")

def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    x = f(n >> 1)
    y = f(n // 2 + 1)
    return g(x, y, not n & 1)


def e(b, j):
    return 5 * f(b) - 7 ** j


def d(v):
    return v << 1


def g(x, y, l):
    if l:
        return h(x, y)
    return x ** 2 + y ** 2


def h(x, y):
    return x * j(x, y)


def j(x, y):
    return 2 * y - x




aa = []
for x in file:
    aa.append(x[:-1])

flag = ""
inpi = 0
ff1 = []

for _ in range(12): 
    for x in string.printable:        
        inp = bytes(flag + x, 'utf-8')
        print("[+] Bruteforcing : " + flag + x )
        a = []
        for i, c in enumerate(inp):
            a.append(e(c, i))
        else:
            for c in a:
                ff1.append(d(c))
                if int(ff1[inpi]) == int(aa[inpi]):
                    flag += x                     
                    if (flag[-1] == '}') and (len(flag) == 24): #24 is output length
                        print("[+] Flag found   : " + flag) #flag{s3qu3nc35_4nd_5um5}
                        sys.exit()                 
                    inpi = inpi + 1
                    
                else:
                    ff1 = ff1[:-1]
 ```                  

![image](https://user-images.githubusercontent.com/72421091/122679917-c141dd80-d1e4-11eb-812a-f761f1b00297.png)




## Flag

```
flag{s3qu3nc35_4nd_5um5}
```
