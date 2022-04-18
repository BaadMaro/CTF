# Challenge Name: general informations 3


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-5-blue.svg)  


## Description

```
THIS CHALLENGE REQUIRES BUILDING  YOUR OWN PROFILE 

https://drive.google.com/file/d/1MkzKlZEdhRU0gCqMU-pjPlyd7Rfjxhfv/view?usp=sharing
```

what is the machine ip address ?

format _thnb{}_ 

_Author: c3p0_

## Detailed solution

The linux profile https://github.com/BaadMaro/CTF/blob/main/THN-B'Darija-CTF/Forensics/general%20informations/README.md#building-the-linux-profile 

Let's use the plugin linux_ifconfig to see ifconfig output 

```bash
python2 volatility/vol.py -f mem.raw --profile Linuxubuntu20_04-5_4_0-97-genericx64 linux_ifconfig
Volatility Foundation Volatility Framework 2.6.1

Interface        IP Address           MAC Address        Promiscous Mode
---------------- -------------------- ------------------ ---------------
lo               127.0.0.1            00:00:00:00:00:00  False
eth0             142.93.229.223       ba:50:5b:24:7a:9b  False
eth0             10.18.0.5            ba:50:5b:24:7a:9b  False
eth1             10.110.0.2           46:76:30:3f:e4:0b  False

```

The machine ip address is `142.93.229.223`  

## Flag

```
thnb{142.93.229.223}
```
