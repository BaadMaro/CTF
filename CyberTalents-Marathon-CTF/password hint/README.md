
# Challenge Name: password hint


![date](https://img.shields.io/badge/date-02.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)




## Detailed solution

In this challenge we have a Sam registry hive. I'm gonna use RegRipper to extract data 

https://github.com/keydet89/RegRipper3.0

```
Username        : Flag [1001]
Full Name       : Flag
User Comment    : 
Account Type    : Default Admin User
Account Created : 2020-01-20 15:31:43Z
Name            :  
Password Hint   : ZmxhZ3tHcmVhdCAhIF9wYXJzaW5nX1NhbV9IaXZlfQ==
Last Login Date : Never
Pwd Reset Date  : 2020-01-20 15:33:17Z
Pwd Fail Date   : Never
Login Count     : 0
Embedded RID    : 1001
  --> Password does not expire
  --> Normal user account
```  

We see a password hint, it's a base64 encoded data let's decode it 
```
ZmxhZ3tHcmVhdCAhIF9wYXJzaW5nX1NhbV9IaXZlfQ== --> flag{Great ! _parsing_Sam_Hive}  
```

## Flag

```
flag{Great ! _parsing_Sam_Hive}
```
