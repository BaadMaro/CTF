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

Our kernel version is `5.4.0-97-generic` 

## Building the linux profile

To be able to interact with our dump we need to create a specific profile to use it with volatility

I followed the article https://beguier.eu/nicolas/articles/security-tips-3-volatility-linux-profiles.html 

I didn't have a docker setup so i used WSL in Windows, it has the same ubuntu version 20.04 

- git clone https://github.com/volatilityfoundation/volatility
- cd volatility/tools/linux/
- sed -i 's/$(shell uname -r)/5.4.0-97-generic/g' Makefile
- sudo apt update && sudo apt install -y linux-image-5.4.0-97-generic linux-headers-5.4.0-97-generic build-essential dwarfdump make zip
- cd /volatility/
- Make
- zip ubuntu20.04-5.4.0-97-generic.zip module.dwarf /boot/System.map-5.4.0-97-generic
- cp ubuntu20.04-5.4.0-97-generic.zip <volatility>/plugins/overlays/linux/

Output [ubuntu20.04-5.4.0-97-generic.zip](ubuntu20.04-5.4.0-97-generic.zip) 

Now we can verify the profile 

```bash
python2 volatility/vol.py --info | grep Profile
Volatility Foundation Volatility Framework 2.6.1
Profiles
Linuxubuntu20_04-5_4_0-97-genericx64 - A Profile for Linux ubuntu20.04-5.4.0-97-generic x64
```
Let's use the plugin linux_bash

```bash
python2 volatility/vol.py -f mem.raw --profile Linuxubuntu20_04-5_4_0-97-genericx64 linux_bash
Volatility Foundation Volatility Framework 2.6.1

Pid      Name                 Command Time                   Command
-------- -------------------- ------------------------------ -------
    1057 bash                 2022-04-08 08:28:31 UTC+0000   apt install vsftpd zip ssh apach2 php libapache2-mod-php php-mysql
    1057 bash                 2022-04-08 08:28:31 UTC+0000   mv index.html index.php
    1057 bash                 2022-04-08 08:28:31 UTC+0000   sudo ufw status
    1057 bash                 2022-04-08 08:28:31 UTC+0000   w
    1057 bash                 2022-04-08 08:28:31 UTC+0000   tail -f auth.log
    1057 bash                 2022-04-08 08:28:31 UTC+0000   systemctl sshd status
    1057 bash                 2022-04-08 08:28:31 UTC+0000   ls -la
  ....
```
  
  
## Flag

```
thnb{5.4.0-97-generic}
``` 
