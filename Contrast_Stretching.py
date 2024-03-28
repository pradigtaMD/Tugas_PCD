import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image

def getGrayColor(rgb):
    return rgb[0]

def setGrayColor(color):
    return [color, color, color]

img = Image.open('Lena.jpg')
img = np.asarray(img)

# copy list not reference
ct = deepcopy(img)

r1 = 100
s1 = 50
r2 = 150
s2 = 200

def getGrayColor(rgb):
    return rgb[0]

def applyContrastStretching(img, r1, s1, r2, s2):
    ct = deepcopy(img)

    for i in range(len(img)):
        for j in range(len(img[i])):
            x = getGrayColor(img[i][j])
            if 0 <= x <= r1:
                ct[i][j] = setGrayColor(int(s1 / r1 * x))
            elif r1 < x <= r2:
                ct[i][j] = setGrayColor(int(((s2 - s1) / (r2 - r1)) * (x - r1) + s1))
            elif r2 < x <= 255:
                ct[i][j] = setGrayColor(int(((255 - s2) / (255 - r2)) * (x - r2) + s2))

    return ct

ct = applyContrastStretching(img, r1, s1, r2, s2)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(ct)
plt.title('Contrast-Stretched Image')
plt.show()