# Challenge Name: High Ground Climbing


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Cryptography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-100-blue.svg)  


## Description

I have this message "PLKRPLZVJVWWZVAMST", and I know that it means "HEYTHEREHOWAREYOU". I also know that it is encrypted using some kind of matrix, can you help me get what "NZSHUZAPJJRJTEAWAB" means?

**Author**: kw4ntum

## Detailed solution 

We have two hints for the our cipher. The first one is challenge name which refer to "Hill" and also the usage of a matrix for encryption. 

Our cipher is Hill. We can use a decoder to find the used matrix and the plaintext https://www.dcode.fr/hill-cipher 

Let's start with the first cipher text "PLKRPLZVJVWWZVAMST" to find our matrix 

![image](https://user-images.githubusercontent.com/72421091/221590078-a30c501c-5fbd-4048-9251-f1db839da67a.png)

We did get the matrix used and also the alphabet. We have to remove the last charcater Z to match the solution needed.

Now let's decode our final text "NZSHUZAPJJRJTEAWAB" with the same matrix and alphabet  

![image](https://user-images.githubusercontent.com/72421091/221591444-1c869d39-e951-47c9-ba97-0179faeb0631.png)

## Flag

```
IDEH{LOWLEVELJABIPPSEC}
```
