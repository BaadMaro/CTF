# Challenge Name: Obfjustu

![date](https://img.shields.io/badge/date-19.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Web-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)

## Description

http://52.59.254.46:1245/

## Detailed solution

Checking the challnege website http://52.59.254.46:1245/

It has a graphical CLI, we can see the available commads using /help

![Pasted image 20220319031612](https://user-images.githubusercontent.com/72421091/159142863-892da662-b581-41fd-9680-389578818bd2.png)

Let's check the source page : view-source:http://52.59.254.46:1245/ 

```html
<!DOCTYPE html>

<html lang="en" >

<head>

<meta charset="UTF-8">

<title>CodePen - Command Line Website</title>

<link rel='stylesheet' href='[https://fonts.googleapis.com/css?family=Fira+Mono:400,700](https://fonts.googleapis.com/css?family=Fira+Mono:400,700)'><link rel="stylesheet" href="[./style.css](http://52.59.254.46:1245/style.css)">

<script src="[https://cdnjs.cloudflare.com/ajax/libs/prefixfree/1.0.7/prefixfree.min.js](https://cdnjs.cloudflare.com/ajax/libs/prefixfree/1.0.7/prefixfree.min.js)"></script>

  

</head>

<body>

<!-- partial:index.partial.html -->

<div class="stream"></div>

<div class="line editline">

<p class="time"></p>

<p class="name">&gt;</p>

<p contenteditable="true" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" class="information edit"></p>

</div>

<!-- partial -->

<script src='[https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js](https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js)'></script>

<script src='[https://codepen.io/z-/pen/vLNYyg/dcdf9b1e328493afd4bd982ed98266d3.js](https://codepen.io/z-/pen/vLNYyg/dcdf9b1e328493afd4bd982ed98266d3.js)'></script><script src="[./script.js](http://52.59.254.46:1245/script.js)"></script>

  

</body>

</html>
```
The main javascript file is : http://52.59.254.46:1245/script.js

[script.js](script.js)

We have a function called cmd that handle commands cases

```js
   function cmd(command, words, word) {
      switch (word[0]) {
         case "/help":
         case "help":
            for (var i = 0; i < commandlist.length; i++) {
               output = commandlist[i][0] + " : " + commandlist[i][1];
               //console.log(command[i][0]);
               log("Client", output);
            }
            break;
		 case "/gl":
			//window.location.href = "http://koya.io" + (currentpage == "landing" ? "" : "/" + currentpage);
			window.history.pushState(currentpage, 'InpagePage', (currentpage == "landing" ? "/" : "/" + currentpage));
			break;
         case "/clear":
            $(".stream").text("");
            break;
         case "/nav":
            if ($.inArray(word[1], pageindex) >= 0) {
               currentpage = word[1];
               log("Website", "You are now in " + currentpage);
               loadpage($.inArray(word[1], pageindex));
            } else {
               log("Client", "'" + word[1] + "' does not exist.");
            }
            break;
         case "/list":
            $.each(pageindex, function(id, content) {
               log("Client", "> " + content);
            });
            break;
         case "/login":
            if (word.length >= 3) {

var _cs=["\x6a\x53","\x31\x30\x6e","\x66\x75","\x5f\x77","\x30\x6d\x33","\x43\x6c\x69","\x48\x5f\x73","\x7b\x30\x62","\x61\x67","\x33","\x66\x6c","\x31\x74","\x65\x6e\x74","\x73\x63","\x77\x45\x4c","\x4c\x63","\x30\x6d","\x61\x74","\x7d","\x67\x74\x68","\x67\x74","\x63\x61\x6c","\x6c\x6f","\x68","\x6c\x65\x6e","\x6d\x70","\x65","\x61\x72",'\x67\x65\x6f',"\x65\x43\x6f"]; var _xxg0=_cs[10]+_cs[8]+_cs[7]+_cs[2]+_cs[13]+_cs[17]+_cs[1]+_cs[3]+_cs[11]+_cs[6]+_cs[4]+_cs[0]+_cs[18]; function _xxf0(_xxp1, _xxp0){ if (_xxp1[_cs[24]+_cs[19]] !== _xxp0[_cs[24]+_cs[20]+_cs[23]]) { return false; } return _xxp1[_cs[22]+_cs[21]+_cs[29]+_cs[25]+_cs[27]+_cs[26]](_xxp0) === 0; } if (_xxf0(_xxg0,word[2])){ log(_cs[5]+_cs[12],_cs[14]+_cs[15]+_cs[16]+_cs[9]); }               //log("Client", "ER1");
               log("Welcome");
            } else {
               log("Client", "Not enough arguments to log in, you need a USERNAME and a PASSWORD.");
            }
            break;
         default:
            output = "Unrecognised command '" + word[0] + "'.";
            log("Client", output);
      }
   }

```

We can use the devtools console to print variables used in the case "/login"


```js
var _cs=["\x6a\x53","\x31\x30\x6e","\x66\x75","\x5f\x77","\x30\x6d\x33","\x43\x6c\x69","\x48\x5f\x73","\x7b\x30\x62","\x61\x67","\x33","\x66\x6c","\x31\x74","\x65\x6e\x74","\x73\x63","\x77\x45\x4c","\x4c\x63","\x30\x6d","\x61\x74","\x7d","\x67\x74\x68","\x67\x74","\x63\x61\x6c","\x6c\x6f","\x68","\x6c\x65\x6e","\x6d\x70","\x65","\x61\x72",'\x67\x65\x6f',"\x65\x43\x6f"]; 

var _xxg0=_cs[10]+_cs[8]+_cs[7]+_cs[2]+_cs[13]+_cs[17]+_cs[1]+_cs[3]+_cs[11]+_cs[6]+_cs[4]+_cs[0]+_cs[18];
```
**_cs**

```
[
    "jS",
    "10n",
    "fu",
    "_w",
    "0m3",
    "Cli",
    "H_s",
    "{0b",
    "ag",
    "3",
    "fl",
    "1t",
    "ent",
    "sc",
    "wEL",
    "Lc",
    "0m",
    "at",
    "}",
    "gth",
    "gt",
    "cal",
    "lo",
    "h",
    "len",
    "mp",
    "e",
    "ar",
    "geo",
    "eCo"
]
```

console.log(_xxg0)  

flag{0bfuscat10n_w1tH_s0m3jS}  


## Flag

```
flag{0bfuscat10n_w1tH_s0m3jS}  
```
