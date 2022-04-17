# Challenge Name: Impostor


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-100-blue.svg)  


## Description

yesterday we lost one of our flags and the impostor left us this picture help us retrieve the flag   

_Author: c3p0_

[Impostor_image.png](https://thnbdarija.ctfd.io/files/4d20b1e15a8f607f44f092b872268516/Impostor_image.png?token=eyJ1c2VyX2lkIjoyNywidGVhbV9pZCI6MTUsImZpbGVfaWQiOjI1fQ.YltZRw.EEfr3l2WHYkaRumuVwpyf0ZnzQM)

## Detailed solution

![Impostor_image](https://user-images.githubusercontent.com/72421091/163735246-8b72372f-6fdc-41ad-bdc1-91e5607c7bd3.png)

```bash
┌──(kali㉿kali)-[~]
└─$ file Impostor_image.png
Impostor_image.png: PNG image data, 250 x 450, 8-bit/color RGB, non-interlaced
```  
  
It's a png image let's check metadata

```bash
┌──(kali㉿kali)-[~]
└─$ exiftool Impostor_image.png
ExifTool Version Number         : 12.40
File Name                       : Impostor_image.png
Directory                       : .
File Size                       : 31 KiB
File Modification Date/Time     : 2022:04:17 00:01:28+00:00
File Access Date/Time           : 2022:04:17 00:01:28+00:00
File Inode Change Date/Time     : 2022:04:17 22:57:41+00:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 250
Image Height                    : 450
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 250x450
Megapixels                      : 0.113

```


Nothing special. Now let's switch to stegano detection, i'll use zsteg because we have a png image

```bash
┌──(kali㉿kali)-[~]
└─$ zsteg Impostor_image.png                                                              1 ⨯
imagedata           .. file: PDP-11 UNIX/RT ldp
b1,b,lsb,xy         .. text: "[?{r5Cu]"
b1,bgr,lsb,xy       .. text: "thnb{w3ll_d0ne_y0u_gOt_TH3_imp0sT0r}====="
b3,r,msb,xy         .. file: Targa image data 36 x 1170 x 8 +8210 - 2-bit alpha - four way interleave " @\222$H\002"
b3,b,lsb,xy         .. file: gfxboot compiled html help file
b3,rgb,msb,xy       .. file: Applesoft BASIC program data, first line number 2
b4,g,lsb,xy         .. file: 0420 Alliant virtual executable not stripped
b4,b,lsb,xy         .. file: PDP-11 UNIX/RT ldp
b4,rgb,lsb,xy       .. file: 0421 Alliant compact executable not stripped

```



We found our flag with the payload "b1,bgr,lsb,xy" 

## Flag

```
thnb{w3ll_d0ne_y0u_gOt_TH3_imp0sT0r}
```
