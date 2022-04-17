# Challenge Name: Baby Steg


![date](https://img.shields.io/badge/date-16.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  


## Description

Just another Random baby steganography challenge

[challenge.png](https://thnbdarija.ctfd.io/files/abc68b1e4c21777a54c8d0405e05f38a/challenge.png?token=eyJ1c2VyX2lkIjoyNywidGVhbV9pZCI6MTUsImZpbGVfaWQiOjR9.Ylstbg.ShsASWBKVEfuUWzwrnrOc_PT3Ck)


## Detailed solution

![challenge](https://user-images.githubusercontent.com/72421091/163734941-7498b208-dab2-4458-8477-0187dabff8cf.png)

```bash
┌──(kali㉿kali)-[~]
└─$ file challenge.png
challenge.png: PNG image data, 419 x 610, 8-bit/color RGBA, non-interlaced
```
It's a png image let's check metadata

```bash
┌──(kali㉿kali)-[~]
└─$ exiftool challenge.png
ExifTool Version Number         : 12.40
File Name                       : challenge.png
Directory                       : .
File Size                       : 411 KiB
File Modification Date/Time     : 2022:04:16 20:56:18+00:00
File Access Date/Time           : 2022:04:16 20:56:18+00:00
File Inode Change Date/Time     : 2022:04:17 22:45:34+00:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 419
Image Height                    : 610
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Significant Bits                : 8 8 8 8
Image Size                      : 419x610
Megapixels                      : 0.256
```  

Nothing special. Now let's switch to stegano detection, i'll use zsteg because we have a png image

```bash
┌──(kali㉿kali)-[~]
└─$ zsteg challenge.png
b1,r,lsb,xy         .. text: "[<GZ2Zfv9Z@"
b1,rgb,lsb,xy       .. text: "thnb{St3g4n0graphy_1s_C0ol_th0}"
b2,r,msb,xy         .. text: "@DQP@AETU"
b2,rgba,lsb,xy      .. text: ";+++++++"
b2,abgr,msb,xy      .. text: "WSSSWWGCGCWW"
b3,bgr,lsb,xy       .. text: "h4Z- X(&"
b4,r,msb,xy         .. text: "\"wwPwWsg#&5wwwwww!$b1ww"
b4,g,lsb,xy         .. text: "fB\"bDDDBfN"
b4,g,msb,xy         .. text: "w DRdpqtsvd&!DaF"
b4,b,msb,xy         .. text: "UUUUs$fs"
b4,rgb,msb,xy       .. text: "3t`D!R&c6cpA"
b4,bgr,msb,xy       .. text: "u4d AVb#3v`@"
b4,rgba,lsb,xy      .. text: "/(OJoLol"
b4,abgr,msb,xy      .. text: "/Ao%o#?c"
```

We found our flag with the payload "b1,rgb,lsb,xy" 

## Flag

```
thnb{St3g4n0graphy_1s_C0ol_th0}
```
