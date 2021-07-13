# Challenge Name: baby

![date](https://img.shields.io/badge/date-10.07.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Crypto-blueviolet.svg)   
![value](https://img.shields.io/badge/value-102-blue.svg)  


## Description

I want to do an RSA!

Author : EvilMuffinHa

[output.txt](output.txt)

## Detailed solution

We have an RSA encryption
```
n: 228430203128652625114739053365339856393
e: 65537
c: 126721104148692049427127809839057445790
```  
  
An RSA modulus is the product of two secret prime numbers p and q : N = pq. for factoring we gonna use factordb

![image](https://user-images.githubusercontent.com/72421091/125488201-965b12bd-a637-4295-9d30-a7443e2066a5.png)

We need to calcul :   
`phi = ( q — 1 ) * ( p — 1 )` Euler’s Totient for the number N.  
`d = inverse( e, phi )` the private key with the MODULAR INVERSE of e and phi.  

To decrypt the message :

`m ≡ c^d (mod n)`

I'm gonna use the python library **Pycryptodome** [baby.py](baby.py)

```python
from Crypto.Util.number import long_to_bytes, inverse

n = 228430203128652625114739053365339856393
e = 65537
c = 126721104148692049427127809839057445790

p = 12546190522253739887
q = 18207136478875858439

phi = (p-1)*(q-1)

d = inverse(e, phi)

flag = pow(c,d,n)

print(long_to_bytes(flag).decode())
``` 


## Flag

```
flag{68ab82df34}
```
