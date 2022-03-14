from PIL import Image

im = Image.open("palette.PNG") 
im = im.resize((500, 250), resample=Image.BOX) #resizing to reduce loop time
pix = im.load()

colors = []

def rgb_to_hex(rgb):
    return "#%02x%02x%02x"  % rgb

for y in range(250):
    for x in range(500):
        hexc = rgb_to_hex(pix[x,y])        
        if hexc not in colors or hexc != colors[-1]:
            colors.append(hexc)
           
#print(colors)

f1 = ""
f2 = []
flag = []

#save only blue colors and convert hex values to ascii
for i in range(len(colors)):    
    if colors[i][3:] == 'ffff':
        f1 += colors[i][1:3]
f2 = bytearray.fromhex(f1).decode()

#cleaning duplicates / 6 because we have 6 colors in each line
for i in range(0,len(f2),6):
    if f2[i:i+6] not in flag:
        flag.append(f2[i:i+6])
        
#flag with duplicates        
print(f2)
print("\n")

#flag
print("".join(flag))
