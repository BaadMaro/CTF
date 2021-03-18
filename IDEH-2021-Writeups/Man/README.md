
# Challenge Name: Man  


![date](https://img.shields.io/badge/date-17.03.2021-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg) 
![misc category](https://img.shields.io/badge/category-misc-lightgrey.svg)
![score](https://img.shields.io/badge/score-300-blue.svg)


## Attached files
- [man.jpg](man.jpg)





## Detailed solution
We can see just a walking man in the image lets start exploring more.   
```bash
file man.jpg
man.jpg: JPEG image data, JFIF standard 1.02, resolution (DPI), density 72x72, segment length 16, Exif Standard: [TIFF image data, little-endian, direntries=12, description=Stanford professor Michel Serres hikes the Dish on a regular basis., manufacturer=NIKON CORPORATION, model=NIKON D300, orientation=upper-left, xresolution=257, yresolution=265, resolutionunit=2, software=Adobe Photoshop Elements 10.0 Macintosh, datetime=2014:04:24 11:18:11], progressive, precision 8, 405x270, components 3
```
It's a JPEG image that has some metadata, let's run exiftool  
```shell
exiftool man.jpg  

ExifTool Version Number         : 12.16
File Name                       : man.jpg
Directory                       : .
File Size                       : 172 KiB
File Modification Date/Time     : 2021:03:06 18:43:28+00:00
File Access Date/Time           : 2021:03:18 20:30:05+00:00
File Inode Change Date/Time     : 2021:03:18 20:30:35+00:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Exif Byte Order                 : Little-endian (Intel, II)
Image Description               : Stanford professor Michel Serres hikes the Dish on a regular basis.
Make                            : NIKON CORPORATION
Camera Model Name               : NIKON D300
Orientation                     : Horizontal (normal)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Software                        : Adobe Photoshop Elements 10.0 Macintosh
Modify Date                     : 2014:04:24 11:18:11
Artist                          : Linda A. Cicero / Stanford News Service
Copyright                       : Photographs provided by the Stanford University News Service are to be used – with appropriate credit – for                  editorial purposes only. Flopping, altering or otherwise embellishing these photos in any way that changes the photographs' editorial conten                 t is prohibited. Unless otherwise specified, please credit Linda A. Cicero / Stanford University News Service.
Exposure Time                   : 1/4000
F Number                        : 3.5
Exposure Program                : Aperture-priority AE
ISO                             : 250
Exif Version                    : 0220
Date/Time Original              : 2009:05:19 16:26:36
Create Date                     : 2009:05:19 16:26:36
Shutter Speed Value             : 1/4000
Aperture Value                  : 3.5
Exposure Compensation           : -1/3
Max Aperture Value              : 2.8
Metering Mode                   : Multi-segment
Light Source                    : Fine Weather
Focal Length                    : 17.0 mm
Sub Sec Time Original           : 23
Color Space                     : sRGB
Exif Image Width                : 405
Exif Image Height               : 270
Sensing Method                  : One-chip color area
File Source                     : Digital Camera
Scene Type                      : Directly photographed
Exposure Mode                   : Auto
White Balance                   : Manual
Digital Zoom Ratio              : 1
Focal Length In 35mm Format     : 25 mm
Scene Capture Type              : Standard
Gain Control                    : None
Contrast                        : Normal
Saturation                      : Normal
Sharpness                       : Normal
Subject Distance Range          : Unknown
Compression                     : JPEG (old-style)
Thumbnail Offset                : 1360
Thumbnail Length                : 5512
Current IPTC Digest             : 5c4422f08d95db0b92b383c42f31cabe
Coded Character Set             : UTF8
Application Record Version      : 2
Caption-Abstract                : Stanford professor Michel Serres hikes the Dish on a regular basis.
By-line                         : Linda A. Cicero / Stanford News
By-line Title                   : University Photographer
Province-State                  : CA
Copyright Notice                : Photographs provided by the Stanford University News Service are to be used – with appropriate credit – for                  editorial purpos
Time Created                    : 16:26:36-07:00
Sub-location                    : Stanford University
IPTC Digest                     : 5c4422f08d95db0b92b383c42f31cabe
Displayed Units X               : inches
Displayed Units Y               : inches
Print Style                     : Centered
Print Position                  : 0 0
Print Scale                     : 1
Global Angle                    : 30
Global Altitude                 : 30
URL List                        :
Slices Group Name               : walking
Num Slices                      : 1
Pixel Aspect Ratio              : 1
Has Real Merged Data            : Yes
Writer Name                     : Adobe Photoshop Elements
Reader Name                     : Adobe Photoshop Elements 10.0
Photoshop Quality               : 12
Photoshop Format                : Progressive
Progressive Scans               : 3 Scans
XMP Toolkit                     : Adobe XMP Core 5.2-c001 63.139439, 2010/10/12-08:45:30
Creator Tool                    : Adobe Photoshop Camera Raw 7.1 (Macintosh)
Metadata Date                   : 2014:04:24 11:18:11-07:00
Rating                          : 0
Serial Number                   : 3102836
Lens Info                       : 17-55mm f/2.8
Lens                            : 17.0-55.0 mm f/2.8
Image Number                    : 22005
Approximate Focus Distance      : 2
State                           : CA
City                            : Stanford
Authors Position                : University Photographer
Date Created                    : 2009:05:19
Legacy IPTC Digest              : 665386C4871978A8D806076CFCE27454
Color Mode                      : RGB
ICC Profile Name                : sRGB IEC61966-2.1
Location                        : Stanford University
Format                          : image/jpeg
Preserved File Name             : _LAC1998.NEF
Document ID                     : xmp.did:AD6EA2FAC40011E3997CBE47E08729E4
Original Document ID            : B3E9DA8B10992D47A45D1FC3DD423192
Instance ID                     : xmp.iid:F99272DF1F206811822AFAE6D46DF0EC
Native Digest                   : 256,257,258,259,262,274,277,284,530,531,282,283,296,301,318,319,529,532,306,270,271,272,305,315,33432;E5576                 6AC696932394DCC93459BE8B771
Creator Work Email              : lacicero@stanford.edu, newslibrary@stanford.edu
Rights                          : Photographs provided by the Stanford University News Service are to be used – with appropriate credit – for                  editorial purposes only. Flopping, altering or otherwise embellishing these photos in any way that changes the photographs' editorial conten                 t is prohibited. Unless otherwise specified, please credit Linda A. Cicero / Stanford University News Service.
Creator                         : Linda A. Cicero / Stanford News Service
Description                     : Stanford professor Michel Serres hikes the Dish on a regular basis.
History Action                  : saved, derived, saved, derived, saved, saved, saved, saved, saved
History Instance ID             : xmp.iid:9C411FEAC12068119109FD01B58D5EEA, xmp.iid:9D411FEAC12068119109FD01B58D5EEA, xmp.iid:DEEE78C3DA20681                 19109FD01B58D5EEA, xmp.iid:4E528792C42068118C14AB5560FD25FE, xmp.iid:0A80117407206811871F8F05664F4626, xmp.iid:F89272DF1F206811822AFAE6D46DF0                 EC, xmp.iid:F99272DF1F206811822AFAE6D46DF0EC
History When                    : 2014:04:22 13:57:01-07:00, 2014:04:22 13:57:04-07:00, 2014:04:22 13:59:41-07:00, 2014:04:22 14:01:18-07:00,                  2014:04:24 11:10:03-07:00, 2014:04:24 11:18:11-07:00, 2014:04:24 11:18:11-07:00
History Software Agent          : Adobe Photoshop Camera Raw 7.1 (Macintosh), Adobe Photoshop Camera Raw 7.1 (Macintosh), Adobe Photoshop Cam                 era Raw 7.1 (Macintosh), Adobe Photoshop CS6 (Macintosh), Adobe Photoshop Camera Raw 7.1 (Macintosh), Adobe Photoshop Elements 10.0 Macintosh                 , Adobe Photoshop Elements 10.0 Macintosh
History Changed                 : /metadata, /, /, /, /, /, /
History Parameters              : saved to new location, converted from image/dng to image/tiff
Derived From Instance ID        : xmp.iid:0A80117407206811871F8F05664F4626
Derived From Document ID        : xmp.did:DEEE78C3DA2068119109FD01B58D5EEA
Derived From Original Document ID: B3E9DA8B10992D47A45D1FC3DD423192
Flash Fired                     : False
Flash Return                    : No return detection
Flash Mode                      : Unknown
Flash Function                  : False
Flash Red Eye Mode              : False
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Media-Relative Colorimetric
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
DCT Encode Version              : 100
APP14 Flags 0                   : [14]
APP14 Flags 1                   : (none)
Color Transform                 : YCbCr
Image Width                     : 405
Image Height                    : 270
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Aperture                        : 3.5
Image Size                      : 405x270
Megapixels                      : 0.109
Scale Factor To 35 mm Equivalent: 1.5
Shutter Speed                   : 1/4000
Date/Time Original              : 2009:05:19 16:26:36.23
Thumbnail Image                 : (Binary data 5512 bytes, use -b option to extract)
Date/Time Created               : 2009:05:19 16:26:36-07:00
Flash                           : No Flash
Lens ID                         : AF-S DX Zoom-Nikkor 17-55mm f/2.8G IF-ED
Circle Of Confusion             : 0.020 mm
Depth Of Field                  : 2.59 m (1.34 - 3.93 m)
Field Of View                   : 71.5 deg
Focal Length                    : 17.0 mm (35 mm equivalent: 25.0 mm)
Hyperfocal Distance             : 4.04 m
Light Value                     : 14.3
```
The image has some metadata, and a thumbnail image. We can search online for the original image it has the same metadata.  

Let's check for data inside the image file. I'll start by binwalk 

```bash
binwalk man.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
30            0x1E            TIFF image data, little-endian offset of first image directory: 8
1360          0x550           JPEG image data, JFIF standard 1.02
17318         0x43A6          Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"
139687        0x221A7         PDF document, version: "1.4"
139875        0x22263         Zlib compressed data, default compression
140830        0x2261E         Zlib compressed data, default compression
161601        0x27741         Zlib compressed data, default compression
162134        0x27956         Zlib compressed data, default compression
172050        0x2A012         Zlib compressed data, default compression
```

The first part has the image, the thumbnail image and metadata. The second part has pdf and some zlib compressed data.  

We can extract all and start exploring ```binwalk -e --dd='.*' man.jpg```  
 
```bash   
┌──(kali㉿kali)-[~/_man.jpg.extracted]
└─$ file *
0:          JPEG image data, JFIF standard 1.02, resolution (DPI), density 72x72, segment length 16, Exif Standard: [TIFF image data, little-endian, direntries=12, description=Stanford professor Michel Serres hikes the Dish on a regular basis., manufacturer=NIKON CORPORATION, model=NIKON D300, orientation=upper-left, xresolution=257, yresolution=265, resolutionunit=2, software=Adobe Photoshop Elements 10.0 Macintosh, datetime=2014:04:24 11:18:11], progressive, precision 8, 405x270, components 3
1E:         TIFF image data, little-endian, direntries=12, description=Stanford professor Michel Serres hikes the Dish on a regular basis., manufacturer=NIKON CORPORATION, model=NIKON D300, orientation=upper-left, xresolution=257, yresolution=265, resolutionunit=2, software=Adobe Photoshop Elements 10.0 Macintosh, datetime=2014:04:24 11:18:11
2A012:      ASCII text
2A012.zlib: zlib compressed data
43A6:       data
221A7:      PDF document, version 1.4
550:        JPEG image data, JFIF standard 1.02, aspect ratio, density 72x72, segment length 16, baseline, precision 8, 160x107, components 3
2261E:      TrueType Font data, 16 tables, 1st "OS/2", 7 names, Microsoft, language 0x409
2261E.zlib: zlib compressed data
22263:      ASCII text
22263.zlib: zlib compressed data
27741:      ASCII text
27741.zlib: zlib compressed data
27956:      TrueType Font data, 16 tables, 1st "OS/2", 7 names, Microsoft, language 0x409
27956.zlib: zlib compressed data
```  

Checking the PDF 221A7 file 
  
```bash
file 221A7
221A7: PDF document, version 1.4 

binwalk 221A7

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PDF document, version: "1.4"
188           0xBC            Zlib compressed data, default compression
1143          0x477           Zlib compressed data, default compression
21914         0x559A          Zlib compressed data, default compression
22447         0x57AF          Zlib compressed data, default compression
32363         0x7E6B          Zlib compressed data, default compression
```

We can also extract the full pdf using dd 
  
```bash
dd if=man.jpg of=man.pdf bs=1 skip=139687
```
We start by opening the pdf, it's only a whitepage but if we select all we can find some hidden text 

![image](https://user-images.githubusercontent.com/72421091/111699599-a0aa6600-8838-11eb-89ab-df3002edce5f.png)  

```
The only clue I can give you is :
○ copy & paste this b5xDDRmj
○ and make use of this 91a413f0b000245c02b7a74e24ab2b0b
```  
We can also use a tool called pdf2text  

https://github.com/euske/pdfminer/blob/master/tools/pdf2txt.py  

```bash
python3 pdf2txt.py man.pdf
The only clue I can give you is :

○ copy & paste this b5xDDRmj
○ and make use of this 91a413f0b000245c02b7a74e24ab2b0b
```

Let's check strings with our pdf (from dd or binwalk it's the same file). we found some metadata  

```bash
strings man.pdf 

%%EOF%BeginExifToolUpdate
1 0 obj
/Title (4 in roman is : usefulstringhaha)
/Producer (the key of freedom is : idehcitinptevent)
/Author (As Easy aS Cooking Bacon Chips)
endobj
17 0 obj
/Type /Metadata
/Subtype /XML
/Length 3110
stream
<?xpacket begin='
' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 12.16'>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
 <rdf:Description rdf:about=''
  xmlns:dc='http://purl.org/dc/elements/1.1/'>
  <dc:title>
   <rdf:Alt>
    <rdf:li xml:lang='x-default'>4 in roman is : usefulstringhaha</rdf:li>
   </rdf:Alt>
  </dc:title>
 </rdf:Description>
 <rdf:Description rdf:about=''
  xmlns:pdf='http://ns.adobe.com/pdf/1.3/'>
  <pdf:Author>As Easy aS Cooking Bacon Chips</pdf:Author>
  <pdf:Producer>the key of freedom is : idehcitinptevent</pdf:Producer>
 </rdf:Description>
</rdf:RDF>
```  

**Bonus PDF Forensics :**   

We can use some other tools to interact more with the pdf file 

- Using peepdf https://github.com/jesparza/peepdf  : start with interacting with the pdf file, at the stream 17 we found the same additional metadata that contains secrets information.  
- Using pdf-parser https://blog.didierstevens.com/programs/pdf-tools/ : we can find our data at PDF Comment '%%EOF%BeginExifToolUpdate\n' 

Let's analyze what we found  

The only clue I can give you is :  
○ copy & paste this b5xDDRmj  
○ and make use of this 91a413f0b000245c02b7a74e24ab2b0b    

4 in roman is : usefulstringhaha  
As Easy aS Cooking Bacon Chips  
the key of freedom is : idehcitinptevent   

4 in roman is : IV  -> IV = usefulstringhaha  
As Easy aS Cooking Bacon Chips : uppercase hint for AES CBC encryption  
the key of freedom is : idehcitinptevent -> encryption key = idehcitinptevent   

So we have an AES CBC Encyption  

https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation    

![image](https://user-images.githubusercontent.com/72421091/111702457-92f6df80-883c-11eb-856a-31772cc81977.png)

![image](https://user-images.githubusercontent.com/72421091/111702477-9a1ded80-883c-11eb-93f2-735c60d15a89.png)

We have the ciphertext 91a413f0b000245c02b7a74e24ab2b0b the IV usefulstringhaha and the key idehcitinptevent.   
We need to decrypt the text using AES CBC decryption. I'll use pycrypto   

```python 
from Crypto.Cipher import AES
from binascii import unhexlify

ciphertext = unhexlify('91a413f0b000245c02b7a74e24ab2b0b')
IV = 'usefulstringhaha'
key = 'idehcitinptevent'

aes = AES.new(key.encode('utf-8'), AES.MODE_CBC,IV.encode('utf-8'))
enc = aes.decrypt(ciphertext)

print(enc)

print(enc[:-6].decode('utf-8'))
```  

The decrypted part is : 3812YsUKLd 

Now we have b5xDDRmj 3812YsUKLd we need to use them. I tired to think about what we can do but there is nothing. 

**All about the hint**  

A hint was released at the second day of the CTF : 

```
Do you want the flag? I put it in my Bin using a really strong password
``` 
The strong password is the one that we decrypted using AES CBC. Bin is a reference for pastbin.  

Let's open the pastbin file and use the password 3812YsUKLd 

``` 
http://pastebin.com/b5xDDRmj
```  
  
We found our flag  


## Flag

```
IDEH{y0u_kn0w_h0w_t0_051nt}
```
