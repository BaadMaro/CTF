# Challenge Name: Moon


![date](https://img.shields.io/badge/date-26.02.2023-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Steganography-blueviolet.svg)   
![value](https://img.shields.io/badge/value-100-blue.svg)  


## Description

The moon is everywhere, because CIT is the moon.

[flag.png](flag.png)
[flagged](flagged)

**Author**: kw4ntum

## Detailed solution 


flagged file has a double base64 encoding that give us "doublepass" 

![image](https://user-images.githubusercontent.com/72421091/221620213-57c1eeda-4254-42c0-a290-2f3637592097.png)

For our image i check strings and metadata but noting detected. It could be that flagged is the secret used to hide data inside the image. 

I check aperisolve that automate muliple checks. it detected some potential passwords which includ our doublepass https://www.aperisolve.com/a41cd0aeb78a0a124b9d092a17492838

![image](https://user-images.githubusercontent.com/72421091/221622558-5d9dcfc6-5689-4226-80df-94301865fb63.png)


As we have a png image steghide will not be an option. We need to explore other tools used for hide secrets inside png images like openstego https://github.com/syvaidya/openstego

![image](https://user-images.githubusercontent.com/72421091/221621641-1fce36ac-b51e-4521-96a0-eec7b441ab46.png)

The extracted data 

![image](https://user-images.githubusercontent.com/72421091/221623029-c3a1d968-6f86-4f64-89fc-a806f6a7b492.png)

## Flag

```
IDEH{34sy_st3g4no_f0r_ya}
```


