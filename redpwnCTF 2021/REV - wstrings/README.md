# Challenge Name: wstrings


![date](https://img.shields.io/badge/date-10.07.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![reverse category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![value](https://img.shields.io/badge/value-102-blue.svg)  


## Description

Some strings are wider than normal...

Author : NotDeGhost

[wstrings](wstrings)

## Detailed solution

As the description mention let's start by checking file strings

At offest 0x930 we can see our flag
  
```bash
~# hexdump -n 140 -s 0x930 -C wstrings
00000930  01 00 02 00 00 00 00 00  66 00 00 00 6c 00 00 00  |........f...l...|
00000940  61 00 00 00 67 00 00 00  7b 00 00 00 6e 00 00 00  |a...g...{...n...|
00000950  30 00 00 00 74 00 00 00  5f 00 00 00 61 00 00 00  |0...t..._...a...|
00000960  6c 00 00 00 31 00 00 00  5f 00 00 00 73 00 00 00  |l...1..._...s...|
00000970  74 00 00 00 72 00 00 00  31 00 00 00 6e 00 00 00  |t...r...1...n...|
00000980  67 00 00 00 73 00 00 00  5f 00 00 00 61 00 00 00  |g...s..._...a...|
00000990  72 00 00 00 33 00 00 00  5f 00 00 00 73 00 00 00  |r...3..._...s...|
000009a0  6b 00 00 00 31 00 00 00  6e 00 00 00 6e 00 00 00  |k...1...n...n...|
000009b0  79 00 00 00 7d 00 00 00  00 00 00 00              |y...}.......|
000009bc
```


## Flag

```
flag{n0t_al1_str1ngs_ar3_sk1nny}
```
