# Challenge Name: Fish

![date](https://img.shields.io/badge/date-19.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-OISNT-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)

## Description

Can you find the following?

1. What's the name of the artist? (firstname_lastname) [note: lowercase letters]

2. In which year did he draw it? (####)

3. Where is that painting located? (latitude_longitude) [note: 3 decimal places]

Flag Format:

flag{firstname_lastname_year_latitude_longitude}

 [https://hubchallenges.s3.eu-west-1.amazonaws.com/OSINT/Fish.png](https://hubchallenges.s3.eu-west-1.amazonaws.com/OSINT/Fish.png)

## Detailed solution

![image](https://user-images.githubusercontent.com/72421091/159143213-75db48be-05fc-476b-acd3-6cfdb1ee246e.png)

Using google search to try to find the original image

I found an article about street art that has the same image

https://streetartnews.net/2014/09/finok-paints-new-new-mural-in-heerlen.html

![image](https://user-images.githubusercontent.com/72421091/159143234-d603f631-35bc-4bc7-bca9-3a57320acd92.png)

Finok was one of the international artists that took part in recently completed Heerlen Murals Project 2014. The young Brazilian artist brought a bit of different flavor to the Dutch city with this colorful piece.

From the article we got the artist name, year and location 

Search for the artist real name using "Finok brazilian artist", i found this link https://www.galleriapatriciaarmocida.com/en/artists/finok 

 **Raphael Sagarra, aka “Finok”**
 
 For the location of the image, i found a website that list all street painating in Heerlen https://streetartheerlen.nl/
 
![image](https://user-images.githubusercontent.com/72421091/159143370-580f648e-5df7-47e6-aa2f-f46323f88358.png)

https://www.google.com/maps/@50.8896195,5.9837931,3a,75y,13.98h,91.47t/data=!3m6!1e1!3m4!1sJE5V1a8I-xN3FrsPpPkN-Q!2e0!7i16384!8i8192

http://www.google.com/maps/dir/?api=1&origin=&destination=50.889749324537,5.9838956594467

Location is : 50.889749324537,5.9838956594467

![image](https://user-images.githubusercontent.com/72421091/159143464-aa3505b6-36a8-4470-8733-27a052c3b546.png)

Flag Format:

flag{firstname_lastname_year_latitude_longitude} [note: lowercase letters] [note: 3 decimal places] 

## Flag

```
flag{raphael_sagarra_2014_50.889_5.983}
```
