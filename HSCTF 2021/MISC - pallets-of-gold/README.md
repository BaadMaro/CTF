# Challenge Name: pallets-of-gold


![date](https://img.shields.io/badge/date-16.06.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![misc category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   
![value](https://img.shields.io/badge/value-289-blue.svg)  


## Description

It doesn't really look like gold to me...

[pallets-of-gold.png](pallets-of-gold.png)

## Detailed solution

Checking the image file 

```
┌──(kali㉿kali)-[~]
└─$ file pallets-of-gold.png
pallets-of-gold.png: PNG image data, 3191 x 227, 8-bit colormap, non-interlaced
``` 

```
┌──(kali㉿kali)-[~]
└─$ exiftool pallets-of-gold.png
ExifTool Version Number         : 12.16
File Name                       : pallets-of-gold.png
Directory                       : .
File Size                       : 683 KiB
File Modification Date/Time     : 2021:06:16 21:50:39+00:00
File Access Date/Time           : 2021:06:20 00:53:55+00:00
File Inode Change Date/Time     : 2021:06:20 00:53:55+00:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 3191
Image Height                    : 227
Bit Depth                       : 8
Color Type                      : Palette
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Palette                         : (Binary data 768 bytes, use -b option to extract)
Image Size                      : 3191x227
Megapixels                      : 0.724
``` 
Challenge name pallets is refering to colour palette (bitmap) 

Let's use stegonline to check for colour palette https://stegonline.georgeom.net/upload 

![image](https://user-images.githubusercontent.com/72421091/122659033-4d172380-d16b-11eb-98bd-dcd6e196e317.png)

Let's browse colour palette

![image](https://user-images.githubusercontent.com/72421091/122659061-8fd8fb80-d16b-11eb-9ce4-13f783056975.png)

![image](https://user-images.githubusercontent.com/72421091/122659073-98313680-d16b-11eb-85b5-424f53867f3c.png)

We can see our flag 




## Flag

```
flag{plte_chunks_remind_me_of_gifs}
```
