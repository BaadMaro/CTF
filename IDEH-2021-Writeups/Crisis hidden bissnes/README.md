
# Challenge Name: Crisis hidden bissnes  


![date](https://img.shields.io/badge/date-07.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![web category](https://img.shields.io/badge/category-web-lightgrey.svg)
![score](https://img.shields.io/badge/score-75-blue.svg)




## Detailed solution  

Start by opening the given link and exploring pages, nothings there.  

I checked for the Robots.txt file i fonded some files/directories. The one that was working is a dic file : 

```
/755f85c2723bb39381c7379a604160d8/dic
```  

It's a text file contains many words, numbers and filename with extensions for each line in the file. It's probably a wordlist dictionary (dic) for some hidden files/directories in the website.  

Lets' bruteforce using the dic file, i'll use **dirb** : 
  
```
dirb http://131.94.144.47/ dic  

+ http://131.94.144.47/creds.txt (CODE:200|SIZE:189)
==> DIRECTORY: http://131.94.144.47/top_secret/
```  
We finded the file creds.txt and the directory top_secret let's open them.  

The creds.txt has some logins with email:password  

```
Eddie_Morra@crisis.com:djksd@q!
0pwny@Hackira.com:tst2020
jakom@crisis.com:hello123
Mssasi@crisis.com:secure2020
okay@crisis.com:coco
tensho@crisis.com:hm12dj@!
nizar@crisis.com:spipah1100
```

The directory /top_secret has a  login page, we can use our credentials to try log in (i don't remeber which one xd).  

Login page ```http://131.94.144.47/top_secret/login.php``` 

It's a chat app that has some discussions, we start looking one by one.  

The chat **tst tst** has some secret sharing :  
  
```
Theres somthing in https://crisi5.com/

Oursecret

Oursecret.txt

Oursecret.txt
```  
We can go check the Oursecret.txt file in https://crisi5.com/  
  
```
http://crisi5.com/Oursecret.txt
```
We found our flag 

## Flag

```
IDEH{Master_0fR3con!337}
```
