# Challenge Name: TheJudgment


![date](https://img.shields.io/badge/date-19.06.2021-brightgreen.svg)  
![Steganography category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   


## Description

You are in the day before your judgment where Decim gives you a chance by challenging you to unhide the secret message which is hidden within the picture but you have only two options, either unhide the flag so you can get another chance to live your life or you will be sent to hell with no mercy.  

[decim.png](decim.png)  

Author : [Lelouche01](https://github.com/Lelouche01)

Challenge link : https://github.com/Lelouche01/TheJudgment 

## Detailed solution

Start by downloading the png image and check for some details  
  
```bash
┌──(kali㉿kali)-[~]
└─$ file decim.png                                                                             
decim.png: PNG image data, 1920 x 1428, 8-bit/color RGB, non-interlaced
```  

```bash  

┌──(kali㉿kali)-[~]
└─$ exiftool decim.png
ExifTool Version Number         : 12.16
File Name                       : decim.png
Directory                       : .
File Size                       : 1370 KiB
File Modification Date/Time     : 2021:06:19 15:25:10+00:00
File Access Date/Time           : 2021:06:19 15:25:09+00:00
File Inode Change Date/Time     : 2021:06:19 15:25:10+00:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1920
Image Height                    : 1428
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 1920x1428
Megapixels                      : 2.7

```  

Let's check for embedded files using binwalk  

```bash  

┌──(kali㉿kali)-[~]
└─$ binwalk decim.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1920 x 1428, 8-bit/color RGB, non-interlaced

```  

As we can see the file is only a png image  

Now let's focus in the image and try some known methodes used for hidding data. I tried couple things but without success 

- strings -n 6 decim.png : Check for some strings in the file, nothing suspicious  
- [StegSolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install) : Check different planes
- [Stegonline](https://stegonline.georgeom.net/upload) : Check for lsb, colour palette...  

Probably the secret message is not an image so let's try a known tool used for detect hidding data in png called [**Zsteg**](https://github.com/zed-0xff/zsteg)  

![image](https://user-images.githubusercontent.com/72421091/122651154-cba1a000-d12e-11eb-97e4-a387d123f1a5.png)

We found our flag with the payload  **b8,b,lsb,xy**  

We can extract the file using  ``` zsteg -E b8,b,lsb,xy decim.png > flag ```

![image](https://user-images.githubusercontent.com/72421091/122651343-1374f700-d130-11eb-8d7a-092ae3cd084f.png) 

We found our flag 



## Flag

```
Th3 Fl4g 1s{1 4p0l0g153. 4 W45 M4k1n9 4 5m477 J0k3}
```
