# Challenge Name: inspect-me

![date](https://img.shields.io/badge/date-09.07.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![web category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![value](https://img.shields.io/badge/value-101-blue.svg)  


## Description

See if you can find the flag in the source code!

inspect-me.mc.ax

Author : NotDeGhost


## Detailed solution

Opening the challenge link https://inspect-me.mc.ax/

Checking the page source and we can see the flag in a comment tag view-source:https://inspect-me.mc.ax/
  
```html
<body>
	<br><br><br>
	<h1><marquee><span><u>Van Der Pawn's SITE</u></span></marquee></h1>
	<hr>
  <h2>Welcome to Van Der Pawn's website!</h2>
  <br>
  <br>
	<img src="/const2.gif"/>
  <br>
  <br>
  <h2>important updates!</h2>
  <li>We are working hard to always keep our site as up-to-date and modern as possible!</li>
  <li>TODO: remove flag from HTML comment</li>

  <!-- flag{inspect_me_like_123} -->
  
  <hr>
  <div style="display: flex; justify-content: center">
    <img src="/welcome.gif" height="200px"/>
    <img src="/welcome.gif" height="200px"/>
    <img src="/welcome.gif" height="200px"/>
    <img src="/welcome.gif" height="200px"/>
    <img src="/welcome.gif" height="200px"/>
    <img src="/welcome.gif" height="200px"/>
  </div>

	<hr>

	<br>
	<br>
	<img src="/ie.gif" height="50px/"><img src="/netscape.gif" height="50px/">
	<br>Copyright (c) 2019
</div>

</body>
```

We got our flag

## Flag

```
flag{inspect_me_like_123}  
```
