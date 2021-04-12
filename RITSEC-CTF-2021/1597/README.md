# Challenge Name: 1597




![date](https://img.shields.io/badge/date-11.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![score](https://img.shields.io/badge/score-100-blue.svg)




## Detailed solution

Starting by cloning the repository 

```
git clone http://git.ritsec.club:7000/1597.git/
```  
```
ls -la                                                                 
total 8
drwxr-xr-x  3 kali kali 100 Apr 11 14:35 .
drwxr-xr-x 16 kali kali 540 Apr 11 14:35 ..
-rw-r--r--  1 kali kali   1 Apr 11 14:35 flag.txt
drwxr-xr-x  8 kali kali 260 Apr 11 14:35 .git
-rw-r--r--  1 kali kali  44 Apr 11 14:35 README.md
```
flag.txt is empty and README.md has the text A git ```challenge series? Sounds fun.```

Let's check the.git folder 

```
ls -la
total 20
drwxr-xr-x  8 kali kali 260 Apr 12 17:01 .
drwxr-xr-x  3 kali kali 100 Apr 12 17:01 ..
drwxr-xr-x  2 kali kali  40 Apr 12 17:01 branches
-rw-r--r--  1 kali kali 262 Apr 12 17:01 config
-rw-r--r--  1 kali kali  73 Apr 12 17:01 description
-rw-r--r--  1 kali kali  23 Apr 12 17:01 HEAD
drwxr-xr-x  2 kali kali 300 Apr 12 17:01 hooks
-rw-r--r--  1 kali kali 209 Apr 12 17:01 index
drwxr-xr-x  2 kali kali  60 Apr 12 17:01 info
drwxr-xr-x  3 kali kali  80 Apr 12 17:01 logs
drwxr-xr-x 15 kali kali 300 Apr 12 17:01 objects
-rw-r--r--  1 kali kali 181 Apr 12 17:01 packed-refs
drwxr-xr-x  5 kali kali 100 Apr 12 17:01 refs
```
Let's check the log of git commits 

![image](https://user-images.githubusercontent.com/72421091/114437996-bc462980-9bb6-11eb-9213-3f18166f550c.png)

We can see an old text in the flag.txt 
  
```
Your princess is in another castle
``` 
Let's check the packed-refs  
  
```
cat packed-refs
# pack-refs with: peeled fully-peeled sorted
b123f674a07eaf5914eda8845d86b5219fc1de11 refs/remotes/origin/!flag
dcc402050827e92dbcf2578e24f2cba76f34229c refs/remotes/origin/master
```
Let's check the **origin/!flag** 

![image](https://user-images.githubusercontent.com/72421091/114439044-10054280-9bb8-11eb-9c69-b16d3139671e.png)

## Flag

```
RS{git_is_just_a_tre3_with_lots_of_branches}
```
