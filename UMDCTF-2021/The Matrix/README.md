# Challenge Name: The Matrix





![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg)  
![score](https://img.shields.io/badge/score-3/10-ff69b4.svg)

## Description

Oh no! It looks like the robots have taken over! Infilitrate their site and save the world! But beware, they only allow one of them to access it.

curl http://chals5.umdctf.io:4000

## Detailed solution

Starting by opening challenge link http://chals5.umdctf.io:4000  

![image](https://user-images.githubusercontent.com/72421091/115163701-23be1680-a09a-11eb-8a17-189d145f5d7a.png)

Let's check the page source view-source:http://chals5.umdctf.io:4000/ 
```html
<!doctype html>

<html lang="en">

<head>
    
    <link rel= "stylesheet" type= "text/css" href= "/static/main.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
    
    <meta charset="utf-8">
    <title>Enter the Matrix</title>
</head>
<body>
    <h1>The Matrix</h1>

    <nav id="nav" class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/the-matrix">The Matrix</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/about">About</a>
      </li>
    </ul>
  </div>
</nav>
</body>

<div class='centered-wrapper'>
    <a href="/the-matrix" class='button centered'>Enter the matrix!</a>
</div>
 ```
 
We have 3 pages ```/Home```, ```/the-matrix``` and ```about```. ```/about``` has only some text that explain the matrix 

Let's check ```/the-matrix```

![image](https://user-images.githubusercontent.com/72421091/115163786-962ef680-a09a-11eb-9d52-21832470592e.png)

We need to to change the User-agent to have a Robot identity. I tried using **Robot**  
  
```bash
curl 'http://chals5.umdctf.io:4000/the-matrix' \
  -H 'Connection: keep-alive' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Robot' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Referer: http://chals5.umdctf.io:4000/' \
  -H 'Accept-Language: en-US,en;q=0.9,ar;q=0.8,fr;q=0.7' \
  --compressed \
  --insecure
```  

Output 

```html
<!doctype html>

<html lang="en">

<head>

    <link rel= "stylesheet" type= "text/css" href= "/static/main.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

    <meta charset="utf-8">
    <title>Enter the Matrix</title>
</head>
<body>
    <h1>The Matrix</h1>

    <nav id="nav" class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/the-matrix">The Matrix</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/about">About</a>
      </li>
    </ul>
  </div>
</nav>
</body>

<h2>Greetings Fellow Robot Overlord</h2>
<p>UMDCTF-{r0b0t_r3b3ll!0n}</p>
 ``` 
 
 
## Flag

```
UMDCTF-{r0b0t_r3b3ll!0n}
```
