# Challenge Name: Plain sight


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg)  


## Description

Hidden in plain sight

3wabactf.cf

_author: mando_

## Detailed solution

The website 3wabactf.cf is unreachable so i start checking dns information 

https://www.nslookup.io/dns-records/3wabactf.cf 

We found a TXT record `TXowbVFVNDRSMDBrTzBVdFB6UlhNVUUrTkNWTU9qYzVSVDh3Q2c9PQo=` 

It's a base64 string, let's decode it 

`Mz0mQU44R00kO0UtPzRXMUE+NCVMOjc5RT8wCg=`

Another base64 strings, let's decode it 

3=&AN8GM$;E-?4W1A>4%L:79E?0 

We got an unkonw encoding i used cyberchef magic functionality https://gchq.github.io/CyberChef/#recipe=Magic(3,true,false,'thnb')&input=Mz0mQU44R00kO0UtPzRXMUE%2BNCVMOjc5RT8w 

I got a close string to flag format `Sthnb{DnS_StayAlive=G` 

I used the option carry through which make the rotate right true https://gchq.github.io/CyberChef/#recipe=From_Base64('%20-_',false)Rotate_right(2,true)  

The output : `Sthnb{DnS_StayAlive}.`   

## Flag

```
thnb{DnS_StayAlive}
```
