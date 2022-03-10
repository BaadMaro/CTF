# Challenge Name: Golden Bug 1843


![date](https://img.shields.io/badge/date-06.03.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-20-blue.svg)  


## Description

Created By **sicmundos**

The Gold Bug(1843), my favorite story, referred to those who favored basing the U.S. monetary system on gold excluding silver. Take your time and read between lines.

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/hkxzFmkvtDfoZKPfUuE39LjAoNpnweH8wiUyoT0h.zip)

## Detailed solution

We can see two files : cipher.png and glodbug.png

**cipher.png**

![cipher](https://user-images.githubusercontent.com/72421091/156956072-4fab7a58-2624-4304-8a16-cac646557f44.PNG)

**glodbug.png**

![goldbug](https://user-images.githubusercontent.com/72421091/156956087-bd9720c7-052a-4663-8cc9-b3ca04316a42.png)

Searching about glod-Bug, i found a story that involves cryptography by using a substitution cipher 

### Gloden-Bug 1843

"The Gold-Bug" is a short story by American writer Edgar Allan Poe published in 1843. The plot follows William Legrand, who was bitten by a gold-colored bug. His servant Jupiter fears that Legrand is going insane and goes to Legrand's friend, an unnamed narrator, who agrees to visit his old friend. Legrand pulls the other two into an adventure after deciphering a secret message that will lead to a buried treasure

The story involves cryptography with a detailed description of a method for solving a simple substitution cipher using letter frequencies. The encoded message is:

![image](https://user-images.githubusercontent.com/72421091/156956747-806d4952-2aae-443c-bd9b-df45fb2c1282.png)

You can solve the cipher using letter frequencies but we're coming from the future, as it's a simple substitution cipher we already now the conversion table x)  
 
![image](https://user-images.githubusercontent.com/72421091/156957175-ac8a5af1-8ee0-4a9f-8a4b-e4407b2ee4c4.png)  

We can use a decoder for that https://www.dcode.fr/gold-bug-poe 

```
365.(9*†¶8
GIAPRMNDVE
```

## Flag

```
CRISIS{GIAPRMNDVE}
```
