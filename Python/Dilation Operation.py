import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, morphology
from skimage.filters import threshold_otsu

img = io.imread('C:\\Users\\Admin\\OneDrive\\Desktop\\ryse.jpg')

if img.ndim == 3:
    gray = color.rgb2gray(img)
else:
    gray = img

binary = gray > threshold_otsu(gray)
selem = morphology.disk(2)
dilated = morphology.dilation(binary, selem)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(binary, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dilated, cmap='gray')
plt.title('Dilated Image')
plt.axis('off')

plt.tight_layout()
plt.show()
