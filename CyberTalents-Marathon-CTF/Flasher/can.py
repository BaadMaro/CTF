import binascii
a = open("C:/Users/maros/Downloads/can.txt", "r")
c = ''
b = a.readlines()
for x in b:
    if x == '010000\n':
      c += '0'
    else:
      c += '1'
print(binascii.unhexlify('%x' % int(c,2)).decode())
