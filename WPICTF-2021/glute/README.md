# Challenge Name: glute

![date](https://img.shields.io/badge/date-24.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg)  


## Description

I swear I didn't realize what I was naming it until I submitted the challenge


[glute.png](glute.png)

## Detailed solution

Checking strings in the image i found a PDF string ```%PDF-1.7``` which is the version of a PDF file

Let's run **binwalk** to check for embedded files  

```
binwalk glute.png                                                                                                                 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 699 x 699, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
285674        0x45BEA         PDF document, version: "1.7"
286201        0x45DF9         Zlib compressed data, default compression
288793        0x46819         JPEG image data, JFIF standard 1.01
288823        0x46837         TIFF image data, big-endian, offset of first image directory: 8
309081        0x4B759         Zlib compressed data, default compression
309501        0x4B8FD         Zlib compressed data, default compression
324160        0x4F240         Zlib compressed data, default compression
324474        0x4F37A         Zlib compressed data, default compression
342030        0x5380E         Zlib compressed data, default compression
```  

Let's extract all files 

```
binwalk -e --dd='.*' glute.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 699 x 699, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
285674        0x45BEA         PDF document, version: "1.7"
286201        0x45DF9         Zlib compressed data, default compression
288793        0x46819         JPEG image data, JFIF standard 1.01
288823        0x46837         TIFF image data, big-endian, offset of first image directory: 8
309081        0x4B759         Zlib compressed data, default compression
309501        0x4B8FD         Zlib compressed data, default compression
324160        0x4F240         Zlib compressed data, default compression
324474        0x4F37A         Zlib compressed data, default compression
342030        0x5380E         Zlib compressed data, default compression
```

```
file *
  
0:          PNG image data, 699 x 699, 8-bit/color RGBA, non-interlaced
4B8FD:      TrueType Font data, 14 tables, 1st "OS/2", 46 names, Macintosh, \251 2018 Microsoft Corporation. All Rights Reserved.Comic Sans MSRegularMicrosoft Comic SansVer
4B8FD.zlib: zlib compressed data
4B759:      ASCII text
4B759.zlib: zlib compressed data
4F37A:      TrueType Font data, 14 tables, 1st "OS/2", 50 names, Unicode, \251 2018 Microsoft Corporation. All Rights Reserved.
4F37A.zlib: zlib compressed data
4F240:      ASCII text
4F240.zlib: zlib compressed data
29:         locale data table
29.zlib:    zlib compressed data
45BEA:      PDF document, version 1.7 (password protected)
45DF9:      ASCII text, with CRLF line terminators
45DF9.zlib: zlib compressed data
5380E:      data
5380E.zlib: zlib compressed data
46819:      JPEG image data, JFIF standard 1.01, resolution (DPI), density 120x120, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=5], baseline, precision 8, 599x504, components 3
46837:      TIFF image data, big-endian, direntries=5
```

We can see our flag in the pdf file 45BEA 

## Flag

```
WPI{P0lyGlOtz_R_koo1}
```
