# Challenge Name: The Magic of the PHP


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-35-blue.svg)  


## Description

Created By **m4rc0s**

I did manage to get the source code of the authentication page but still cannot extract the password it's hashed in md5, I tried all brute-force solution. Can you bypass this system?
```php
<?php
if(isset ($_POST['password'])){
    $password = $_POST['password'];
    if(md5($password) == 0e7b1c8e2327e0881bf7058bd533dd22)
    {
        echo "$FLAG</br>";
    }
    else echo "Incorrect Password </br>";
}
?>
<html>
    Enter your password : </br>
    <form action="" method="POST">
<input type="password" name="password"></input>    
<input type="submit" ></input>
</form>
</html>
```
Website : http://18.168.221.53/

## Detailed solution

The comparison between the md5 of our input and the secret hash use loose comparisons == that has some a known vulnerabilite called type juggling referred to the feature used by PHP for comparaison

More Details : https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf 

![image](https://user-images.githubusercontent.com/72421091/157162373-175402d1-e383-457b-bfcd-b28efc917f6f.png)

To be able to bypass our code we need to find a md5 hash that start with 0e to trick the loose comparisons. They are calleg magic hashes

https://github.com/spaze/hashes/blob/master/md5.md

```
240610708:0e462097431906509019562988736854
```

Now let's use **240610708** 

![image](https://user-images.githubusercontent.com/72421091/157162589-a2389c74-4086-4a7a-9ef5-9b2dcd5c8c24.png)

## Flag

```
CRISIS{Sazs280}
```


