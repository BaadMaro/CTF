# Challenge Name: Baby's First Reversing

![date](https://img.shields.io/badge/date-24.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![reversing category](https://img.shields.io/badge/category-Reversing-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  


## Description

Baby's first reversing, I think. Get it to terminate with exit 0 with an input matching the flag format (WPI{foo bar baz})

[mhm](mhm)


## Detailed solution

Starting by checking the challenge file  

```
file mhm

mhm: python 3.8 byte-compiled
```

It's a pyc file, a compiled bytecode of Python code

We need to decompile it to get the source code. i'll use the Python byte-code decompiler uncompyle6

https://pypi.org/project/uncompyle6/

```python
uncompyle6 mhm.pyc

# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: uhhhhhhh.py
# Compiled at: 2021-03-05 00:04:38
# Size of source mod 2**32: 1222 bytes


def __main__(inp):
    i = -4
    for c in inp:
        if i == 4:
            if c != ' ':
                exit(82)
            else:
                if i == -4:
                    if c != 'W':
                        exit(133)
                    else:
                        if i == -2:
                            if c != 'I':
                                exit(42069)
                            elif i == -1 and c != '{':
                                exit(11037)
                            if i == 10:
                                if c != '}':
                                    exit(9001)
                        else:
                            if i == 1:
                                if c != '@':
                                    exit(11037)
                            if i == 2 and c != '5':
                                exit(11037)
                        if i == 7 and c != 'P':
                            exit(11037)
                    if i == 3:
                        if c != 'E':
                            exit(11037)
                else:
                    if i == 0:
                        if c != 'h':
                            exit(82)
                    if i == 5 and c != 'h':
                        exit(11037)
                if i == -3 and c != 'P':
                    exit(133)
            if i == 9:
                if c != '!':
                    exit(133)
        else:
            if i == 6:
                if c != '0':
                    exit(133)
            if i == 8 and c != '3':
                exit(133)
        i += 1
    else:
        print(':)')


__main__(input('hi'))
# okay decompiling mhm.pyc

```

We can see some characters for each i in our decompiled code. It test the characters of the input string and check if the characteres dosen't match with the tests it call the exit function   

As we know our flag format is WPI{foo bar baz} we can see at i=-4 the first character of our flag **W**  

To get the flag we need to combine all characters using the position i fron i=-4 to i=10



## Flag

```
WPI{P0lyGlOtz_R_koo1}
```
