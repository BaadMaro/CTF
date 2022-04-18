# Challenge Name: this is super easy

![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Cryotography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  

## Description

75 69 6f 63 7a 4e 6f 32 5e 62 69 35 73 5e 79 6e 53 7c

_Author: Jakom_ 

## Detailed solution

I start analysing different decoding using cyberchef 

Using the magic functionality, i was able to find the flag using XOR with the key `1` 

First decode from hex and xor with 1 https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'1'%7D,'Standard',false)&input=NzUgNjkgNmYgNjMgN2EgNGUgNmYgMzIgNWUgNjIgNjkgMzUgNzMgNWUgNzkgNmUgNTMgN2M

## Flag

```
thnb{On3_ch4r_xoR}
```
