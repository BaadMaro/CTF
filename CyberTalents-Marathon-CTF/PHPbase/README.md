
# Challenge Name: PHPbase


![date](https://img.shields.io/badge/date-14.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Secure%20coding-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)



## Detailed solution

Start by opening the challenge link http://3.122.227.44:3333/ 

![image](https://user-images.githubusercontent.com/72421091/113357921-b9d50b80-933c-11eb-8757-f11603762466.png)
  
We have a code review system we can see the source code of some pages and we have a submit button.  

Checking files 
  
```
SRC/ABOUT
SRC/SERVICES
SRC/INDEX.PHP
SRC/HOME
SRC/CONTACT 
``` 
At Index.php we can see a php code 

```php
        <?php
          $file = $_GET["file"];
          if(preg_match("/^\s*\/|^\s*http:\/\/|^.*?\.\..*?$/", $file)){echo "<center><h3>HOME</h3></center>";}
          if(preg_match("/^\s*\/|^\s*php:\/\/|^.*?\.\..*?$/", $file)){echo "<center><h3>HOME</h3></center>";}
          if(!empty($file)){
            if(!preg_match("/^\s*\/|^\s*file:\/\/|^.*?\.\..*?$/", $file)){
              $page =  file_get_contents($file);
              if($page){
                echo $page;
              }else{
                echo "<center><h3>HOME</h3></center>";
              }

            }
          }else {
            echo file_get_contents("home");
          }
          ?> 
          
``` 

The code has a GET parametre to read files and some protection for lfi/rfi that detect http and php in the parametre get file.   
  
```php
if(preg_match("/^\s*\/|^\s*http:\/\/|^.*?\.\..*?$/", $file)){echo "<center><h3>HOME</h3></center>";}
if(preg_match("/^\s*\/|^\s*php:\/\/|^.*?\.\..*?$/", $file)){echo "<center><h3>HOME</h3></center>";}
```
As the challenge tell us to fix a vulnerability, let's start by submiting the actual code  

![image](https://user-images.githubusercontent.com/72421091/113358426-afffd800-933d-11eb-95de-c1a5a12da809.png)

So we have a testing system, probably testing some php vulnerabilities. Let's open the console  

![image](https://user-images.githubusercontent.com/72421091/113358614-079e4380-933e-11eb-90ea-474b1749fb12.png)

We found some tests and one of them failed, we notice that they used the framework **Pytest**  

Looking at the failed test  

```
@pytest.mark.timeout(5)
    def test_vulnerable_1():
    	r = requests.get('http://127.0.0.1/?file=php://filter/convert.base64-encode/resource=/etc/passwd')
>   	assert "cm9vdDp4OjA6MD" not in r.text
E    assert 'cm9vdDp4OjA6MD' not in '<!DOCTYPE h...n\n</html>\n'
E      'cm9vdDp4OjA6MD' is contained here:
E        <!DOCTYPE html>
E        <html lang="en">
E        
E        <head>
E        
E          <meta charset="utf-8">...
E      
E      ...Full output truncated (54 lines hidden), use '-vv' to show

test_challenge.py:27: AssertionError
```
php://filter/convert.base64-encode/resource=/etc/passwd has trigger a LFI without failure because that data passed was in base64 and the output in base 64 cm9vdDp4OjA6MD which is ```root:x:0:0``` so the passwd file has been leaked.    

So our code is vulnerable to LFI using php warpper  

**Fix vulnerability**  

let's fix the vulnerability by only allowing the files that we want to be readed. Let's edit the index.php file and submit the new code    
  
```php
$file = $_GET["file"];
$validValues = array('contact', 'services','about', 'home');          
if (!in_array($file, $validValues, true)) {die("invalid value");}
``` 
![image](https://user-images.githubusercontent.com/72421091/113359620-0ff77e00-9340-11eb-9813-9eb9fe30dc28.png)

## Flag

```
FLAG{PHP_Wr@per$_@Re_ri$ky_som3times}
```
