# Challenge Name: Nocab


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Crypto-blueviolet.svg)   
![value](https://img.shields.io/badge/value-5-blue.svg)  


## Description

Created By sicmundos

AAABBAABAAAAABABAAAABABBAABBBABAABA BAABAAABBBAABAA AABABABABAAAAAAAABBA 

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/Wp79LDMx5N1LGAJA2EgnrwiTsJQxMgYtA47JeOoi.zip)

## Detailed solution

I tired to search for some cihper that use A and B and i found one called Bacon cipher

Bacon's encryption uses a substitution alphabet based on 2 letters (called biliteral), often A and B, replacing the letters of the alphabet.

![image](https://user-images.githubusercontent.com/72421091/157151688-e4cea385-f7e4-45c0-a734-53f0e2d5b3d0.png)


Let's decode description first. We can use https://www.dcode.fr/bacon-cipher 

```
AAABBAABAAAAABABAAAABABBAABBBABAABA BAABAAABBBAABAA AABABABABAAAAAAAABBA 
DECRYPTTHEFLAG
```
And now let's check the file **nocab.txt**

```
AAABABAAAAABAAABAAABABAAABAAAB{ABAAA_ABABAABAAAABAABAABAA_AAAABAAAAAAAABAABBABABBAA}
CRISISILIKEBACON
```

We found our flag, we need to add { } _ 

```
CRISIS{I_LIKE_BACON}
```
