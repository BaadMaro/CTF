# Challenge Name: Shuffled


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Cryotography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-100-blue.svg)  

## Description  

Just reverse it.. 

_Author: Jakom_

 [enc.py](https://thnbdarija.ctfd.io/files/1936366db7f9a939ee92fe2dc4a24c5f/enc.py?token=eyJ1c2VyX2lkIjoyNywidGVhbV9pZCI6MTUsImZpbGVfaWQiOjEwfQ.YltBew.XZlnZI0yQTTkd9UaGccA5kYQUCM)

 [encoded.txt](https://thnbdarija.ctfd.io/files/b1664c5abe98e1a50216d5e1bc43be41/encoded.txt?token=eyJ1c2VyX2lkIjoyNywidGVhbV9pZCI6MTUsImZpbGVfaWQiOjE2fQ.YltBew.qVy-N4zleXHvi77uy0r_xRcQtXs)
 
 ## Detailed solution  
 
Let's check the enc.py script 

 ```python
 import random

def padding(char):
    c = []
    for i in range(32, char):
        c.append(chr(i))
    c.append(chr(char))
    random.shuffle(c)
    print("".join(c))

flag = str(input())

for i in flag:
    _l =  ord(i)
    padding(_l)
 ```
 - We have a loop that save all the characeters from 32 to the charactere from flag and after that it shuffle them 

even if the encoded strings are shuffled we can identify them by the maximun decimal number because the chracaters from flag are always in the end of loop

Simple solution is using the function sorted in python and take the last character

Here is the solution

```python
f = open("encoded.txt" ,"r")

flag = ""
for i in f.readlines():
    a = sorted(i)
    #print(a[-1])
    flag += a[-1]
print(flag)

```
 
## Flag 

```
thnb{w3LL_I_7rI3d_70_S37_4_k3Wl_N4M3}
```
