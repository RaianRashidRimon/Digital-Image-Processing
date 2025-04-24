import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from skimage.color import rgb2gray

img = imageio.imread('Enter your image path here')
grayscale_img = rgb2gray(img)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original RGB Image', fontsize=12)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(grayscale_img, cmap='gray')
plt.title('Grayscale Image', fontsize=12)
plt.axis('off')

plt.tight_layout()
plt.show()
