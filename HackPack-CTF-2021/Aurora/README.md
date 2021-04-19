
# Challenge Name: Aurora



![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![misc category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

Aurora is a marvelous phenomenon caused by the interaction between strong solar wind and magnetosphere around the earth.

Image source: https://science.nasa.gov/flag-shaped-aurora-over-sweden

[Aurora.jpg](Aurora.jpg)

## Detailed solution

Start by checking the image and use strings 
  
```
file Aurora.jpg
Aurora.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 100x100, segment length 16, comment: "flag{6e4ut1fuL_Aur0r4}", baseline, precision 8, 960x641, components 3
```  

```
strings Aurora.jpg

JFIF
flag{6e4ut1fuL_Aur0r4}
Ducky
Adobe
cs4&
1AQ"
!p[nq
tm6)
:~GIu
```
We got our flag

## Flag

```
flag{6e4ut1fuL_Aur0r4}
```
