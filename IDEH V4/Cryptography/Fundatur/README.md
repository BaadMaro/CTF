# Challenge Name: Fundatur


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Cryptography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-75-blue.svg)  


## Description

Can you speak in `IRKFS6SOLBFFUMTRGVVTOWTLGZCGSR3ZJBIEE22MNRVFONCPNJHGCTZV` ?

**Author**: kw4ntum

## Detailed solution 

I started by analyzing our encoded text using cyberchef magic feature https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')&input=SVJLRlM2U09MQkZGVU1UUkdWVlRPV1RMR1pDR1NSM1pKQklFRTIyTU5SVkZPTkNQTkpIR0NUWlY  

We got a match with a base32 encoding. Now let's decode using base32. 

The output "DTYzNXJZ2q5k7Zk6DiGyHPBkLljW4OjNaO5" 

I didn't get much with cyberchef so i switched to dcode.fr for the new encdoing https://www.dcode.fr/cipher-identifier

It detects base62. Let's decode it https://gchq.github.io/CyberChef/#recipe=From_Base62('0-9A-Za-z')&input=RFRZek5YSloycTVrN1prNkRpR3lIUEJrTGxqVzRPak5hTzU

We found our flag. 

We can go for another approch using basecrack https://github.com/mufeedvh/basecrack

![image](https://user-images.githubusercontent.com/72421091/221588657-6c00f95c-6615-4796-943f-d7d046198769.png)


## Flag

```
IDEH{b4se_62_then_b4se_32}
```
