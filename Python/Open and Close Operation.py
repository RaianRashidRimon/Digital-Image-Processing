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
selem = morphology.disk(8)
opened = morphology.opening(binary, selem)
closed = morphology.closing(binary, selem)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(binary, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(opened, cmap='gray')
plt.title('Opened Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(closed, cmap='gray')
plt.title('Closed Image')
plt.axis('off')

plt.tight_layout()
plt.show()
