# Challenge Name: Acoustic Phonetics


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-20-blue.svg)  


## Description

Created By **sicmundos**

We just found out about some aliens visiting our planet, and they sent us this audio file.

Can you help us get some information from it?

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/CpW2TKKYax10Tj8fV9xIicRi7yEmOAuL0CScDC9O.zip)

## Detailed solution

After extracting the attachement file, we found a WAV file that has some random noises while playing it  

Let's check the spectogram using Audacity

![image](https://user-images.githubusercontent.com/72421091/156954583-8ec0df93-e77b-4a6c-b194-24d707c50d38.png)

We found the flag  

![image](https://user-images.githubusercontent.com/72421091/156954652-656e53a1-da25-407b-a52b-ef6a37db652f.png)

## Flag

```
CRISIS{5A6rOHgy8}
```
