# Challenge Name: LolSec


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Cryptography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  


## Description

My friend uses SMS language nearly everywhere, even in codes. He sent me this and told me if I could solve this he will introduce me to his fun new programming language. I need some help please

```
HAI 1.2
    VISIBLE "IDEH{too_obvious_nah}"
    I HAS A TH1S ITZ "100"
    I HAS A N3V3R ITZ "010"
    I HAS A KN3W ITZ "011"
    I HAS A L0L ITZ "001"
    BTW FLAG IZ VAR NAME AND APPEND UNDERSCORE
KTHXBYE
```

**Author** : kw4ntum

## Detailed solution

If we search for "HAI 1.2", we will find that it's used in a language called LOLCODE https://github.com/justinmeza/lolcode-spec/blob/master/v1.2/lolcode-spec-v1.2.md 

- HAI 1.2 : The version used which is 1.2
- VISIBLE : to print a message
- I HAS A `variable name` ITZ `value` : to declare a variable with name and value
- BTW [MESSAGE] : to put a message 

You can use a decompiler to play with the language https://www.tutorialspoint.com/execute_lolcode_online.php

From the BTW message part, we understand that the flag has the variable name and we should use underscore between parts

For the variables, the value represent the order (in binary) that we should use.

We just need to put varibales name using the order and seprate by underscore 

## Flag

```
IDEH{L0L_N3V3R_KN3W_TH1S}
```
