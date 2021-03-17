
# Challenge Name: inspect_it



![date](https://img.shields.io/badge/date-06.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![web category](https://img.shields.io/badge/category-web-lightgrey.svg)
![score](https://img.shields.io/badge/score-25-blue.svg)




## Detailed solution
It's was an easy introduction to web exploitation, the idea is to search about something hiding in the challenge website. 

The challenge is talking about inspect so we need to inspect pages to look for hidden data. 

We start inspecting available pages/files, in the main page we found the first part : 

```
IDEH{1nspecT_firST_and
```

The css/main.css has the second part : 
  
```
_cSS_c0me_next
```  
And The js/preloader.js has the third part : 

```
_js_c0mes_4t_THE_END}
```  

Let's group them to get our flag.   

## Flag

```
IDEH{1nspecT_firST_and_cSS_c0me_next_js_c0mes_4t_THE_END}
```
