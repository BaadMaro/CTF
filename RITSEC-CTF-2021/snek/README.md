
# Challenge Name: snek




![date](https://img.shields.io/badge/date-11.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![score](https://img.shields.io/badge/score-100-blue.svg)




## Detailed solution

Starting by checking the challenge file 
  
```
file snek
snek: python 3.7 byte-compiled
```  
It's a pyc file, a compiled bytecode of Python code 

We need to decompile it to get the source code. i'll use the Python byte-code decompiler **uncompyle6**

https://pypi.org/project/uncompyle6/ 
```  
uncompyle6 snek.pyc  

# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: snek.py
# Compiled at: 2021-04-08 07:24:05
# Size of source mod 2**32: 834 bytes
"""
Written for RITSEC CTF 2021
Author: knif3
Flag: RITSEC{}

TODO: Finish this challenge
"""

class d(object):

    def __init__(self, password):
        self.password = password.encode()
        self.decrypt = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 82, 83, 123, 97, 108, 108, 95, 104, 105, 36, 36, 95, 97, 110, 100, 95, 110, 48, 95, 98, 105, 116, 51, 125]

    def __eq__(self, other):
        if self.password == bytes(self.decrypt):
            print('!flag')
            return True
        return False


x = input('Enter my name: ')
a = d(x)
if a == x:
    print('IS_THIS_THE_FLAG??')
    print('NOPE')
else:
    print('WRONG')
# okay decompiling snek.pyc
```  
We can see that the input is compared to a decrypted flag 

We can make a simple Python script to decrypt it 

```python  

decrypt = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 6>

flag = bytes(decrypt).decode()

# print(flag) -> abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_RS{all_hi$$_and_n0_bit3}

print(flag[53:])

```
## Flag

```
RS{all_hi$$_and_n0_bit3}
```
