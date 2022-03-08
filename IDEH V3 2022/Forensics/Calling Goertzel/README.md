# Challenge Name: Calling Goertzel


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-10-blue.svg)  

## Description

Created By **sicmundos**

Some weird number keeps calling me, can you extract it?

> Dont forget to wrap what you have found inside CRISIS{}

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/FEb0joyUynFtqOH4XDdDMqr03FIoxVFQrr7ecdCB.zip)

## Detailed solution

We have a WAV audio file 

```shell
┌──(kali㉿kali)-[~]
└─$ file file.wav                                                          
file.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 8 bit, mono 8000 Hz
```
After listen to it, we can hear some buttons sound  probably from an old phone 

It's DTMF 

```
Dual-tone multi-frequency signaling (DTMF) is a telecommunication signaling system using the voice-frequency band over telephone lines between telephone equipment and other communications devices and switching centers.
```
For each key we have a frequency range  

![image](https://user-images.githubusercontent.com/72421091/157148524-dd706b85-d122-411d-848c-91d9ec6edf79.png)

Here is the sound for 1 : https://upload.wikimedia.org/wikipedia/commons/b/bf/Dtmf1.ogg

We can use a decoder to detect each key using sound clips frenquencies https://unframework.github.io/dtmf-detect/#/

![Pasted image 20220306031943](https://user-images.githubusercontent.com/72421091/157148966-89732da7-8826-4c83-b3d8-4da730063c22.png)


## Flag

```
CRISIS{6058942233}
```
