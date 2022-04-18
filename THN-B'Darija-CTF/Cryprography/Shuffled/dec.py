

f = open("e2.txt" ,"r")

flag = ""
for i in f.readlines():
    a = sorted(i)
    print(a[-1])
    flag += a[-1]
print(flag)
