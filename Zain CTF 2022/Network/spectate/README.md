# Challenge Name: M4Lw4r3

![date](https://img.shields.io/badge/date-19.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Network-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

Two PCs on the same network are communicating using TCP channel, what is the flag?

[https://hubchallenges.s3.eu-west-1.amazonaws.com/Forensics/spectate.zip](https://hubchallenges.s3.eu-west-1.amazonaws.com/Forensics/spectate.zip)

## Detailed solution

We have a pcap file let's use wireshark to analyze packets

Description mention TCP so we gonna focus TCP connections

![image](https://user-images.githubusercontent.com/72421091/159141822-0b96eef0-e65c-4e1a-8ae8-925843691af6.png)

Following the first stream "tcp.stream eq 0" show a plaintext message

**10.0.0.21:60596 -> 10.0.0.24:x11 (86 bytes)**

```
Hello, Agent; 

I will send private data through port 7754 

use password: d0L1x65900Q

```

Now let's focus the tcp port 7754 using the filtre "tcp.port == 7754"  

We found that the tcp stream 5 has an archive file identified by PK and data.txt (probably the compressed file)

**10.0.0.21:49172 -> 10.0.0.24:7754 (215 bytes)**

```
00000000  50 4b 03 04 33 03 01 00  63 00 99 7c 96 53 00 00 PK..3... c..|.S..
00000010  00 00 2b 00 00 00 17 00  00 00 08 00 0b 00 64 61 ..+..... ......da
00000020  74 61 2e 74 78 74 01 99  07 00 02 00 41 45 01 00 ta.txt.. ....AE..
00000030  00 b1 99 db 2d f3 cc 67  79 8e 99 88 ad 53 e5 d7 ....-..g y....S..
00000040  51 d8 39 5f 59 0f c9 8f  24 2a 9a ec de 27 fe f7 Q.9_Y... $*...'..
00000050  3c 6a ed f5 c7 61 2f a6  cb 19 26 45 50 4b 01 02 <j...a/. ..&EPK..
00000060  3f 03 33 03 01 00 63 00  99 7c 96 53 00 00 00 00 ?.3...c. .|.S....
00000070  2b 00 00 00 17 00 00 00  08 00 2f 00 00 00 00 00 +....... ../.....
00000080  00 00 20 80 a4 81 00 00  00 00 64 61 74 61 2e 74 .. ..... ..data.t
00000090  78 74 0a 00 20 00 00 00  00 00 01 00 18 00 80 86 xt.. ... ........
000000A0  dd a4 73 f7 d7 01 80 67  d3 aa 73 f7 d7 01 80 86 ..s....g ..s.....
000000B0  dd a4 73 f7 d7 01 01 99  07 00 02 00 41 45 01 00 ..s..... ....AE..
000000C0  00 50 4b 05 06 00 00 00  00 01 00 01 00 65 00 00 .PK..... .....e..
000000D0  00 5c 00 00 00 00 00                             .\.....

```

Now let's choose raw output and save file 

![image](https://user-images.githubusercontent.com/72421091/159142032-290d3466-278a-417f-9dbd-36656b9aaa88.png)


Checking the file show that it's a zip archive 

![image](https://user-images.githubusercontent.com/72421091/159142029-2fa254ac-1923-482a-894d-12314a5a94d1.png)


The zip file is protected by a password. Let's use the one from the first message **d0L1x65900Q**

We found our flag inside data.txt file

## Flag

```
flag{p0rt_sp3ct4at3_w$}
```
