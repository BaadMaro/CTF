
# Challenge Name: password hint


![date](https://img.shields.io/badge/date-17.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)



## Detailed solution

The solution is to fing an attacker trace using a request. The flag format is flag{X.X.X.X}  

```
HTTP/1.1 200 OK

Date: Mon, 27 Jul 2009 12:28:53 GMT

Server: Apache/2.2.14 (Win32)

Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT

Accept-Ranges: bytes

ETag: "6238615a28:0"

Content-Length: 20

Content-Type: text/html

 

MDgzLzA3OS8zMzAvMDc0
``` 

We have a base64 encoded string, let's decode it. We found 083/079/330/074  

The flag format has a "." between numbers so if we want to get a "." from "/" we need to xor "/" with 1. I'll use Cyberchef  

https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'1'%7D,'Standard',false)&input=MDgzLzA3OS8zMzAvMDc0  

![image](https://user-images.githubusercontent.com/72421091/113363441-c3fd0700-9348-11eb-9c35-f96508147bb6.png)


## Flag

```
Flag{192.168.221.165}
```
