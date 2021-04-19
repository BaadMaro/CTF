# Challenge Name: Coldplay's Flags






![date](https://img.shields.io/badge/date-18.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-289-blue.svg)  
![score](https://img.shields.io/badge/score-5/10-ff69b4.svg)

## Description

I just downloaded Coldplay's latest song and noticed that my song file seems a bit odd. Can you help me figure out what's up with my file?

Note: For the password, think words, not characters

https://drive.google.com/drive/folders/1e0D5LElerPu9VcUm2bKp5j542CLuNadB?usp=sharing

## Detailed solution

The song is **Coldplay Flags**  

Start by checking the file 
  
```
file flags.wav
flags.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 44100 Hz
```  
```
exiftool flags.wav
ExifTool Version Number         : 12.16
File Name                       : flags.wav
Directory                       : .
File Size                       : 36 MiB
File Modification Date/Time     : 2021:04:18 16:53:30+00:00
File Access Date/Time           : 2021:04:18 16:53:30+00:00
File Inode Change Date/Time     : 2021:04:18 16:53:56+00:00
File Permissions                : rw-r--r--
File Type                       : WAV
File Type Extension             : wav
MIME Type                       : audio/x-wav
Encoding                        : Microsoft PCM
Num Channels                    : 2
Sample Rate                     : 44100
Avg Bytes Per Sec               : 176400
Bits Per Sample                 : 16
Software                        : Lavf58.45.100
Duration                        : 0:03:37
```  
The file size kinda large for a song, let's check binwalk for some embedded data  

``` 
binwalk -e flags.wav

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
712822        0xAE076         MySQL ISAM compressed data file Version 1
845224        0xCE5A8         MySQL ISAM index file Version 1
6088742       0x5CE826        MySQL MISAM index file Version 3
6936308       0x69D6F4        MySQL ISAM compressed data file Version 1
20443148      0x137F00C       MySQL ISAM compressed data file Version 6
27679314      0x1A65A52       MySQL MISAM index file Version 5
28755155      0x1B6C4D3       MySQL MISAM index file Version 8
35886544      0x22395D0       MySQL MISAM compressed data file Version 1
36095154      0x226C4B2       MySQL ISAM compressed data file Version 4
38195278      0x246D04E       Zip archive data, encrypted at least v1.0 to extract, compressed size: 45, un compressed size: 33, name: flag.txt
38195483      0x246D11B       End of Zip archive, footer length: 22
38195505      0x246D131       Zip archive data, at least v2.0 to extract, compressed size: 82, uncompressed  size: 97, name: hint.txt
38195731      0x246D213       End of Zip archive, footer length: 22
```  

We can see two zip files with ```flag.txt``` and ```hint.txt```. Let's extract the zip files using **dd**  

**flag.zip ( flag.txt)** 
  
```
dd if=flags.wav of=flag.zip bs=1 skip=38195278 count=227
227+0 records in
227+0 records out
227 bytes copied, 0.00112051 s, 203 kB/s
```  

**hint.zip ( hint.txt)** 

```
dd if=flags.wav of=hint.zip bs=1 skip=38195505
248+0 records in
248+0 records out
248 bytes copied, 0.0017693 s, 140 kB/s
```
The flag.zip is protected by a password so we need to check the hint file 

Let's decompress hint.zip and read the hint.txt file 

```
Assume all characters are lowercase
password: (1:49)_(1:01)_(0:16)_(0:56)_(0:17)_(1:33)_a_(1:34)?     
```
Password parts is words from the song, we need to listen and list words using timeline 

I used deezer to see the lyrics in real time  : https://www.deezer.com/en/track/1182616162 

![image](https://user-images.githubusercontent.com/72421091/115186171-bf6a7980-a0d0-11eb-9fd2-b2155e324629.png)

I listed lyrics by time and listen to the words used at the exact timing 

```
1:49 : I know that I am living, but can you show me how to live? | can you
1:01 : To be Pyotr Tchaikovsky | Tchaikovsky
0:16 : Talk among the skeletons this morning | Talk
0:56 : Was to be whatever they wanted to be | to be
0:17 : Talk among the skeletons this morning | the skeletons
1:33 : You may telephone in by a ouija | by 
a
1:34 : You may telephone in by a ouija | ouija
```  

can_Tchaikovsky_Talk_to_skeletons_by_a_ouija?

Combine them for the password and use lowercase : ```can_tchaikovsky_talk_to_skeletons_by_a_ouija?``` 

Let's decompress the flag.zip using the password  

```
unzip flag.zip
Archive:  flag.zip
[flag.zip] flag.txt password:
 extracting: flag.txt
``` 
Let's read the flag.txt  

```
cat flag.txt
UMDCTF-{PY07r_11Y1CH_7CH41K0V5KY}   
```
## Flag

```
UMDCTF-{PY07r_11Y1CH_7CH41K0V5KY}   
```
