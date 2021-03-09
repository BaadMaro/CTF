from PIL import Image

#first decode the messge from base32 and replace IDEH by 1 and CTF by 0 (cyberchef cs im bad with py xd) -> alien.txt

im= Image.new("RGB", (32, 66), 'white')
f = open("C:/Users/maros/Downloads/alien.txt")

b = [line[:-1] for line in f]
pixels = im.load()
pi = []

for x in range(33):
    pi.append([int(d) for d in str(b[x])])
for x in range(32):   
    for y in range(66):
       if pi[x][y] == 0:
         pixels[x,y] = (0, 0, 0)    

     
#im = im.resize((1880, 1880), Image.ANTIALIAS) #the image is too small 32x65
im = im.resize((1880, 1880), resample=Image.BOX) #upscale without blur
im.show()
im.save("alien.jpg")
