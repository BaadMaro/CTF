
# Challenge Name: Robots




![date](https://img.shields.io/badge/date-11.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![score](https://img.shields.io/badge/score-100-blue.svg)




## Detailed solution

Starting by opening challenge link http://34.69.61.54:5247/ 

![image](https://user-images.githubusercontent.com/72421091/114392728-b0437300-9b88-11eb-8c8e-00749c1ae4d8.png)

Let's check page source 

```html
<!-- templates/index.html -->
<html>
  <head>
    <title>Robots Are Taking Over</title>
  </head>
  <body style="background-color:black;">
    <center>
        <h1 style="color:white">Robots are Taking Over</h1>
        <img src="/static/img/robots.jpeg">

        <p style="border:2px solid white; color:white">
            You need to hide. They have become smarter than us.</p>
        <br>

        <p style=color:black">
          flag.txt</p>
    </center>
  </body>
</html>
```
The challenge mentien robots so let's check the robots.txt file http://34.69.61.54:5247/robots.txt 

We found an interseting path 

```
Allow: /flag/UlN7UjBib3RzX2FyM19iNGR9
```

If we try the check the file, we got not found. The filename is probably a base64 encoded string  

Decoding ```UlN7UjBib3RzX2FyM19iNGR9``` with base64 and we got our flag 


## Flag

```
RS{R0bots_ar3_b4d}
```
