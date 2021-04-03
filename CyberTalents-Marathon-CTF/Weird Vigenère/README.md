
# Challenge Name: Weird Vigenère


![date](https://img.shields.io/badge/date-31.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Cryptography-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Medium-blue.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)


## Attached files

- [Di-di-dah-dah-dah.txt](Di-di-dah-dah-dah.txt)

## Detailed solution

After searching for di dah i found that it's morce code 

Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes or dits and dahs. 

To reflect the sounds of Morse code receivers, the operators began to vocalize a dot as "dit", and a dash as "dah". Dots which are not the final element of a character became vocalized as "di". For example, the letter "c" was then vocalized as "dah-di-dah-dit".  

![image](https://user-images.githubusercontent.com/72421091/113422714-154adc00-93c5-11eb-8bae-1e125a810c36.png)

As we see "di" is ".", "dah" is "-", "dit" is "di" before space. Let's convert dits and dahs to dots and dashes. I'll use a simple Python script  

```python
f = open("morse.txt")

morse = f.read()

msg = morse.replace("-", "").replace("dah", "-").replace("dit", ".").replace("di", ".").replace("Dah", "-").replace("Dit", ".").replace("Di", ".")
print(msg)
``` 

The output : 
  
``` 
----- -..- ....- -.-. -.... ..-. ...-- ----- -.... -... ..--- .- --... ..... ..... ----- ..--- .- ....- --... ...-- ...-- --... ....- ...-- . ....- -... ...-- ...-- --... ----. ..--- .---- ..--- .---- ..--- .---- ...-- ....- ....- ..--- ...-- ----- ..... -.... ...-- ...-- ..--- ..... ..--- ..... ..... ----. ...-- ----- --... ..... ...-- ..--- ...-- .- ..... ----- ....- ---.. ...-- ...-- ...-- ....- -.... ....- ..--- .- --... --... ...-- ----- ..... --... ..--- ...-- -.... ---.. ...-- ....- ...-- ..... ....- ---.. --... ....- ...-- ....- ....- --... ..--- ...-- ..--- .---- ..... ....- ...-- ..--- ...-- ...-- ....- . -.... ....- ...-- .---- -.... . ....- --... ...-- -... -.... --... -.... --... ..--- ----. ..--- ----- ....- -.. ....- ....- ....- ..-. ..... .- --... -... ..... ....- ....- .---- ..... ..... ..... ..-. ....- -.... ....- .---- ....- -... ..... ..-. ..... --... ..... .---- ....- . ....- -.. ....- --... ....- -.... ....- --... --... -.. ....- ----- -.... ...-- -.... ..-. --... ..--- -.... ..-. -.... . -.... .---- -.... -.... -.... -.-. -.... .---- -.... --...
``` 

Let's decode it i'll use Cyberchef  

![image](https://user-images.githubusercontent.com/72421091/113423131-d9644680-93c5-11eb-9396-6e7b01cf134c.png)

The ouput is in hex format let's decode it 

``` 
Lo0k*uP*G3t>K3y!!!4B0V3%%Y0u2:PH34d*w0W#h45Ht4G#!T23Nd1nG;gg) MDOZ{TAU_FAK_WQNMGFG}@coronaflag
``` 
We can see our flag but it's decrypted ``` MDOZ{TAU_FAK_WQNMGFG} ```. We notice that the challenge name talk about a weird vigenere  

The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution.  

We can see the use of the word "weird" so probably it's not the Vigenère cipher but a variant  
  
Some Vigenère cipher variants : 
- Variant Beaufort
- Gronsfeld cipher
- Trithemius Cipher  

I started by checking the variant beaufort cipher https://www.dcode.fr/variant-beaufort-cipher  

Our main text contains : 

- Lo0k*uP*G3t>K3y!!!4B0V3%%Y0u2:PH34d*w0W#h45Ht4G#!T23Nd1nG;gg)
- MDOZ{TAU_FAK_WQNMGFG}
- coronaflag

I tried to decrypt the ciphert text using variant beaufort cipher with the key coranaflag but no success 

We know that our flag format is flag{} so i used the option "known plaintext word" to decrypt with mode "BEAUFORT CLASSIC (KEY-TXT)" 

![image](https://user-images.githubusercontent.com/72421091/113424928-dc146b00-93c8-11eb-83be-b765e892cfd6.png)

We get our flag with key ROOF 

![image](https://user-images.githubusercontent.com/72421091/113425469-cf444700-93c9-11eb-991a-f9ef199f0e14.png)


So to get the flag we need to decrypt our variant beaufort ciphertext with the key ROOF and the mode BEAUFORT CLASSIC (KEY-TXT)

The hint for the key was also mentioned in ```Lo0k*uP*G3t>K3y!!!4B0V3%%Y0u2:PH34d*w0W#h45Ht4G#!T23Nd1nG;gg)``` 

Lo0k*uP*G3t>K3y!!!4B0V3%%Y0u2 -> Look up get key above you -> ROOF  

## Flag

```
FLAG{YOU_ARE_SPECIAL}
```
