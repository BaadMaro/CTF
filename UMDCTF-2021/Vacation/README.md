# Challenge Name: Vacation





![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-OSINT-blueviolet.svg)   
![value](https://img.shields.io/badge/value-250-blue.svg)  
![score](https://img.shields.io/badge/score-5/10-ff69b4.svg)

## Description

My mom told me she went to this amazing brewing company in the Carribbean and when I asked her the name of the place, she sent me a picture of her ship. Can you help me find the name of this brewing company?

Flag format: UMDCTF-{City_Companyname}

Note: Companyname = first part of the company name

https://drive.google.com/drive/folders/14eh2f13z32Uf7WFVNHWqHGnXE0P8y8G-?usp=sharing

## Detailed solution

Starting by looking at the picture from google drive link

![](cruise_ship.PNG)  

We can see the Freedom of the Seas a cruise ship operated by Royal Caribbean International. 

https://www.royalcaribbean.com/cruise-ships/freedom-of-the-seas

Checking article https://www.cruisecritic.com/news/5163/ 

Royal Caribbean’s recently-revitalized Freedom of the Seas has returned to San Juan, Puerto Rico, where it operates cruises to the Southern Caribbean.  

So our place is in the Southern Caribbean. I notice the rum therapy place so i searched for ```rum therapy Southern Caribbean``` and check google images 

I found the place "Rum Therapy Bar and Treatment Center" at Castries, St. Lucia

![image](https://user-images.githubusercontent.com/72421091/115172672-43166d00-a0b5-11eb-8598-92fb708317a9.png)  

Search around for a brewing company, i found "Antillia Brewing Company Bar" which is close to the first bar 

![2021-04-19_02h23_09](https://user-images.githubusercontent.com/72421091/115173199-48c08280-a0b6-11eb-963f-d5d28c5cdf89.png)

Flag format: UMDCTF-{City_Companyname}  

- City : Castries 
- Companyname : Antillia

## Flag

```
UMDCTF-{Castries_Antillia}
```

