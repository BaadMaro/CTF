# Challenge Name: Email Address

![date](https://img.shields.io/badge/date-19.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-OISNT-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)


## Description

Can a username be enough to find the email address of our target?

Username: c5oylchicrlnofu

Note: Please use the following flag format to submit the answer:

flag{emailaddress}

## Detailed solution

I started by using the username to search for social media accounts using sherlock 

https://github.com/sherlock-project/sherlock


```bash
┌──(kali㉿kali)-[~]
└─$ sherlock c5oylchicrlnofu                                                                                                                 130 ⨯
[*] Checking username c5oylchicrlnofu on:
[+] CapFriendly: https://www.capfriendly.com/users/c5oylchicrlnofu
[+] Chess: https://www.chess.com/member/c5oylchicrlnofu
[+] Coil: https://coil.com/u/c5oylchicrlnofu
[+] Fiverr: https://www.fiverr.com/c5oylchicrlnofu
[+] GitHub: https://www.github.com/c5oylchicrlnofu
[+] Gumroad: https://www.gumroad.com/c5oylchicrlnofu
[+] HackerNews: https://news.ycombinator.com/user?id=c5oylchicrlnofu
[+] LeetCode: https://leetcode.com/c5oylchicrlnofu
[+] Minecraft: https://api.mojang.com/users/profiles/minecraft/c5oylchicrlnofu
[+] Smule: https://www.smule.com/c5oylchicrlnofu
[+] Spotify: https://open.spotify.com/user/c5oylchicrlnofu
[+] TradingView: https://www.tradingview.com/u/c5oylchicrlnofu/
[+] Venmo: https://venmo.com/u/c5oylchicrlnofu
```
As we can we found some accounts, the one that i think it's the way to go is github

https://github.com/c5oylchicrlnofu/

There a repossitory created recently https://github.com/c5oylchicrlnofu/MyFirstRepository/commits/main

We can search for the email using the public data from the api 

https://api.github.com/users/c5oylchicrlnofu/events/public

```json
{
"id": "20641771480",
"type": "PushEvent",
"actor": {
  "id": 97314918,
  "login": "c5oylchicrlnofu",
  "display_login": "c5oylchicrlnofu",
  "gravatar_id": "",
  "url": "https://api.github.com/users/c5oylchicrlnofu",
  "avatar_url": "https://avatars.githubusercontent.com/u/97314918?"
},
"repo": {
  "id": 467599760,
  "name": "c5oylchicrlnofu/MyFirstRepository",
  "url": "https://api.github.com/repos/c5oylchicrlnofu/MyFirstRepository"
},
"payload": {
  "push_id": 9297145752,
  "size": 1,
  "distinct_size": 1,
  "ref": "refs/heads/main",
  "head": "9f15379fa7f92d37c6a5dda62ee9df73367709db",
  "before": "c9afe2ea52f2b78b0c2ac1fb2ebb56fcd5183a21",
  "commits": [
    {
      "sha": "9f15379fa7f92d37c6a5dda62ee9df73367709db",
      "author": {
        "email": "ch05o6wo7ribrlfrldrusp1ke@protonmail.com",
        "name": "c5oylchicrlnofu"
      },
      "message": "Update README.md",
      "distinct": true,
      "url": "https://api.github.com/repos/c5oylchicrlnofu/MyFirstRepository/commits/9f15379fa7f92d37c6a5dda62ee9df73367709db"
    }
  ]
},
"public": true,
"created_at": "2022-03-08T16:54:27Z"
}
```

"email": "ch05o6wo7ribrlfrldrusp1ke@protonmail.com"



## Flag

```
flag{ch05o6wo7ribrlfrldrusp1ke@protonmail.com}
```
