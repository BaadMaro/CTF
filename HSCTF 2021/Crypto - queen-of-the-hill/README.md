# Challenge Name: LSBlue

![date](https://img.shields.io/badge/date-15.06.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Cryptography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-221-blue.svg)  


## Description

After finding a special key of the Hill, which contains a note to visit the Queen of the Hill, our brave Amanda begins her adventure to find the Queen of the Hill’s treasure. How shall she meet the Queen of the Hill? (a=0)

Cipher text: rtca{vbuhp_kaiq_gfj_nx_rda_ujw}

Encryption key:

16 25 8

14 19 5

15 17 3

## Detailed solution

We have a mentien for **Hill** in the description let's search for Hill cipher https://en.wikipedia.org/wiki/Hill_cipher 

Hill cipher use a matrice n x n as key with is similar to the encryption key in the description  

Let's decode the Hill ciphertext with the key matrice 3x3 i'll use https://www.dcode.fr/hill-cipher 

![image](https://user-images.githubusercontent.com/72421091/122655792-36fa6a80-d14d-11eb-88ac-272df127ef6d.png)




## Flag

```
flag{climb_your_way_to_the_top}
```
