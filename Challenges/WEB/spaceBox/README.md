# Challenge Name: spaceBox

![date](https://img.shields.io/badge/date-09.10.2021-brightgreen.svg)  
![web category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)


## Description

A simple vulnerable web application. Gain access then capture the flag.

Author : Hamza Elansari @hamza07-w

Challenge link : https://github.com/hamza07-w/spaceBox



### Web app setup

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
Now it's permissions time. Never run a website from your home directory!

Details : https://askubuntu.com/questions/767504/permissions-problems-with-var-www-html-and-my-own-home-directory-for-a-website

- Allow Apache access to the folders and the files 

```
sudo chgrp -R www-data /var/www/spacebox.hkg
sudo find /var/www/spacebox.hkg -type d -exec chmod g+rx {} +
sudo find /var/www/spacebox.hkg -type f -exec chmod g+r {} +
```

- Give your owner read/write privileges to the folders and the files, and permit folder access to traverse the directory structure 
```
sudo chown -R USER /var/www/html/
sudo find /var/www/html -type d -exec chmod u+rwx {} +
sudo find /var/www/html -type f -exec chmod u+rw {} +
```
USER : your username ex: ubuntu if run Ubuntu

- Make sure every new file after this is created with www-data as the 'access' user.
```
sudo find /var/www/spacebox.hkg -type d -exec chmod g+s {} +
```
- Final security cleanup, if you don't want other users to be able to see the data
```
sudo chmod -R o-rwx /var/www/spacebox.hkg/
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

```
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

- posts/ has some php files with some text : welcome, artcile1
- 









