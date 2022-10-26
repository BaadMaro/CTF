# Challenge Name: lorem ipsum




![date](https://img.shields.io/badge/date-11.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Crypto-blueviolet.svg)   
![score](https://img.shields.io/badge/score-150-blue.svg)

## Attached files

- [cipher.txt](cipher.txt)


## Detailed solution

The challenge description give us a hint   

![image](https://user-images.githubusercontent.com/72421091/114442229-dc2c1c00-9bbb-11eb-8429-b4411c351cc3.png)

Using google images i found that is Ave Maria 

I search for Ave Maria cipher and i found **Trithemius' Ave Maria**  

Trithemius Ave Maria is a steganographic process invented by the benedictine monk Johannes Trithemius around 1518. It replaces each letter of the plaintext by a group of words which looks like a poem.  

![image](https://user-images.githubusercontent.com/72421091/114444880-e3a0f480-9bbe-11eb-83a7-a9a6cefd57b3.png)
  
Our ciphertext with latin words 

```
Incompraehensibilis Conseruator.
Redemptor optimus
Iudex omnipotens
Sapientissimus omnipotens
Redemptor fabricator
Iudex redemptor
Optimus magnus
Aeternus iudex
Auctor omnipotens.
```
We can decrypt it manually or use a tool like https://www.dcode.fr/trithemius-ave-maria  

Output : 

```
RSTHISISTRITHEMIUS
```  
The challenge description mention that the flag is case sensitive and we know that the flag format is RS{} 

The first two words start with uppercase and our flag format also start with uppercase so we can assume that if the first character in latin word is uppercase the equivalent character is uppercase also 


## Flag

```
RS{ThIsIsTrItHeMiUs}
```
