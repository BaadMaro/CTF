
# Challenge Name: Baby


![date](https://img.shields.io/badge/date-16.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![crypto category](https://img.shields.io/badge/category-Reverse-blueviolet.svg)   
![level](https://img.shields.io/badge/level-Easy-blue.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)


## Attached files

- [Baby3786587346542865082.exe](Baby3786587346542865082.exe)

## Detailed solution

Let's fireup IDA and check main function

![image](https://user-images.githubusercontent.com/72421091/113362061-62876900-9345-11eb-9b57-807596402d9e.png)

We can see our flag caracteres, let's make a breakpoint at the end of main and use the local windows debugger 

![image](https://user-images.githubusercontent.com/72421091/113362628-b0e93780-9346-11eb-9258-6656dc21f58b.png) 

Click at ebp and choose jump to operand  

![image](https://user-images.githubusercontent.com/72421091/113362755-03c2ef00-9347-11eb-9d4e-9770a1bfbb6a.png)



## Flag

```
FLAG{345y_P345Y}
```
