# Challenge Name: Hack0r



![date](https://img.shields.io/badge/date-13.03.2022-brightgreen.svg)  
![solved](https://img.shields.io/badge/solved-after%20CTF-red.svg)    
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-15-blue.svg)  

## Description

Created By **sicmundos**

Someone sent me these files, I doubt That there is a secret message, but I can't find it
https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/sKyXB72pOhoAk3889Y04DSpx1oVJu7KhdhcLRYcH.zip

## Notes

After extracting the attachement file we found 3 files 

```
h4cker.wav  hack3r.jpg  hacker.jpg
```

**hack3r.jpg** has a base64 comment **cDQ1NXcwcmQ=** we can find it using strings too

```bash
┌──(kali㉿kali)-[~/hackers]
└─$ exiftool hack3r.jpg                                                                                                                    
ExifTool Version Number         : 12.40
File Name                       : hack3r.jpg
Directory                       : .
File Size                       : 16 KiB
File Modification Date/Time     : 2022:03:05 18:06:36+00:00
File Access Date/Time           : 2022:03:05 18:06:36+00:00
File Inode Change Date/Time     : 2022:03:09 02:43:13+00:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Comment                         : cDQ1NXcwcmQ=
Image Width                     : 600
Image Height                    : 398
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 600x398
Megapixels                      : 0.239
```

Let's decode it

```bash
┌──(kali㉿kali)-[~/hackers]
└─$ echo "cDQ1NXcwcmQ=" | base64 -d                                                                                                        
p455w0rd
```
hacker.jpg has also a base64 comment



```bash
┌──(kali㉿kali)-[~/hackers]
└─$ exiftool hacker.jpg                                                                                                                   
ExifTool Version Number         : 12.40
File Name                       : hacker.jpg
Directory                       : .
File Size                       : 21 KiB
File Modification Date/Time     : 2022:03:05 18:02:06+00:00
File Access Date/Time           : 2022:03:05 18:02:06+00:00
File Inode Change Date/Time     : 2022:03:09 02:43:13+00:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Comment                         : SURFSA==
Image Width                     : 600
Image Height                    : 400
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 600x400
Megapixels                      : 0.240

```

```bash
┌──(kali㉿kali)-[~/hackers]
└─$ echo "SURFSA==" | base64 -d                                                                                                           
IDEH 
```
h4cker.wav file has nothing in exif adn strings data 

I switch to steghide detection and use steegseek to do some bruteforce. I found that a file was hidden in wav file using passphrase honeymoon

```bash
┌──(kali㉿kali)-[~/hackers]
└─$ stegseek h4cker.wav                                                                                                                    
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "honeymoon"
[i] Original filename: "h4cker.txt".
[i] Extracting to "h4cker.wav.out".
```
```
┌──(kali㉿kali)-[~/hackers]
└─$ cat h4cker.wav.out                                                                                                                 
65LTGNTHKTD5   
```
I have grouped all the elements found to a single wordlist to use it for bruteforcing the others files. I found that a file was hidden in hacker.jpg file using passphrase IDEH
 

```bash
┌──(kali㉿kali)-[~/hackers]
└─$ stegseek -wl 1.txt hacker.jpg                                                                                                      
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "IDEH"
[i] Original filename: "hacker.txt".
[i] Extracting to "hacker.jpg"
```

```bash
┌──(kali㉿kali)-[~/hackers]
└─$ cat hacker.jpg.out                                                                                                                    
INJESU2JKN5XG5    
```
I found that a file was hidden in hack3r.jpg file using passphrase cDQ1NXcwcmQ=

```
┌──(kali㉿kali)-[~/hackers]
└─$ stegseek -wl ../1.txt hack3r.jpg
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "cDQ1NXcwcmQ="
[i] Original filename: "hack3r.txt".
[i]
Extracting to "hack3r.jpg.out".
```

```
┌──(kali㉿kali)-[~/hackers]
└─$ cat hack3r.jpg.out
BTM42G4327GE2V  
```

65LTGNTHKTD5, INJESU2JKN5XG5 and BTM42G4327GE2V are base32 encoded

with the order "INJESU2JKN5XG5BTM42G4327GE2V65LTGNTHKTD5" we can get our flag using base32 decoding

## Flag

```
CRISIS{st3g4no_15_us3fuL}
```
