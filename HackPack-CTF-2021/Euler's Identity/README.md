# Challenge Name: Euler's Identity



![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![misc category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

One night, a man named Euler gave you three strings in your dream: MD5:d8d540ae49aadd151b96feb4e0ff124f, SHA1:abb07ca45c9e7719e66e766b958d943f561b8de6, SHA2(SHA1(MD5)):c037c03ee627047a85df540c42d59c6b6028841704a7c706feff584a997fd2a3.

Hint : People ask:'How does great Euler find the relationship among pi, imaginary number, and Euler's number.'  
Hint : On the following night, the man appeared in your dream again. He told you concatenating secrets together foreshadowed the future. For example, given MD5(This), SHA1(is), and SHA2(SHA1(MD5(future))), the key is flag{Thisisfuture}.  

## Detailed solution

Start by decrypting the md5 hash d8d540ae49aadd151b96feb4e0ff124f  

https://md5hashonline.com/id/ show that MD5 hash value of e^ is d8d540ae49aadd151b96feb4e0ff124f 

Now let's back to our description, we have a hint for Euler's identity eiπ + 1 = 0 which can be represented as eiπ = -1

![image](https://user-images.githubusercontent.com/72421091/115268227-94604400-a129-11eb-95d3-947badc7009e.png)

We got the first part which is **e^**  

The second part of the flag is SHA1 hash, we notice in euler's identity the iπ so i tried to find the part that leads to the SHA1 hash abb07ca45c9e7719e66e766b958d943f561b8de6  

Sha1(ipi=) = abb07ca45c9e7719e66e766b958d943f561b8de6

The second part is **ipi=** 

The third part is **-1** as we can see in Euler's identity but let's verify it first 

SHA2(SHA1(MD5)):c037c03ee627047a85df540c42d59c6b6028841704a7c706feff584a997fd2a3
- Md5(-1) = 6bb61e3b7bce0931da574d19d1d82c88
- Sha1(6bb61e3b7bce0931da574d19d1d82c88) = 5d3c4e0314c88f970ab3877e983527cf64d86a53
- Sha256(5d3c4e0314c88f970ab3877e983527cf64d86a53) = c037c03ee627047a85df540c42d59c6b6028841704a7c706feff584a997fd2a3

We got all parts let's combine them for the flag  

## Flag

```
flag{e^ipi=-1}
```
