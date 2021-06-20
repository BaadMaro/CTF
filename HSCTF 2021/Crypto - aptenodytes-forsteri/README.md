# Challenge Name: aptenodytes-forsteri


![date](https://img.shields.io/badge/date-15.06.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Cryptography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-183-blue.svg)  


## Description

Here's a warmup cryptography challenge. Reverse the script, decrypt the output, submit the flag.

- [aptenodytes-forsteri.py](aptenodytes-forsteri.py)  
- [output.txt](output.txt)

## Detailed solution  

We need to reverse the script and use the output to decrypt the flag  

- The flag is a string that start with flag{ and end with }   
- Uppercase letters used in encoding   
- We need to find the flag characters that it give us the encoded characters (output.txt) with letters[(letters.index(flag_chars)+18)%26]  

A python script to decrypt the output  

```python

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
flag = ""
encoded = "IOWJLQMAGH"
for i in encoded:
    for j in letters:
      if letters[(letters.index(j)+18)%26] == i:
        flag+=j
print("flag{"+ flag + "}")
```
## Flag

```
flag{QWERTYUIOP}
```
