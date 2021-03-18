
# Challenge Name: A Pessimistic Life


![date](https://img.shields.io/badge/date-10.03.2021-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg) 
![stego category](https://img.shields.io/badge/category-stego-lightgrey.svg)
![score](https://img.shields.io/badge/score-200-blue.svg)


## Attached files

- [APessimisticLife.jpg](APessimisticLife.jpg)
- [Depression.txt](Depression.txt)





## Detailed solution
The challenge description was refering to **depression** so i tried to use the word to extract with steghide :  
first use setghide info to check :
```bash
steghide info APessimisticLife.jpg
"APessimisticLife.jpg":
  format: jpeg
  capacity: 22.8 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:  
  embedded file "Depression.txt":
    size: 271.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```
and second extracting data :

```bash
steghide extract -sf APessimisticLife.jpg -p depression
wrote extracted data to "Depression.txt".
```
**Bonus :** 
  
I tried to continue in solving the probleme later after CTF ended, and i tried stegseek to crack the passphrase using the wordlist rockyou
```bash
stegseek APessimisticLife.jpg rockyou.txt
StegSeek version 0.5
Progress: 0.42% (582363 bytes)

[i] --> Found passphrase: "depression"
[i] Original filename: "Depression.txt"
[i] Extracting to "APessimisticLife.jpg.out"
```
Stegseek is a lightning fast steghide cracker that can be used to extract hidden data from files. 
It can also be used to detect and extract any unencrypted (meta) data from a steghide image. This exploits the fact that the random number generator used in steghide only has 2^32 possible seeds, which can be bruteforced in a matter of minutes.  

![](https://github.com/RickdeJager/stegseek/raw/master/.demo/seed.gif)

**Depression.txt**  
  
the text file has some weird code

```
⎕IO ← 0
      A ← 'abcdefghijklmnopqrstuvwxy_1234567890'
      I ← (6 6 ⍴ 1 + ⍳6)+⍉(10 × 6 6 ⍴ 1 + ⍳6)
      S ← 6 6 ⍴ A
      E ← {⌈/⌈/ (~⍵ ⍳ S) × I}
      E¨flag
23 14 15 22 52 33 22 52 23 41 52 42 22 23 41 52 15 41 33 42 15 36 23 13
```
I tried to google some of these lines and i find that the code corresponds to **APL**, an array-oriented programming language.  
  
https://en.wikipedia.org/wiki/APL_(programming_language)  
https://en.wikipedia.org/wiki/APL_syntax_and_symbols 

I searched for how the code work and instruction syntax, i found this cool website : 

https://tryapl.org/ 

I Started to play with some instrcutions and start digging with our code. I found that ⎕ is used to print data, so i used it to analyze our code : 
```
      A ← 'abcdefghijklmnopqrstuvwxy_1234567890'
      ⎕ ← A
abcdefghijklmnopqrstuvwxy_1234567890
      I ← (6 6 ⍴ 1 + ⍳6)+⍉(10 × 6 6 ⍴ 1 + ⍳6)
      ⎕ ← I
22 23 24 25 26 27
32 33 34 35 36 37
42 43 44 45 46 47
52 53 54 55 56 57
62 63 64 65 66 67
72 73 74 75 76 77
      S ← 6 6 ⍴ A
      ⎕ ← S
abcdef
ghijkl
mnopqr
stuvwx
y_1234
567890
      E ← {⌈/⌈/ (~⍵ ⍳ S) × I}
      ⎕ ← E
┌┴┐             
⊢ {⌈/⌈/(~⍵⍳S)×I}
```
Start analyzing :
- 'abcdefghijklmnopqrstuvwxy_1234567890' the alphebets used
- I : it's a 6x6 matrix and it start with 6 + 10 + 6 = 22 for the first number
- S : store the alphabet A in a 6x6 matrix
- E : ⌈/22 44 -> 44 ⌈ it give the maximun between the two. i didn't find a solution to execute and print E
- looking at the code the last data possibly what E printed : 23 14 15 22 52 33 22 52 23 41 52 42 22 23 41 52 15 41 33 42 15 36 23 13  
    we can see a 2 digits numbers with 1min and 6max -> refering to 6x6 matrix too
- we know our flag should start by ideh so we need to find the relation betwen S, I and our last data 

looking at code printing resultats we see that we have 6x6 matrix, we start with the matrix S :

```
  123456
1 abcdef
2 ghijkl
3 mnopqr
4 stuvwx
5 y_1234
6 567890
```

Our first number is 23 which it should be an i as we know. i have the indice 2-3 which correspend to i in the matrix S so we find our solution.  
We need to convert those numbers using the position of the digits to find the caractere. First digit rows, second columns

23 14 15 22 52 33 22 52 23 41 52 42 22 23 41 52 15 41 33 42 15 36 23 13

```
23 = i
14 = d
15 = e
22 = h
...
```

## Flag

```
ideh_oh_is_this_esoteric
```
