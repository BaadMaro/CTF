# Challenge Name: Fsociety


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-10-blue.svg)  


## Description

Created By **sicmundos**

Fsociety is the name of a hacker group based in Coney Island, New York, led by the mysterious Mr. Robot.

Mr. Robot is another **extension** to the personality of Elliot, Here is the Fsociety's LOGO.

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/HADtiA8RZSnm5yX3T8utArwSyah1hR1Ga5xhBSC0.zip)

## Detailed solution

![challenge](https://user-images.githubusercontent.com/72421091/156955361-945256f2-55e4-4b65-81e0-83229be2cea6.jpg)

We have a jpg image 

```bash
┌──(kali㉿kali)-[~]
└─$ file challenge.jpg
challenge.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1280x839, components 3
```
As nothing visible in the image let's check strings first

```bash
┌──(kali㉿kali)-[~]
└─$ strings challenge.jpg
JFIF
(ICC_PROFILE
mntrRGB XYZ
acsp
        desc
trXYZ


CRISIS{As15tGew63X}
```
At the end of strings output we can see our flag

## Flag

```
CRISIS{As15tGew63X}
```

