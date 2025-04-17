import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
import imageio.v2 as imageio


img = imageio.imread('Enter image path here')
img = img.astype(np.uint8)

filter_size = 6
kernel = np.ones((filter_size, filter_size), dtype=np.float32) / (filter_size ** 2)

filtered_img = np.zeros_like(img)
for c in range(img.shape[2]):
    filtered_img[:, :, c] = convolve(img[:, :, c], kernel, mode='nearest')

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_img)
plt.title('Filtered Image with Mean Filter')
plt.axis('off')

plt.tight_layout()
plt.show()


