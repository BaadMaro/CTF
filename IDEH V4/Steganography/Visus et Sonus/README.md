# Challenge Name: Visus et Sonus


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  


## Description

That noise is really blurry.

[audiocheck.net_spectrotyper.wav](audiocheck.net_spectrotyper.wav)

**Author**: kw4ntum

## Detailed solution

We have a WAV audio file 

![image](https://user-images.githubusercontent.com/72421091/221624376-ffe6619c-5355-4be6-a7bf-77d753d51023.png)

The audio has only noise. If we check the filename, we can see a hint for spectrogram

We can use audacity to check spectrogram for the audio file https://www.audacityteam.org/download/ 

![image](https://user-images.githubusercontent.com/72421091/221625004-f43cd874-66f3-410f-9e55-b4ce1bbbffca.png)


## Flag

```
IDEH{1_c4n_re4d_audi0}
```
