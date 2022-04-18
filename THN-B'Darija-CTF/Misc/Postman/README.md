# Challenge Name: Postman


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Misc-blueviolet.svg)   
![value](https://img.shields.io/badge/value-150-blue.svg) 

## Description

one of our team members recieved a blank letter , we do not know how can we help him figure out what it is about . can you help him ?   

_Author : c3p0d4y_

[postman.png](https://thnbdarija.ctfd.io/files/052e3f42dab3b7bfdc674087ef6ad6a0/postman.png?token=eyJ1c2VyX2lkIjoyNywidGVhbV9pZCI6MTUsImZpbGVfaWQiOjV9.Yltn5Q.PnRqYau8n7kM-FL596Ppp-mqMe4)
 
## Detailed solution  

![postman](https://user-images.githubusercontent.com/72421091/163736792-219d0322-9beb-4be4-be1d-b06efe16db8e.png)

We can see a barcode at the end 

![image](https://user-images.githubusercontent.com/72421091/163736819-a451e4dd-8f44-46d0-b2ca-553feee93448.png)  

It's a KIX barcode. We need to identify the country fot this type i'll use https://products.aspose.app/barcode/recognize/ 

We found a Number with the type OneCode `5111997989795521145195108515184`  

Decoding as ascii https://www.dcode.fr/ascii-code 

`3waba_4r3_l33T`

## Flag

```
thnb{3waba_4r3_l33T}
```
