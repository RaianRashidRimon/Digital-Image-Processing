import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Enter your image path here')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

skip_factor = 15
rows, cols, num_channels = img.shape
output_rows = int(np.ceil(rows / skip_factor))
output_cols = int(np.ceil(cols / skip_factor))

skipped_img = np.zeros((output_rows, output_cols, num_channels), dtype=img.dtype)

for channel in range(num_channels):
    skipped_img[:, :, channel] = img[::skip_factor, ::skip_factor, channel]

skipped_img_rgb = cv2.cvtColor(skipped_img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(6, 8))

plt.subplot(2, 1, 1)
plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(skipped_img_rgb)
plt.title('Pixel Skipped Image')
plt.axis('off')

plt.tight_layout()
plt.show()
