from Crypto.Cipher import AES
from binascii import unhexlify

ciphertext = unhexlify('91a413f0b000245c02b7a74e24ab2b0b')
IV = 'usefulstringhaha'
key = 'idehcitinptevent'

aes = AES.new(key.encode('utf-8'), AES.MODE_CBC,IV.encode('utf-8'))
enc = aes.decrypt(ciphertext)

print(enc)

print(enc[:-6].decode('utf-8'))

