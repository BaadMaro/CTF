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




