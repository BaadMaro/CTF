# Challenge Name: Beep


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg)  


## Description

Can you see the sound? 

[audiocheck.net_dtmf_1486_4125_1456.wav](audiocheck.net_dtmf_1486_4125_1456.wav)

Note: The blank between beeps is an underscore.

**Author**: kw4ntum

## Detailed solution 

We have a WAV audio file 

![image](https://user-images.githubusercontent.com/72421091/221616845-84f05799-54bd-4037-a478-95ab3f28feb5.png)

After listen to it, we can hear some buttons sound  probably from an old phone 

It's DTMF 

```
Dual-tone multi-frequency signaling (DTMF) is a telecommunication signaling system using the voice-frequency band over telephone lines between telephone equipment and other communications devices and switching centers.
```
For each key we have a frequency range  

![image](https://user-images.githubusercontent.com/72421091/157148524-dd706b85-d122-411d-848c-91d9ec6edf79.png)

Here is the sound for 1 : https://upload.wikimedia.org/wikipedia/commons/b/bf/Dtmf1.ogg

We can use a decoder to detect each key using sound clips frenquencies https://unframework.github.io/dtmf-detect/#/ 

![image](https://user-images.githubusercontent.com/72421091/221617370-e9329e14-788c-46ae-97b0-37b5e4abe08e.png)

We have a blank between each 4 beeps. We need to add and underscore between each 4 numbers

## Flag

```
IDEH{1486_4125_1456}
```
