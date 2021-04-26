# Challenge Name: wpi-admin-2

![date](https://img.shields.io/badge/date-25.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-250-blue.svg)  


## Description

Now that you've hacked into a student worker's account, maybe you can access the admin portal.


## Detailed solution

From the wpi-admin challenge we found the student worker account ```dennisb@uupeye.edu 123123``` 

login at : https://wpiadmin.wpictf.xyz/studLogin 

At the student news we can see 

![image](https://user-images.githubusercontent.com/72421091/116032218-c94f2800-a64e-11eb-8484-2077da801601.png)

Checking student communications, we can see the new link for the admin portal https://wpiadmin.wpictf.xyz/iyghfihGBKHJF9719fn113

![image](https://user-images.githubusercontent.com/72421091/116032318-fa2f5d00-a64e-11eb-8167-f157fcfc0385.png)

I tired to brutforce dennisb@uupeye.edu password for the admin portal but no success

I start checking for some Authentication bypass using SQL Injection. I used some payloads https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/Intruder/Auth_Bypass.txt  



![image](https://user-images.githubusercontent.com/72421091/116032899-00720900-a650-11eb-953d-31c950cdb354.png)

We were able to bypass the auth, we can login as ```dennisb@uupeye.edu / admin' or 1=1--``` 

We found our flag 

![image](https://user-images.githubusercontent.com/72421091/116033307-b63d5780-a650-11eb-9e96-1850c951e237.png)





## Flag

```
WPI{adM1n_1nj3c710N}
```
