from numpy import *
from PIL import Image

enc = Image.open(r"enc.png")
img = array(enc)

key = [41, 37, 23]

a, b, c = img.shape

for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(0,3):
            for j in range(0,41):
                e = (j * 251 + pixel[i]) / key[i]
                eint = int(e)
                if eint == e:
                    pixel[i] = e
                    break
        img[x][y] = pixel

flag = Image.fromarray(img)
flag.save('flag.png')
