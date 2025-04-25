import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, morphology
from skimage.util import img_as_ubyte
from skimage.filters import threshold_otsu

img = io.imread('Enter your image path here')

if img.ndim == 3:
    gray = color.rgb2gray(img)
else:
    gray = img

binary = gray > threshold_otsu(gray)
selem = morphology.disk(9)
eroded = morphology.erosion(binary, selem)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(binary, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(eroded, cmap='gray')
plt.title('Eroded Image')
plt.axis('off')

plt.tight_layout()
plt.show()
