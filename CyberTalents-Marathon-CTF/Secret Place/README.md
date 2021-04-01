
# Challenge Name: Secret Place


![date](https://img.shields.io/badge/date-05.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)


## Attached files

- [SecretPlace.exe](SecretPlace.exe)

## Detailed solution

Let's start by checking our file 
  
```
file SecretPlace.exe
SecretPlace.exe: PE32 executable (console) Intel 80386, for MS Windows
```  

It's a windows PE32 executable. I'll use Dotpeek to decompile it 

At resources we found a secret base64 string  
  
![image](https://user-images.githubusercontent.com/72421091/113331093-6ac8af80-9317-11eb-8587-cb4ae7390fe8.png)

Let's decode it  

## Flag

```
flag{0xALWAYS_CHECK_YOUR_EMBEDDED_RESOURCES}
```
