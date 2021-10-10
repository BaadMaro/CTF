# Challenge Name: spaceBox

![date](https://img.shields.io/badge/date-09.10.2021-brightgreen.svg)  
![web category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)


## Description

A simple vulnerable web application. Gain access then capture the flag.

Author : Hamza Elansari @hamza07-w

Challenge link : https://github.com/hamza07-w/spaceBox

## Detailed solution

### Setup

For a better experience we need to setup a web server to run the web application. 

The simple way is to run it using the php web server locally ```php -S localhost:8000``` in the app folder.

I'm gonna choose Apache to have a classic situation. You can use Nginx too. 

### Apache config

Here is a detailed guide to how setup Apache. I'm in Kali linux so Apache and PHP already installed.

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

sudo mv spaceBox/ spacebox.hkg/

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






