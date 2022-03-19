# Challenge Name: squirrel

![date](https://img.shields.io/badge/date-19.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

an image tells a story, try to discover more details

https://hubchallenges.s3.eu-west-1.amazonaws.com/Forensics/squirrel.zip

## Detailed solution

![squirrel](https://user-images.githubusercontent.com/72421091/159141059-37cd82ea-5f6f-4bb2-9fb1-752ef7e2adee.jpg)

After checking image strings, we found a mediafire link

```bash
┌──(kali㉿kali)-[~]
└─$ strings -n 10 squirrel.jpg                                                                                                                 1 ⨯
bPhotoshop 3.0
ioncfvl/kdal/je
afgnbvikmjkwvasbf7dw es 6qtntekias dteewf.zas/ddsas.......
https://www.mediafire.com/file/yuy6pf4pj3004em/iamnotreal.zip/file
```
The zip file is protected by a password let's try crack it using john

```
zip2john iamnotreal.zip > hash.txt
```
```bash
┌──(kali㉿kali)-[~]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
squirrel07       (iamnotreal.zip/evil/EVIL)
1g 0:00:00:00 DONE (2022-03-18 23:32) 4.545g/s 5736Kp/s 5736Kc/s 5736KC/s squirrel44..squiby
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
```bash
┌──(kali㉿kali)-[~]
└─$ john hash.txt --show
iamnotreal.zip/evil/EVIL:squirrel07:evil/EVIL:iamnotreal.zip::iamnotreal.zip

1 password hash cracked, 0 left
```
The password is **squirrel07**. let's unzip the file

```bash
┌──(kali㉿kali)-[~]
└─$ file evil/EVIL
evil/EVIL: data
```
We have a uknow file let's check hex values

```bash
┌──(kali㉿kali)-[~]
└─$ xxd -l 50 evil/EVIL
00000000: a119 74bc 0010 4a46 4946 0001 0101 0048  ..t...JFIF.....H
00000010: 0048 0000 ffed 1b62 5068 6f74 6f73 686f  .H.....bPhotosho
00000020: 7020 332e 3000 3842 494d 0425 0000 0000  p 3.0.8BIM.%....
00000030: 0010                                     ..

```

We can see JFIF, and Photoshop et some exif related stuff. It's a jpeg file we need to fix the header. I'll use HxD

https://en.wikipedia.org/wiki/List_of_file_signatures

![image](https://user-images.githubusercontent.com/72421091/159141454-48b284fc-378f-4fa9-94eb-42556396897c.png)

Old file
![image](https://user-images.githubusercontent.com/72421091/159141428-754ca412-515f-4a5a-919b-81648ad96a11.png)

New file
![image](https://user-images.githubusercontent.com/72421091/159141416-c05ead81-c745-436a-aaca-eb4a214171d2.png)

Output

![1](https://user-images.githubusercontent.com/72421091/159141464-c9b18dd7-0cbc-47a2-91b4-1f00408d4a0d.jpg)

MZWGCZ33IV3DC3C7KM4XK2LSOIZWY6T5

Using cyberchef we found that it's a base32 encoded string let's decode it

https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')&input=TVpXR0NaMzNJVjNEQzNDN0tNNFhLMkxTT0laV1k2VDU


## Flag

```
flag{Ev1l_S9uirr3lz} 
```
