# Challenge Name: The Urban Turing Machine


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Crypto-blueviolet.svg)   
![value](https://img.shields.io/badge/value-5-blue.svg) 


## Description

Created By **m4rc0s**

I heard that with a language of 6 symbols, we can do code anything we want. Attempt to get the flag here

```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>---.+++++++++++++++.---------.++++++++++.----------.++++++++++.>+++++++++++++++++++++++.---.------------------.<<++++++++++++++++++++++++++.++++++++++++.>>---.<<---------------.>>+.+++++++++++.<--------------.<----.>>++++++++++++++.
```

## Detailed solution

We can either search for encoding languages that use thoses symboles or use a cipher identifer like https://www.dcode.fr/cipher-identifier 

It's Brainfuck

```
Brain Fuck is not a proper encryption system, but rather a programming language that has been obfuscated. Encoding consists in writing machine code that returns text as output.
```

We can decode it using https://www.dcode.fr/brainfuck-language 

## Flag

```
CRISIS{xf8Dc5doE1}
```
