# Challenge Name: Shades Of Sky Blue


![date](https://img.shields.io/badge/date-13.03.2022-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg)    
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-10-blue.svg)  

## Description

Created By **sicmundos**

Sometimes even small differences can have profound meaning. Attempt to understand this pallet of colors and extract the flag.

[Download Attachement](https://s3.eu-west-3.amazonaws.com/crisis-assets/crisis_attachements/zjZGlLkOosACw6NoTODKA6CenGrLbnS013OfEZXQ.zip)

## Detailed solution

![palette](https://user-images.githubusercontent.com/72421091/158076814-e718875c-9fd0-4c01-b484-d849978ae0b0.PNG)

We can see that we have 18 blocks with shades of blue color

We can use some online tools to check hex and rgb colors https://imagecolorpicker.com/ 

![image](https://user-images.githubusercontent.com/72421091/158076933-75c7d530-b604-4efd-9897-fa87d1787a6b.png)

The hex code and rgba values for the first block are `#43ffff rgba(67,255,255,255)` 

If we check every block color we can see that the only value changing is red. If we try to convert the value to ASCII we can see the flag parts

Exemple :
- #43ffff => hex 43 => ASCII C

We can do it manually using the online tool and extract hex colors in order and convert them to ASCII or using a script

I'll use the python library [Pillow](https://pillow.readthedocs.io/en/stable/)

```python
from PIL import Image

im = Image.open("palette.PNG") 
im = im.resize((500, 250), resample=Image.BOX) #resizing to reduce loop time
pix = im.load()

colors = []

def rgb_to_hex(rgb):
    return "#%02x%02x%02x"  % rgb

for y in range(250):
    for x in range(500):
        hexc = rgb_to_hex(pix[x,y])        
        if hexc not in colors or hexc != colors[-1]:
            colors.append(hexc)
           
#print(colors)

f1 = ""
f2 = []
flag = []

#save only blue colors and convert hex values to ascii
for i in range(len(colors)):    
    if colors[i][3:] == 'ffff':
        f1 += colors[i][1:3]
f2 = bytearray.fromhex(f1).decode()

#cleaning duplicates / 6 because we have 6 colors in each line
for i in range(0,len(f2),6):
    if f2[i:i+6] not in flag:
        flag.append(f2[i:i+6])
        
#flag with duplicates        
print(f2)
print("\n")

#flag
print("".join(flag))
```
Output
```
CRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISISCRISIS{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8{k65P8XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}XeaHT}


CRISIS{k65P8XeaHT}
```
We can verify the length of flag too to assure that it's equal to 18 

## Flag

```
CRISIS{k65P8XeaHT}
```
