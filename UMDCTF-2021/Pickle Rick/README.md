# Challenge Name: Pickle Rick


![date](https://img.shields.io/badge/date-18.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-250-blue.svg)  
![score](https://img.shields.io/badge/score-5/10-ff69b4.svg)

## Description

You recieve these audio files from someone named Alan Eliasen.

https://drive.google.com/drive/folders/135epDZ18MdIycbBt_Fekbi8hdF-83v6Y?usp=sharing

## Detailed solution

https://futureboy.us/stegano/ made by Alan Eliasen and use steghdie to encode/decode  

We have two wav files ```rickroll.wav``` and ```together-forever-encoded.wav``` 

Checking steghide info on both files, i found that the file ```together-forever-encoded.wav``` has an embedded file and it's not protected 
  
```bash
steghide info together-forever-encoded.wav   
  
"together-forever-encoded.wav":
  format: wave audio, PCM encoding
  capacity: 1.1 MB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "steganopayload318205.txt":
    size: 30.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```  
Let's extract the file  

```
steghide extract -sf together-forever-encoded.wav          

Enter passphrase:
wrote extracted data to "steganopayload318205.txt".
```  
```
cat steganopayload318205.txt

The password is "big_chungus"!  
```  

I used the passowrd to extraxt embedded files form the ```rickroll.wav``` 

```
steghide extract -sf rickroll.wav -p big_chungus

wrote extracted data to "steganopayload318287.txt".
```  

```
cat steganopayload318287.txt

UMDCTF-{n3v3r_g0nna_l3t_y0u_d0wn}
```


## Flag

```
UMDCTF-{n3v3r_g0nna_l3t_y0u_d0wn}
```
