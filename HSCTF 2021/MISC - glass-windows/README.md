# Challenge Name: pallets-of-gold


![date](https://img.shields.io/badge/date-16.06.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![misc category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   
![value](https://img.shields.io/badge/value-311-blue.svg)  


## Description

I found a cool glass texture.


[glass-windows.png](glass-windows.png)

## Detailed solution

Check image details 

```
┌──(kali㉿kali)-[~]
└─$ file glass-windows.png
glass-windows.png: PNG image data, 3722 x 227, 8-bit gray+alpha, non-interlaced
```

```
┌──(kali㉿kali)-[~]
└─$ exiftool glass-windows.png
ExifTool Version Number         : 12.16
File Name                       : glass-windows.png
Directory                       : .
File Size                       : 26 KiB
File Modification Date/Time     : 2021:06:16 21:51:06+00:00
File Access Date/Time           : 2021:06:20 01:20:39+00:00
File Inode Change Date/Time     : 2021:06:20 01:20:39+00:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 3722
Image Height                    : 227
Bit Depth                       : 8
Color Type                      : Grayscale with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 3722x227
Megapixels                      : 0.845
```  

Let's use Stegsolve https://github.com/zardus/ctf-tools/blob/master/stegsolve/install 

colour inversion(xor) show the flag image  


![solved](https://user-images.githubusercontent.com/72421091/122659336-13e0b280-d16f-11eb-87ce-fdd21f29dbda.png)


## Flag

```
flag{this_is_why_i_use_premultiplied_alpha}
```
