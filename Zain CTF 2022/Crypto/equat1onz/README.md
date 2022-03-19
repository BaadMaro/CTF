# Challenge Name: equat1onz

![date](https://img.shields.io/badge/date-18.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Cryptography-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

You won't pass our gate! https://hubchallenges.s3.eu-west-1.amazonaws.com/Crypto/equat1onZ.zip

## Detailed solution

Challenge.py

```py
#!python3 
from math import *
with open('flag.txt','r') as fg:
	flag=fg.read()

def calc(x,val):
	return {
		0: lambda x: (x+1)/(x-1),
		1: lambda x: 984512/(x-69964)+69964
	}[val](x)

def get_val(x,i):
	if ( i % 2 == 0 ):
		return calc(x,1)
	else:
		return calc(x,0)
	
enc=[]
i= 0
for L in flag:
	enc.append(get_val(ord(L),i))
	i+=1


print(enc)
#[69949.90776101458, 1.0186915887850467, 69949.90876951923, 1.0196078431372548, 69949.90352371817, 1.0277777777777777, 69949.90614710683, 1.017094017094017, 69949.90594534237, 1.0186915887850467, 69949.90473463427, 1.017391304347826, 69949.90715584248, 1.018181818181818, 69949.90614710683, 1.024390243902439, 69949.90917288068, 1.0208333333333333, 69949.90534001432, 1.04, 69949.90917288068, 1.02, 69949.90876951923, 1.0175438596491229, 69949.90392737999, 1.0212765957446808, 69949.90574357212, 1.02, 69949.90876951923, 1.0175438596491229, 69949.90392737999, 1.0212765957446808, 69981.0168870452, 1.0212765957446808, 69949.90513822675, 1.0178571428571428, 69949.90473463427, 1.0192307692307692, 69949.90372555197, 1.0166666666666666, 69949.90312003322, 1.2222222222222223]
```

**Reversing calc function**

- For 0 

```
(x+1)/(x-1) = c
x + 1 = xc - c
x (1-c) = -c - 1 
x = (c+1) / (c-1)
```
- For 1

```
984512/(x-69964)+69964 = c

984512/(x-69964) = c - 69964
x = (984512 / (c - 69964)) + 69964

```

R
