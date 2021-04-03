
# Challenge Name: Flasher


![date](https://img.shields.io/badge/date-04.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)


## Attached files

- [candump-2020-11-30_044734.log](candump-2020-11-30_044734.log)
- [can.txt](can.txt)
- [can.py](can.py)

## Detailed solution

The challenge description talk about some secret signals used by drug dealers.  

The log file is a CAN dump from a car, we can see that the ID 188 have multiple lines, after doing some research we find that id 188 is refering to car blink (challenge name hint).  

Let's take only the 188 ID values  

```bash
cat candump-2020-11-30_044734.log | cut -d ' ' -f3 | grep '188#' | cut -d '#' -f2 > can.txt
``` 
[can.txt](can.txt)  

We have two values 010000 and 020000 
   - Right turn signal: 020000
   - Left turn signal: 010000  
   
We can replace one of them by 0 and other by 1 and see. I created a Python 3 script  
  
```python  
import binascii
a = open("C:/Users/maros/Downloads/can.txt", "r")
c = ''
b = a.readlines()
for x in b:
    if x == '010000\n':
      c += '0'
    else:
      c += '1'
print(binascii.unhexlify('%x' % int(c,2)).decode())
```


## Flag

```
flag{b!nary_s3cret_revealed}
```
