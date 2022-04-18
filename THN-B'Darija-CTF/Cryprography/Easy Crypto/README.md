# Challenge Name: Easy Crypto


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Cryotography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  

## Description

x² - 7x = 0

12644, 10088, 11330, 8918, 14268, 2058, 8360, 4680, 2340, 2640, 2244, 8360, 11118, 2340, 2640, 4680, 8360, 2744, 6630, 2640, 800, 8360, 2058, 8360, 5244, 1968, 6794, 2244, 8360, 5100, 13328, 2340, 4148, 12198, 2340, 2640, 2058, 4020, 14750  

## Detailed solution  

We can start by trying to find the relation between first numbers and flag format `thnb{` 

- ord("t") = 116
- `116*116 - 7*116 = 12644` which mean we need to use x² - 7x to find the flag characters

Here is the solution

```python
import string

en = [12644, 10088, 11330, 8918, 14268, 2058, 8360, 4680, 2340, 2640, 2244, 8360, 11118, 2340, 2640, 4680, 8360, 2744, 6630, 2640, 800, 8360, 2058, 8360, 5244, 1968, 6794, 2244, 8360, 5100, 13328, 2340, 4148, 12198, 2340, 2640, 2058, 4020, 14750]

f = ""
a = 0

while(a != len(en)):
    for i in string.printable:
        t = ord(i)**2 - ( 7*ord(i) )
        if t == en[a]:
            f += i
            a = a+1
            #print(f)
            break
        
print(f)
```  

## Flag

```
thnb{1_H473_m47H_8U7 _1_L0V3_Kw4Dr471C}
```
