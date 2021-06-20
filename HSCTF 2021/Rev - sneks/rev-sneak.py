import sys
import string

file = open("sneak-output.txt", "r")

def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    x = f(n >> 1)
    y = f(n // 2 + 1)
    return g(x, y, not n & 1)


def e(b, j):
    return 5 * f(b) - 7 ** j


def d(v):
    return v << 1


def g(x, y, l):
    if l:
        return h(x, y)
    return x ** 2 + y ** 2


def h(x, y):
    return x * j(x, y)


def j(x, y):
    return 2 * y - x




aa = []
for x in file:
    aa.append(x[:-1])

flag = ""
inpi = 0
ff1 = []

for _ in range(12): 
    for x in string.printable:        
        inp = bytes(flag + x, 'utf-8')
        print("[+] Bruteforcing : " + flag + x )
        a = []
        for i, c in enumerate(inp):
            a.append(e(c, i))
        else:
            for c in a:
                ff1.append(d(c))
                if int(ff1[inpi]) == int(aa[inpi]):
                    flag += x                     
                    if (flag[-1] == '}') and (len(flag) == 24): #24 is output length
                        print("[+] Flag found   : " + flag) #flag{s3qu3nc35_4nd_5um5}
                        sys.exit()                 
                    inpi = inpi + 1
                    
                else:
                    ff1 = ff1[:-1]
                    

