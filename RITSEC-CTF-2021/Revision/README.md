# Challenge Name: Revision




![date](https://img.shields.io/badge/date-12.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   
![score](https://img.shields.io/badge/score-200-blue.svg)




## Detailed solution

http://git.ritsec.club:7000/Revision.git/ 

Starting by cloning the Revision repository

```
git clone http://git.ritsec.club:7000/Revision.git/
``` 
```
ls -la
total 244
drwxr-xr-x  8 kali kali    600 Apr 12 14:30 .
drwxr-xr-x 16 kali kali    540 Apr 12 14:29 ..
-rw-r--r--  1 kali kali   3135 Apr 12 14:30 about.html
-rw-r--r--  1 kali kali    606 Apr 12 14:30 alumni.html
drwxr-xr-x  6 kali kali    120 Apr 12 14:30 assets
-rw-r--r--  1 kali kali     15 Apr 12 14:30 CNAME
-rw-r--r--  1 kali kali    203 Apr 12 14:30 _config.yml
-rw-r--r--  1 kali kali    307 Apr 12 14:30 contact.html
drwxr-xr-x  2 kali kali    200 Apr 12 14:30 _data
-rw-r--r--  1 kali kali   1511 Apr 12 14:30 donors.html
-rw-r--r--  1 kali kali    900 Apr 12 14:30 eboard.html
-rw-r--r--  1 kali kali   1124 Apr 12 14:30 events.html
-rw-r--r--  1 kali kali    838 Apr 12 14:30 Gemfile
-rw-r--r--  1 kali kali   1482 Apr 12 14:30 Gemfile.lock
drwxr-xr-x  8 kali kali    260 Apr 12 14:30 .git
-rw-r--r--  1 kali kali     57 Apr 12 14:30 .gitignore
drwxr-xr-x  2 kali kali    260 Apr 12 14:30 _includes
-rw-r--r--  1 kali kali    371 Apr 12 14:30 index.html
drwxr-xr-x  2 kali kali    100 Apr 12 14:30 _layouts
-rw-r--r--  1 kali kali   1718 Apr 12 14:30 links.html
-rw-r--r--  1 kali kali   1011 Apr 12 14:30 newsletters.html
-rw-r--r--  1 kali kali    704 Apr 12 14:30 past-eboards.html
-rw-r--r--  1 kali kali    381 Apr 12 14:30 README.md
-rw-r--r--  1 kali kali    604 Apr 12 14:30 resources.html
drwxr-xr-x  2 kali kali     40 Apr 12 14:30 ritsec.github.io
-rw-r--r--  1 kali kali    532 Apr 12 14:30 signin.html
-rw-r--r--  1 kali kali    644 Apr 12 14:30 signup.html
-rw-r--r--  1 kali kali 163322 Apr 12 14:30 sponsorship.pdf
-rw-r--r--  1 kali kali   2496 Apr 12 14:30 sponsors.html
-rw-r--r--  1 kali kali    210 Apr 12 14:30 tasks.txt
``` 

We have some files and the .git folder  

```
ls -la
total 44
drwxr-xr-x  8 kali kali   260 Apr 12 14:30 .
drwxr-xr-x  8 kali kali   600 Apr 12 14:30 ..
drwxr-xr-x  2 kali kali    40 Apr 12 14:29 branches
-rw-r--r--  1 kali kali   266 Apr 12 14:30 config
-rw-r--r--  1 kali kali    73 Apr 12 14:29 description
-rw-r--r--  1 kali kali    23 Apr 12 14:30 HEAD
drwxr-xr-x  2 kali kali   300 Apr 12 14:29 hooks
-rw-r--r--  1 kali kali 28350 Apr 12 14:30 index
drwxr-xr-x  2 kali kali    60 Apr 12 14:29 info
drwxr-xr-x  3 kali kali    80 Apr 12 14:30 logs
drwxr-xr-x 16 kali kali   320 Apr 12 14:29 objects
-rw-r--r--  1 kali kali  1038 Apr 12 14:30 packed-refs
drwxr-xr-x  5 kali kali   100 Apr 12 14:30 refs
```
Checking the git log with ```git log -p``` i found some commits for flag.txt 

We can use -- flag.txt to see only the file updates 

```
git log -p --all --full-history -- flag.txt  
```

The last commit show that the flag.txt has been deleted 

![image](https://user-images.githubusercontent.com/72421091/114414786-adec1380-9b9e-11eb-85f4-f1cfb8468f1a.png)

Checking the first commits 

![image](https://user-images.githubusercontent.com/72421091/114415014-d83dd100-9b9e-11eb-93a1-5e11fcedcf5a.png)

As we can see in each commit we have an update for the file, removing the existed charactere and add a new one 

We know that the flag format is RS{} so we need to combine file updates to get the flag 

Let's get only the insertion(+) updates from the git log output  
  
```
git log -p --all --full-history -- flag.txt | grep -x '.\{2\}' | grep "^+" | cut -c 2-
```  

```
}
s
m
0
c
_
t
i
g
_
3
s
0
h
t
_
d
e
t
p
1
r
c
s
_
u
0
y
_
3
p
0
h
_
I
{
S
R
```  

Let's save the output in a file and use a little python script to get our flag RS{}  

```python
f = open("flag.txt")

flag = f.read().replace('\n', '')[::-1]

print(flag)
```



## Flag

```
RS{I_h0p3_y0u_scr1pted_th0s3_git_c0ms}
```
