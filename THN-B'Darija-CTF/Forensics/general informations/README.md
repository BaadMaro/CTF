# Challenge Name: general informations 



![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-5-blue.svg)  


## Description

we recently in our mahlaba forensics solution company received a client that has been a vitcime of a cyber attack . after a long talk with him we managed to get a full dump of his compromised server . we know that you are one of the best people in the forensics field help us figure out how he got hacked .

```
THIS CHALLENGE REQUIRES BUILDING  YOUR OWN PROFILE 

https://drive.google.com/file/d/1MkzKlZEdhRU0gCqMU-pjPlyd7Rfjxhfv/view?usp=sharing
```

what is the linux version ? submit the linux version as the first flag . 

format _thnb{}_ 

_Author: c3p0_

## Detailed solution

Identifing the kernel dosen't require building the linux profile but we gonna need it for next challenges

I used volatitlity 3 to read banners from the dump

python3 volatility3/vol.py -f mem.raw banners.Banners

```
Volatility 3 Framework 2.0.3 Progress: 100.00 PDB scanning finished Offset Banner 0x310001a0 Linux version 5.4.0-97-generic (buildd@lcy02-amd64-032) (gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)) #110-Ubuntu SMP Thu Jan 13 18:22:13 UTC 2022 (Ubuntu 5.4.0-97.110-generic 5.4.162) 0x31f9fdd4 Linux version 5.4.0-97-generic (buildd@lcy02-amd64-032) (gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)) #110-Ubuntu SMP Thu Jan 13 18:22:13 UTC 2022 (Ubuntu 5.4.0-97.110-generic 5.4.162) 0x3805ac88 Linux version 5.4.0-97-generic (buildd@lcy02-amd64-032) (gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)) #110-Ubuntu SMP Thu Jan 13 18:22:13 UTC 2022 (Ubuntu 5.4.0-97.110-generic 5.4.162)
```

Our kernerl is `5.4.0-97-generic` 

## Flag

```
thnb{5.4.0-97-generic}
``` 
