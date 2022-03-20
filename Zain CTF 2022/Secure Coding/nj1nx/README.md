# Challenge Name: nj1nx

![date](https://img.shields.io/badge/date-19.03.2021-brightgreen.svg)  
![category](https://img.shields.io/badge/category-Secure%20coding-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Basic-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

[http://52.53.215.65:3333/](http://52.53.215.65:3333/)

This is the strongest configuration file, can you break it ?

## Notes

The website show us a nginx conf file called vulnerable.conf to review it 

http://52.53.215.65:3333/static/challenge_files/src/vulnerable.conf

```
server {
    listen       80;
    server_name  localhost;

    location / {
        root   /usr/share/nginx/html;
        index  index.html;
    }

    location /static {
        proxy_pass http://127.0.0.1/images/;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

The location /static dosen't end with / which lead to a path traversal vulnerability in Nginx 

Details here : https://www.acunetix.com/vulnerabilities/web/path-traversal-via-misconfigured-nginx-alias/

To fix that we need to add / to /static

```
location /static/ {
        proxy_pass http://127.0.0.1/images/;
}
```
## Flag

Unfortunately i wasn't able to test the solution because the server dies many times and return 500 when i submit 
