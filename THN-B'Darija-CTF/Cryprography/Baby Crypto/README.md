# Challenge Name: Baby Crypto


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Cryotography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  


## Description

just another random baby crypt challenge to warmup

flag format: thnb{}

[cipher.txt](https://thnbdarija.ctfd.io/files/e9ecfd53fecb4013c9a06e12e8abbad2/cipher.txt?token=eyJ1c2VyX2lkIjoyNywidGVhbV9pZCI6MTUsImZpbGVfaWQiOjd9.Yls_VA.wvv5mX4BPghMKLemSnWjluBjBf4)
 
## Detailed solution

Cipher had two charcateres H and T 

```
HTTHTTTHHHTHHTTTTTTHTTTTHTTTTHHTHHTTTTHTHTTTTHTHHTTHHHTHTTHT
```

There is a cipher called Bacon cipher that use two characteres A and B https://www.dcode.fr/bacon-cipher 

With A=T and  B=H we got our flag `THNBBBYCRYPT`  

## Flag

```
thnb{THNBBBYCRYPT}
```



