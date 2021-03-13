
# Challenge Name: Investigator 


![date](https://img.shields.io/badge/date-12.03.2021-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg) 
![misc category](https://img.shields.io/badge/category-misc-lightgrey.svg)
![score](https://img.shields.io/badge/score-400-blue.svg)


## Attached files
- [factory.bz2](factory.bz2)
- [factory.jpg](factory.jpg)





## Detailed solution

The challenge give us a file called factory.bz2 and tell us the flag is that plus code of the factory/dealer/shop establishment.  
Start by downloading the factory.bz2 and try to extract it.

```bash
file factory.bz2
factory.bz2: bzip2 compressed data
```
It's a bzip2 file let's extract it with bzip2

```bash
bzip2 -d factory.bz2                                                  
bzip2: factory.bz2 is not a bzip2 file.
```

The extraction failed because the file is not a bzip2 file. but why it shows bzip2 compressed data ?

A file header is a 'signature' placed at the beginning of a file, so the operating system and other software know what to do with the following contents. Possibly that it could be a false bzip2 header to hide hide data.



Run strings on the file :

```bash
strings factory.bz2                                                     2 ⨯
JFIF
Exif

.............
```

We can see JFIF a the the beginning, it's a JPEG image. We need to fix the header to recover the image.

```bash
 xxd factory.bz2 | less
00000000: 425a 68e0 0010 4a46 4946 0001 0100 0001  BZh...JFIF......
```
JPEG header : 
https://en.wikipedia.org/wiki/List_of_file_signatures

```
FF D8 FF E0 00 10 4A 46 49 46 00 01 ÿØÿà..JFIF..
```
Using any Hex editor to fix the file header and save the new file as .jpg. I used Ghex. 

```bash
file factory1.jpg
factory1.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=5, xresolution=74, yresolution=82, resolutionunit=1, GPS-Data], progressive, precision 8, 1040x690, components 3
```

[!image](factory.jpg)

We can see in the flags : RENAULT rabljena vozila

That image has also some exif metadata let's run exiftool :

```bash
exiftool factory.jpg
ExifTool Version Number         : 12.16
File Name                       : factory.jpg
Directory                       : .
File Size                       : 47 KiB
File Modification Date/Time     : 2021:03:13 17:47:37+00:00
File Access Date/Time           : 2021:03:13 17:47:37+00:00
File Inode Change Date/Time     : 2021:03:13 17:47:37+00:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 1
Y Resolution                    : 1
Resolution Unit                 : None
Y Cb Cr Positioning             : Centered
GPS Version ID                  : 2.3.0.0
GPS Latitude                    : 45 deg 48' 0.15"
XMP Toolkit                     : Image::ExifTool 12.14
Creation Date                   : 2021:02:28 13:08:06+01:00
Image Width                     : 1040
Image Height                    : 690
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1040x690
Megapixels                      : 0.718
```

We have a gps latitude 45 deg 48' 0.15" and the gps altitude is missing. In the challenge description the solution is to find the plus code.  

Plus Codes are like street addresses for people or places that don’t have one. Instead of addresses with street names and numbers, Plus Codes are based on latitude and longitude, and displayed as numbers and letters.
https://maps.google.com/pluscodes/

We can't find the place directly without gps altitude so we need to collect all the information that we have to find place in the image.

We have an XMP:CreateDate that support time zone unlike EXIF:CreateDate. It mention the GMT +1 time zone.

```
Creation Date                   : 2021:02:28 13:08:06+01:00
```
So the place that we search it's in a GMT +1 time zone.  

The GPS latitude 45 deg 48' 0.15" is in the DMS(Degrees Minutes Seconds) format we can convert it the the DD (decimal degrees) :
```
45° 48' 0.15" = 45° + 48'/60 + 0.15"/3600 = 45.80004°
```
![](http://sncyear8geography.weebly.com/uploads/5/7/7/8/57782431/8484702.png)

Something missing from GPS latitude, 45°-46° North or South ?

We start using the text in the image "renault rabljena vozila". After searhing we find some croatian, solvenian language. Using google translet :

```
SLOVENIAN renault rabljena vozila <--> ENGLISH renault used cars
CROATIAN rabljena vozila <--> ENGLISH used vehicles
```

Croatian language : 
 - Native to: Croatia, Bosnia and Herzegovina, Serbia (Vojvodina), Montenegro, Romania (Caraș-Severin County)  
Slovenian lnaguage :  
 - Native to	Slovenia, Italy (Friuli Venezia Giulia), Austria (Carinthia and Styria)

Slovene and Croatian are Slavic languages, both members of the South Slavic group, which also includes Serbian, Macedonian, and Bulgarian.  

![](http://travels.bowenplace.com/europe_2008/language/files/651px-slavic_languages.png)  

We know now that the GPS latitude is North, we search the 45°-46° North and use also the timzezone that we founded. 

![](https://www.timetemperature.com/tzmaps/europe-time-zone-map.gif)

The parallel 45° north passes through :
https://en.wikipedia.org/wiki/45th_parallel_north

```
45°0′N 6°44′E	 Italy
45°0′N 13°44′E	 Croatia	Istrian Peninsula, islands of Cres and Krk, and the mainland again
45°0′N 15°46′E	 Bosnia and Herzegovina	
45°0′N 18°44′E	 Croatia	
45°0′N 19°6′E	 Serbia	Passing through the centre of Ruma and through northern part of Sremska Mitrovica
Passing through the northern edge of Stara Pazova, 30 kilometres NW of Belgrade
```



The parallel 46° north passes through :
https://en.wikipedia.org/wiki/46th_parallel_north  

```
46°0′N 7°53′E	 Italy	Passing through Lake Maggiore near Luino
46°0′N 9°1′E	 Italy	Passing through Lake Como
46°0′N 13°29′E	 Slovenia	Passing just south of Ljubljana
46°0′N 15°42′E	 Croatia	
46°0′N 17°18′E	 Hungary	
46°0′N 19°4′E	 Serbia	For about 7 km
46°0′N 19°9′E	 Hungary	For about 4 km
46°0′N 19°12′E	 Serbia	For about 2 km
46°0′N 19°14′E	 Hungary	For about 5 km
46°0′N 19°18′E	 Serbia	passing just south of Subotica
```

Our lattitude 45.80004° N is close to parrallel 46° N so we need to do some research between them using google map. We search for renault rabljena vozila places 

![image](https://user-images.githubusercontent.com/72421091/111044670-3ebdbb00-844a-11eb-907f-20f028ec8a76.png)

I started checking images from the places founded in search in the area 45° to 46° N. Getting close to lattitude 45.80004° N i founded a place in Novo mesto, 8000, Slovenia : 
![image](https://user-images.githubusercontent.com/72421091/111045012-1636c080-844c-11eb-9161-10f3d9d93021.png)

Checking images and 360 street view we finally found our place @45.8000934,15.1740731 which is our lattitude 45.80004° 

![image](https://user-images.githubusercontent.com/72421091/111046310-010e6180-844d-11eb-8ae5-bc3a9be5f46c.png)

Place code is : ```Q5XF+VG Novo mesto, Slovenia```  

The flag is in the following form: IDEH{the_plus_code} Example: IDEH{ABCD+EF}


## Flag

```
IDEH{Q5XF+VG}
```
