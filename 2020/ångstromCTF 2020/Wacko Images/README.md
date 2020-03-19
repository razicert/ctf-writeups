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
Search for "_" in file.

Flag: rtcp{w0Rd5_HuRt_,_d0n'T_Bu11y_,_k1Dz}
