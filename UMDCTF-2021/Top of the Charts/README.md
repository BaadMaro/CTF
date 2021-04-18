# Challenge Name: Top of the Charts





![date](https://img.shields.io/badge/date-17.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-250-blue.svg)  
![score](https://img.shields.io/badge/score-/10-ff69b4.svg)

## Description

I found this site which seems to boast about itself too much. It claims to be above everything else but I'm not so sure. I think the success has gone to its head.

curl http://chals5.umdctf.io:4003

## Detailed solution

Starting by opening the challenge link http://chals5.umdctf.io:4003

![image](https://user-images.githubusercontent.com/72421091/115165229-71d41980-a09c-11eb-922f-66cb7f0030aa.png)  

Let's check the page source view-source:http://chals5.umdctf.io:4003/  

```html
<!doctype html>

<html lang="en">

<head>
    
    <link rel= "stylesheet" type= "text/css" href= "/static/main.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
    
    <meta charset="utf-8">
    <title>Top of the Charts</title>
</head>
<body>
    <h1>Top of the Charts</h1>

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
    </ul>
  </div>
</nav>
</body>

<h3>Welcome to the Top of the Charts!</h3>
<p>Here at top of the charts, we are the ceiling of the world! Nothing is above us!</p>
```

The Home page has only some text, and we don't have any other information 

I used **nikto** to get more details  
  
```bash
nikto -h http://chals5.umdctf.io:4003

- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          104.236.193.108
+ Target Hostname:    chals5.umdctf.io
+ Target Port:        4003
+ Start Time:         2021-04-17 15:58:03 (GMT0)
---------------------------------------------------------------------------
+ Server: Werkzeug/1.0.1 Python/3.5.2
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: OPTIONS, GET, HEAD
```

We can see that we have the HTTP Methode **HEAD **  

Let's use the http method HEAD and check the output  

```bash
curl -I 'http://chals5.umdctf.io:4003/'

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
flag: UMDCTF-{h3@d1ng_t0w@rd5_th3_l1ght}
Content-Length: 0
Server: Werkzeug/1.0.1 Python/3.5.2
Date: Sun, 18 Apr 2021 23:25:35 GMT
``` 

## Flag

```
UMDCTF-{h3@d1ng_t0w@rd5_th3_l1ght}
```

