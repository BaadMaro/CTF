# Challenge Name: PDF stagano


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-5-blue.svg)  


## Description

Created By **sicmundos**

Find the hidden information in this PDF file

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/72ZSuNlPnagJvuHxwhBZedYJnA8S70mJzvcortRW.zip)

## Detailed solution

PDF file has some text and an image for the event 

![image](https://user-images.githubusercontent.com/72421091/156959893-066efef4-6251-4d6e-b7b0-03ec7f4347df.png)

Let's select all to find maybe a hidden text

```
HELLO GEEKS!!
We are proud to announce that the 3rd edition of our amazing IDEH is back this week!
For all new comers, IDEH aka International Days of Ethical Hacking, is a cyber security
event focused mainly on ethical hacking and penetration testing. It spans 2 days consisting
of conferences and workshops on the first day, and a CTF competition on the second day.
This year's conference theme is: "The Future is Crypto", our honorable speakers will tackle
multiple new technologies all relating to blockchain and its security. As for the CTF, it's
jeopardy style, featuring the usual challenges + blockchain ones. Solve them in teams of 3.
This year's edition will be special, it's the first CIT event that will take place both at school
and online, both the conferences and the competition,
as students of INPT will join on premises, while all externs will join us online.
We have interesting prizes to offer, stay tuned to find them out.
So what are you waiting for? Register now and have fun playing our CTF! Show us your
skills and win it!
Special thanks to our official sponsors Crisis for providing us with the platform and
challenges, as well as Redal and CGI.
ps: only Moroccan students are eligible for these prizes (official participants), so you will
have to provide proof during your registration.
CRISIS{taddaaa}
```

We found the hidden flag

## Flag

```
CRISIS{taddaaa}
```
