import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Enter your image path here')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

new_rows = 500
new_cols = 500
original_rows, original_cols, num_channels = img.shape

resized_img = np.zeros((new_rows, new_cols, num_channels), dtype=np.uint8)

row_scale = original_rows / new_rows
col_scale = original_cols / new_cols

for r in range(new_rows):
    for c in range(new_cols):
        orig_r = round((r + 0.5) * row_scale - 0.5)
        orig_c = round((c + 0.5) * col_scale - 0.5)

        orig_r = max(0, min(original_rows - 1, orig_r))
        orig_c = max(0, min(original_cols - 1, orig_c))

        resized_img[r, c, :] = img[orig_r, orig_c, :]

resized_img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(6, 8))

plt.subplot(2, 1, 1)
plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(resized_img_rgb)
plt.title('Resized Image using Replication Method')
plt.axis('off')

plt.tight_layout()
plt.show()
