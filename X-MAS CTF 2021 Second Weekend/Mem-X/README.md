# Challenge Name: Mem-X


![date](https://img.shields.io/badge/date-18.12.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-72-blue.svg)  


## Description

Do you ever find yourself forgetting about {mem_promo_list_rnd}? Well, you're not alone. That's why we created Mem-X, rigorously designed through hundreds of medical and psychological trials to be the perfect memory preservation system. You can find the Discord bot on the X-MAS CTF server, it is the Mem-X#0493 user.

Start your memory journey today with !help.

Hint: Flag is in /flag.txt

By: plaaosert

## Detailed solution

Going the discord channel and start interacting with Mem-X#0493 https://discord.com/invite/nEWq5TZaVc 

!help

![image](https://user-images.githubusercontent.com/72421091/146813528-c8b68285-0efb-4bf4-960a-f3f6415b8044.png)

Saving a note : !note test  

![image](https://user-images.githubusercontent.com/72421091/146813616-730b715a-ab5e-4b10-b470-6acb1f1d03e0.png)
 
Read note by the hash : !remember 1232c9cd7fddc94ebb5dbdb5ede181cd

![image](https://user-images.githubusercontent.com/72421091/146813692-99928e58-fee0-4cd1-ba93-fc9b27c56186.png)

If we try to use !remember without hash : !remember flag

![image](https://user-images.githubusercontent.com/72421091/146814000-a57327a1-6400-4b45-8af7-fd3eccd4993e.png)

As we can see the bot try to load flag.txt let's try using /flag : !remember /flag  

![image](https://user-images.githubusercontent.com/72421091/146814231-77f75fb4-bbe3-4ac2-bdc4-e1877a237703.png)

## Flag

```
X-MAS{f0rgEtt1nG_EvEry7h1Ng_abf91b10e019c}
```


