# Challenge Name: MemeCTF 2 Electric Boogaloo





![date](https://img.shields.io/badge/date-18.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-OSINT-blueviolet.svg)   
![value](https://img.shields.io/badge/value-469-blue.svg)  
![score](https://img.shields.io/badge/score-5/10-ff69b4.svg)

## Description

9c222530fc5822720b24a18e0c5200957fcbe169589915c963e765c99c7f5f3a

## Detailed solution

Start by searching using the hash and i found a github profil 

![image](https://user-images.githubusercontent.com/72421091/115180512-4285d280-a0c5-11eb-91dc-41acf0bb193a.png)

We can see the hash in the repository ```Hmmmmmmmmmmmmmmmmmmmmmmmmm```  

![image](https://user-images.githubusercontent.com/72421091/115180553-5c271a00-a0c5-11eb-8b38-e3b639b1fa2c.png)

I tried to check git log with the .git folder but no commits for a flag

The folder old_files/data is an old repository 

```
total 20
drwxr-xr-x  7 kali kali 240 Apr 19 04:13 .
drwxr-xr-x  3 kali kali  80 Apr 19 04:13 ..
-rw-r--r--  1 kali kali  20 Apr 19 04:13 COMMIT_EDITMSG
-rw-r--r--  1 kali kali  92 Apr 19 04:13 config
-rw-r--r--  1 kali kali  73 Apr 19 04:13 description
-rw-r--r--  1 kali kali  23 Apr 19 04:13 HEAD
drwxr-xr-x  2 kali kali 280 Apr 19 04:13 hooks
-rw-r--r--  1 kali kali 137 Apr 19 04:13 index
drwxr-xr-x  2 kali kali  60 Apr 19 04:13 info
drwxr-xr-x  3 kali kali  80 Apr 19 04:13 logs
drwxr-xr-x 11 kali kali 220 Apr 19 04:13 objects
drwxr-xr-x  3 kali kali  60 Apr 19 04:13 refs
```

Let's check the git log for commits ```git log -p```

![image](https://user-images.githubusercontent.com/72421091/115181236-fb98dc80-a0c6-11eb-8610-30da59375e7d.png)


We got our flag

## Flag

```
UMDCTF-{f0r_th3_m3m3}
```
