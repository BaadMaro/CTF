# Challenge Name: Justin 3





![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-OSINT-blueviolet.svg)   
![value](https://img.shields.io/badge/value-300-blue.svg)  
![score](https://img.shields.io/badge/score-6/10-ff69b4.svg)

## Description

Justin only gave us this camera's live feed and said "Hey guys look! I'm on TV!" Can you find the name of the street he's on?

format: UMDCTF-{Memory_Lane}

we do not own any IP found besides the one listed below

curl http://chals5.umdctf.io:8000


## Detailed solution

Starting by checking the callenge link http://chals5.umdctf.io:8000  

It's a camera feed 

![screenshot_1618685693766](https://user-images.githubusercontent.com/72421091/115174029-0009c900-a0b8-11eb-9e5a-203c2700ca87.jpg)  

Let's check the page source 
  
```html
<!doctype html>

<html lang="en">

<head>
    
    <link rel= "stylesheet" type= "text/css" href= "/static/main.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
    
    <meta charset="utf-8">
    <title>Cam Feed</title>
</head>
<body>
    <h1>Cam Feed</h1>

</body>

<div class='centered-wrapper'>
		<iframe width="667" height="401" src="http://136.169.226.46/1589793911/embed.html?token=4b3a553415b241089f9d8206c78ef975" title="Cam Feed" frameborder="0" allowfullscreen align="center"></iframe>
</div>
``` 

We can see the IP adresse : 136.169.226.46

Let's search for some details about the IP adresse 

Using https://www.proxydocker.com/en/iplookup/136.169.226.86 i found that 136.169.226.86 is an IPv4 address owned by ufanet.ru flag OJSC Ufanet and located in Russia ip detail Russia (RU) , (Ufa , Bashkortostan Republic ). The timezone of this region is Asia/Yekaterinburg.

![image](https://user-images.githubusercontent.com/72421091/115174493-df8e3e80-a0b8-11eb-85d9-46d95bb82306.png)

Back to our cam feed we can see some text like **советская** 

I started searching at ufa Bashkortostan using советская and see the bus stops 

At Pushkina Street Советская площадь, i found the bus stop from the camera feed 

https://yandex.eu/maps/172/ufa/stops/stop__9905665/?ll=55.947357%2C54.721946&panorama%5Bdirection%5D=308.634148%2C9.000000&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=55.946904%2C54.721624&panorama%5Bspan%5D=118.461500%2C60.000000&z=18

![2021-04-19_02h51_11](https://user-images.githubusercontent.com/72421091/115175388-668fe680-a0ba-11eb-88ac-97aa99b5ec57.png)

I checked google maps to get the english version 

![2021-04-19_03h03_09](https://user-images.githubusercontent.com/72421091/115176067-d357b080-a0bb-11eb-9567-5fa073ec74be.png)

Street name : Ulitsa Pushkina 

## Flag

```
UMDCTF-{Ulitsa_Pushkina}
```









