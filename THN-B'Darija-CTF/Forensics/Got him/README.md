# Challenge Name: Got him


![date](https://img.shields.io/badge/date-17.04.2022-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-40-blue.svg)  


## Description

```
THIS CHALLENGE REQUIRES BUILDING  YOUR OWN PROFILE 

https://drive.google.com/file/d/1MkzKlZEdhRU0gCqMU-pjPlyd7Rfjxhfv/view?usp=sharing
```

what is the attacker ip address ?

format _thnb{}_ 

_Author: c3p0_

## Detailed solution

The linux profile https://github.com/BaadMaro/CTF/blob/main/THN-B'Darija-CTF/Forensics/general%20informations/README.md#building-the-linux-profile 

Let's use the plugin linux_netstat to see connections

```bash
python2 volatility/vol.py -f mem.raw --profile Linuxubuntu20_04-5_4_0-97-genericx64 linux_netstat
```
We can see a suspicious connections with nc 

```
TCP      142.93.229.223  :60310 188.166.64.46   : 1337 SYN_SENT                       nc/1167
TCP      142.93.229.223  :60314 188.166.64.46   : 1337 SYN_SENT                       nc/2669
```

The port 1337 is used by the attacker for the reverse shell using netcat

## Flag

```
thnb{188.166.64.46}
```
