
# Challenge Name: Sessions




![date](https://img.shields.io/badge/date-11.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![score](https://img.shields.io/badge/score-100-blue.svg)




## Detailed solution

Starting by opening challenge link http://34.69.61.54:4777 

We have a login page http://34.69.61.54:4777/login  

![image](https://user-images.githubusercontent.com/72421091/114394538-d79b3f80-9b8a-11eb-962c-c158c8611256.png)

Let's check the page source 

```
<html>
<head>
  <title>Iroh - Login</title>
  <!--#remove comment later: login iroh:iroh-->
</head>

<body style="background-color:orange;">
<h2> Login </h2>
<form action="" method="post">
       <input type="text" placeholder="Username" name="username" value="">
        <input type="password" placeholder="Password" name="password" value="">
       <input class="btn btn-default" type="submit" value="Login">
     </form>
     

</body>

</html>
```
As we can see we have a comment tag with the login credentials **iroh:iroh** 

Let's try to login with the iroh:iroh 

Checking the request headers after login, we can see our session cookie 

```
Cookie: sessiontoken=UlN7MG5seV9PbmVfczNzc2lvbl90b2szbn0=
```
Decodinge the sessiontoken with base64 and we got our flag  

## Flag

```
RS{0nly_One_s3ssion_tok3n}
```
