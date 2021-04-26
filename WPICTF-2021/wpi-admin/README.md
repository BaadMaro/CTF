# Challenge Name: wpi-admin

![date](https://img.shields.io/badge/date-25.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![web category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-200-blue.svg)  


## Description

Your friend is a sophomore at Worcester Polytechnic Institute. They have had a rough first two years, so you came up with the idea to hack into WPI's servers and change their grades. Their email is alexo@uupeye.edu

https://wpiadmin.wpictf.xyz/

## Detailed solution

Start by exploring the website https://wpiadmin.wpictf.xyz/ 

![image](https://user-images.githubusercontent.com/72421091/116028972-d1f03000-a647-11eb-9c6e-ca4611f7feef.png)

We can see some pages :
- Home page https://wpiadmin.wpictf.xyz/ : nothing special
- Student login https://wpiadmin.wpictf.xyz/studLogin : a login page using email and password 

![image](https://user-images.githubusercontent.com/72421091/116029609-38298280-a649-11eb-8eea-36005d25ccd2.png)

- Admin portal https://wpiadmin.wpictf.xyz/loginPortal : Portal Temporarily Unavailable Please use direct link
- Top students https://wpiadmin.wpictf.xyz/topStudents : has a list of users with picture, name, email and status

![image](https://user-images.githubusercontent.com/72421091/116029664-4d061600-a649-11eb-86ef-42aaf7da0d24.png)

So we have the top student emails :

```
colino@uupeye.edu
calliep@uupeye.edu
annar@uupeye.edu
gaylenek@uupeye.edu
dennisb@uupeye.edu
sherrim@uupeye.edu
adams@uupeye.edu
```
I intercept the login request and start brutforcing using top students emails and a wordlist for passwords  
  

![image](https://user-images.githubusercontent.com/72421091/116030177-83906080-a64a-11eb-8d3a-40235389b285.png)

I used a simple wordlist https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt 

We can see the correct credentials with a 302 redirection while incorrect credentials show Invalid username/password  

We found all top students credentials 

```
colino@uupeye.edu 123456
sherrim@uupeye.edu 12345678
gaylenek@uupeye.edu qwerty
dennisb@uupeye.edu 123123
calliep@uupeye.edu password 
annar@uupeye.edu iloveyou
adams@uupeye.edu soccer
``` 
Start login in with each emails we can see some new pages : Student news, Student communications and Student notes  

But while log in with dennisb@uupeye.edu email which is a student worker we found our flag at Student news page  

![image](https://user-images.githubusercontent.com/72421091/116030730-c30b7c80-a64b-11eb-853f-a1aca6094ccd.png)



## Flag

```
WPI{1n53cUR3_5tud3Nts}
```
