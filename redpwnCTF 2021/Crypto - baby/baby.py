from Crypto.Util.number import long_to_bytes, inverse

n = 228430203128652625114739053365339856393
e = 65537
c = 126721104148692049427127809839057445790

p = 12546190522253739887
q = 18207136478875858439

phi = (p-1)*(q-1)

d = inverse(e, phi)

flag = pow(c,d,n)

print(long_to_bytes(flag).decode())

