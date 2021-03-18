
# Challenge Name: QRQR



![date](https://img.shields.io/badge/date-06.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![stego category](https://img.shields.io/badge/category-stego-lightgrey.svg)
![score](https://img.shields.io/badge/score-25-blue.svg)


## Attached files

- [QRQRQRQR.zip](QRQRQRQR.zip)

## Detailed solution
Let's check the file 

```shell
file QRQRQRQR.zip
QRQRQRQR.zip: PNG image data, 305 x 305, 8-bit grayscale, non-interlaced
``` 
It's a png image and not a zip, let's open it as an image  

![QRQRQRQR](https://user-images.githubusercontent.com/72421091/111680057-1c4ce880-8822-11eb-83e6-4dcaa2367569.png)

It's a QR-Code we can use any qr-code reader to decode it. i'll use zbarimg

```shell
zbarimg QRQRQRQR.png
QR-Code:01001001 01000100 01000101 01001000 01111011 01010001 01010010 01011111 01100011 00110000 01000100 01000101 01110011 01011111 00110100 01110010 01000101 01011111 01000101 00110100 01010011 01111001 01011111 01010100 00110000 01011111 01000010 01010010 01000101 00110100 01001011 01111101
```  
We found some binary numbers let's convert them from binary to ascii. I'll use cyberchef.   

We found our flag.  


## Flag

```
IDEH{QR_c0DEs_4rE_E4Sy_T0_BRE4K}
```
