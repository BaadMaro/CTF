# Challenge Name: Caedes Frequentiae


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Cryptography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg)  


## Description

Hey officers, I was investigating a murder case and found some messages on the victim's phone, the first one is: "O QD ZIT WTLZ-FQZXKTR EKTQZXKT OF ZIT VGKSR, QFR NTZ O IQCT QSKTQRN AOSSTR ZIKTT DTF, QFR GY ZITLT ZIKTT ZVG VTKT HKOTLZL". I believe the victim and the receiver were using some kind of key to keep their communication secure and understandble by no one by them. The last message was this one, it was written as a draft and not sent though: "WORK_OL_ZIT_DXKRTKTK" I believe the last message holds some useful information for us, can you help me please?

Flag format: IDEH{}

**Author** : kw4ntum

## Detailed solution 

I start by doing some analysis to identify our cipher text. I used https://www.boxentriq.com/code-breaking/cipher-identifier 

![image](https://user-images.githubusercontent.com/72421091/221583742-283b6e68-84ae-4244-b57d-553222d976d9.png)

We probably have substitution cipher. We can see it two at the beginning that looks like "I am"

Using a automatic solver for substitution cipher to try identify english words https://www.boxentriq.com/code-breaking/cryptogram

We found our original text : 

![image](https://user-images.githubusercontent.com/72421091/221584340-f45c2275-7997-424e-b36a-d1602539a4a8.png)

Here is the key used : 

![image](https://user-images.githubusercontent.com/72421091/221584524-dcfda19e-2707-42e7-9641-4b76b307f317.png)

Now let's use the same key to decrypt the second cipher text "WORK_OL_ZIT_DXKRTKTK" 

![Pasted image 20230226044840](https://user-images.githubusercontent.com/72421091/221584740-49d28cc0-91f2-45d8-99fe-35782a8952d1.png)

We just need to put our plaintext in uppercase. 

## Flag

```
IDEH{BIDR_IS_THE_MURDERER}
```
