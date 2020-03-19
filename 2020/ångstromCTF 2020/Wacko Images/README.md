# ångstromCTF 2020 <br/>
**category: Crypto** <br/>
**Challenge Name: Wacko Images** <br/>
**Points: 90** <br/>

**Description:** <br/>
> How to make hiding stuff a e s t h e t i c? And can you make it normal again? enc.png image-encryption.py
> The flag is actf{x#xx#xx_xx#xxx} where x represents any lowercase letter and # represents any one digit number.

We get an encrypted image and encryption script:
image-encryption.py :
```python
from numpy import *
from PIL import Image

flag = Image.open(r"flag.png")
img = array(flag)

key = [41, 37, 23]

a, b, c = img.shape

for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(0,3):
            pixel[i] = pixel[i] * key[i] % 251
        img[x][y] = pixel

enc = Image.fromarray(img)
enc.save('enc.png')
```
enc.png :

![enc.png](https://github.com/razicert/ctf-writeups/blob/master/2020/%C3%A5ngstromCTF%202020/Wacko%20Images/enc.png)

**Solution:** <br/>
From the script we gather that for correct 'j' the ``` e = (j * 251 + pixel[i]) / key[i] ``` gives us the original value before encryption, so we loop through 'j' in range(0, max(key)) and for each 'e' we check if it's a floating point number or not, if not, it's possibly the right one. We add a few lines to the encryption script and hope we get an image that is close enough to original image.

image-decryption.py :
```python
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
```

flag.png :

![flag.png](https://github.com/razicert/ctf-writeups/blob/master/2020/%C3%A5ngstromCTF%202020/Wacko%20Images/flag.png)

Close enough. 

Flag: actf{m0dd1ng_sk1llz}
