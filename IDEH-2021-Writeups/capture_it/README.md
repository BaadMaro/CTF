
# Challenge Name: capture_it

![date](https://img.shields.io/badge/date-11.03.2021-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg) 
![stego category](https://img.shields.io/badge/category-forensics-lightgrey.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)


## Attached files
- [i_captured_THe_flag.zip](i_captured_THe_flag.zip)
- [decryption.py](decryption.py)




## Detailed solution
Starting by download and extract the attached zip file. we found a pcapng file

We use Wireshark to open the file. I started by searching for an HTTP request.
Using the filtre **http** i finded some intersting requests at the end :

````
11073	153.361891194	192.168.43.1	192.168.43.135	HTTP	539	GET /script HTTP/1.1 
11076	153.363021681	192.168.43.135	192.168.43.1	HTTP	932	HTTP/1.0 200 OK  (application/octet-stream)
11636	256.585971887	192.168.43.1	192.168.43.135	HTTP	541	GET /FLAG.enc HTTP/1.1 
11803	256.786844861	192.168.43.135	192.168.43.1	HTTP	1023	HTTP/1.0 200 OK  (application/octet-stream)
````

We have two HTTP requests to GET the files **script** and **Flag.enc** we can click fllow TCP stream on each request and see the content. 
  
The script is a Python 2.7 code : 

````python
import string
import random
from base64 import b64encode, b64decode

FLAG = 'IDEH{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'

enc_ciphers = ['rot47', 'b64e']
def rot47(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)

def b64e(s):
 return b64encode(s)


def encode(pt, cnt=50):
 tmp = '2{}'.format(b64encode(pt))
 for cnt in xrange(cnt):
  c = random.choice(enc_ciphers)
  i = enc_ciphers.index(c) + 1
  _tmp = globals()[c](tmp)
  tmp = '{}{}'.format(i, _tmp)

 return tmp

print encode(FLAG, cnt=?)
````
The script encode a Flag using a cnt number we can see some rot47 and base64 encoding.  
  
Start analyzing the script : 

Encode function : 

````python

def encode(pt, cnt=50):
 tmp = '2{}'.format(b64encode(pt)) # encode pt with b64 and add 2 at the beginning
 for cnt in xrange(cnt):           # cnt loop count
  c = random.choice(enc_ciphers)   # rot47 or b64e 
  i = enc_ciphers.index(c) + 1     # index of the chosen encyption in enc_ciphers + 1 / i = 1 or 2
  _tmp = globals()[c](tmp)         # rot47 or b64e encoding (from c) tmp 
  tmp = '{}{}'.format(i, _tmp)     # add to tmp i (1 or 2) at the beginning

 return tmp
````  
The function rot47 it's simply a rot47 encoding.  
ROT47 is a Caesar cipher rotated by 47 chars. It takes the ASCII characters between 33 and 126 and then moving them on 47 times. It is easy to **reverse the cipher**, by just performing the same operation.  

Trying the encode script :

FLAG = IDEH{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}   
encode(FLAG, cnt=2)    
print c to known the used encryption : rot47 rot 47  
Output : ``1`2SURFSHt4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH0=``  

Analyzing the encoding process :

- base64encode flag  + add 2 at th beginning : ``2SURFSHt4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH0=``  
- the for loop  
   cnt=0  
   rot47 ``a$&#u$wEc6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w_l``    
   add index rot47 + 1 at the beginning ``1a$&#u$wEc6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w_l``    
   encoded = ``1a$&#u$wEc6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w_l``    
   cnt=1  
   rot47 encoded `` `2SURFSHt4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH0= ``  
   add index rot47 + 1 at the beginnning ``1`2SURFSHt4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH0= ``   
   encoded = `` 1`2SURFSHt4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH0= `` 
   
   
The decryption process :   
  
   encoded = `` 1`2SURFSHt4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH0= ``  
   test first caractere if = 1 rot47 if = 2 b64enc  
	 remove first caractere  
	 decode with used enc ->  ``rot47dec(`2SURFSHt4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH0=)``   
   ``1a$&#u$wEc6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w_l``    
   
   ``1a$&#u$wEc6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w_l``    
	 test first caractere if = 1 rot47 if = 2 b64  
	 remove first caractere  
	 decode with used enc -> ``rot47dec(a$&#u$wEc6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w9c6w_l)`` 
   
   ``2SURFSHt4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH0=``      
	 test first caractere if = 1 rot47 if = 2 b64    
	 remove first caractere    
	 decode with used enc ->  ``b64dec(SURFSHt4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH0=)``   
	 IDEH{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}	 
	 
 Note : if encoded is base64 we have 2 cases decode and continue or we found the flag that start with IDEH.  
 
 I created a python 3 script to decrypt the flag.enc  
 
 ````python
 import base64

f = open("flag.enc", "r")
flag_en = f.read()

def rot47dec(s):
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)

tmp = flag_en

while tmp[:4] != 'IDEH':
  if tmp[0] == '1':
    tmp = rot47dec(tmp[1:])   
   
  elif tmp[0] == '2':
    tmp = base64.b64decode(tmp[1:]).decode('utf-8')

   
print(tmp)
````



## Flag

```
IDEH{why_w3_uSE_hTTp_t0_tr4ns}
```
