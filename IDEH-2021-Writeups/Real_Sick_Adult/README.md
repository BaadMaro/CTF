
# Challenge Name: Real_Sick_Adult

![date](https://img.shields.io/badge/date-08.03.2021-brightgreen.svg)  
![solved after CTF](https://img.shields.io/badge/solved-after%20CTF-red.svg) 
![stego category](https://img.shields.io/badge/category-crypto-lightgrey.svg)
![score](https://img.shields.io/badge/score-75-blue.svg)


## Attached files
- [ciphertext](ciphertext)
- [key4orencryption.txt](key4orencryption.txt)
- [rsa.py](rsa.py)




## Detailed solution
First after reading the challenge name we can see that R,S and A are Uppercase, it's a hint for RSA.  
We can see also N used for the encryption, it's used as the modulus for public key for RSA encryption

As you know the encryption in RSA requires the public key which means modulus N and public exponent e.   
`e = 65537` is commonly used as a public exponent in the RSA cryptosystem.

An RSA modulus is the product of two secret prime numbers p and q : N = pq.
for factoring we goona use [factordb](http://factordb.com/)
````
n = 50949155494298606720156954091892517583265242208454601889241428835440365430753
q = 222812004210523246854601954625515044629
p = 228664320285721462178520010766169856157
````
We need to calcul :   
`phi = ( q — 1 ) * ( p — 1 )` Euler’s Totient for the number N.  
`d = inverse( e, phi )` the private key with the MODULAR INVERSE of e and phi.  

To decrypt the message :

`m ≡ c^d (mod n)`

I'm gonna use the python library **Pycryptodome**

```python
from Crypto.Util.number import *

f = open("C:/Users/maros/Downloads/ciphertext.txt", "rb")

c = bytes_to_long(f.read())
n = 50949155494298606720156954091892517583265242208454601889241428835440365430753
q = 222812004210523246854601954625515044629
p = 228664320285721462178520010766169856157
e = 65537

phi = (p-1)*(q-1)

d = inverse(e, phi)

flag = pow(c,d,n)
#print(long_to_bytes(flag))
print(long_to_bytes(flag)[10:-2].decode('utf-8'))
```

## Flag

```
IDEH{RS4_whYsm4LLN}
```
