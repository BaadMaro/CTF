import random

def padding(char):
    c = []
    for i in range(32, char):
        c.append(chr(i))
    c.append(chr(char))
    random.shuffle(c)
    print("".join(c))

flag = str(input())

for i in flag:
    _l =  ord(i)
    padding(_l)
