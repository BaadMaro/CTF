letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
flag = ""
encoded = "IOWJLQMAGH"
for i in encoded:
    for j in letters:
      if letters[(letters.index(j)+18)%26] == i:
        flag+=j
print("flag{"+ flag + "}")

