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
#b'\x02\xb6\xa8\x89\x18f~\xd6n\x00IDEH{RS4_whYsm4LLN}\n\n'

print(long_to_bytes(flag)[10:-2].decode('utf-8'))


#testing the encryption
#test = pow(flag,e,n)
#print(long_to_bytes(test))
#if test == c:
#    print("good")


