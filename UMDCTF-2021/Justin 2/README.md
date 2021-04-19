# Challenge Name: Justin 2 





![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-OSINT-blueviolet.svg)   
![value](https://img.shields.io/badge/value-250-blue.svg)  
![score](https://img.shields.io/badge/score-5/10-ff69b4.svg)

## Description

My friend is in danger and this was the only picture he could send me. Can you find the name of the street he is on? ex. UMDCTF-{Memory_Lane}

https://drive.google.com/drive/folders/1nfFmXuEMRuCOY6BvAAox1AWQPSCqgIhn?usp=sharing


## Detailed solution

Starting by looking at the picture from google drive link 

![](image.PNG)

We can see a Russian language text here 

![image](https://user-images.githubusercontent.com/72421091/115167481-4b67ab80-a0a7-11eb-9457-ee9506788664.png)

жилфонд and it means housing stock

We have also a car plate 

![image](https://user-images.githubusercontent.com/72421091/115167553-9da8cc80-a0a7-11eb-9641-a43b0315db12.png)

I start searching about russian car plate 

https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Russia
https://www.skoda-storyboard.com/en/models/deciphering-number-plates-russia/

**Plate Format**  

The current format uses a letter followed by 3 digits and two more letters. To improve legibility of the numbers for Russian cars abroad, only a small subset of Cyrillic characters that look like Latin characters are used (12 letters: А, В, Е, К, М, Н, О, Р, С, Т, У, Х). 
Finally, the region number (77, 97, 99, 177, 197, 199, 777, and 799 for Moscow, 78, 98, 178, and 198 for Saint Petersburg, etc.) and the international code RUS are included, as well as the national flag (the flag was not used on some of the earliest plates of this format (about 1993–1994)). 

![image](https://user-images.githubusercontent.com/72421091/115167890-9b933d80-a0a8-11eb-8a39-7b404b32f31d.png)

The code of the region is 154 : Novosibirsk Oblast 

**жилфонд**

Start searching for жилфонд новосибирск област using yandex.ru maps 

The first place has a buildig that have the same strcture with the building from our image 

https://yandex.ru/maps/org/zhilfond/1105706703/gallery/?display-text=%D0%B6%D0%B8%D0%BB%D1%84%D0%BE%D0%BD%D0%B4%20%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82&ll=82.945279%2C55.039647&mode=search&noreask=1&photos%5Bbusiness%5D=1105706703&photos%5Bid%5D=urn%3Ayandex%3Asprav%3Aphoto%3A4392922-2a000001775e11219109ee4baa188fae5c7b&sll=82.945279%2C55.039647&sspn=0.180588%2C0.062501&tab=gallery&text=%D0%B6%D0%B8%D0%BB%D1%84%D0%BE%D0%BD%D0%B4%20%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82&z=13

![image](https://user-images.githubusercontent.com/72421091/115169507-b320f500-a0ad-11eb-8c5d-057937830457.png)

I checked the street view around that place and i found the building at улица Фрунзе, 12 Новосибирск, Россия, 630099

https://yandex.ru/maps/65/novosibirsk/?ll=82.926940%2C55.036946&mode=whatshere&panorama%5Bdirection%5D=5.984988%2C14.308090&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=82.926752%2C55.036758&panorama%5Bspan%5D=118.461500%2C60.000000&whatshere%5Bpoint%5D=82.927069%2C55.036933&whatshere%5Bzoom%5D=17.5&z=17


![2021-04-19_01h34_04](https://user-images.githubusercontent.com/72421091/115170148-781fc100-a0af-11eb-9778-8303f92664a0.png)

Street name : Каменская улица 

I Checked google maps to get the english version 

![2021-04-19_01h42_23](https://user-images.githubusercontent.com/72421091/115170772-fa5cb500-a0b0-11eb-8b98-287eae062c6c.png)


Street : Ulitsa Kamenskaya






## Flag

```
UMDCTF-{Ulitsa_Kamenskaya}
```
