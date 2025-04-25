import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

def rgb2hsi(rgb_img):
    rgb = rgb_img.astype(np.float32) / 255
    R = rgb[:, :, 0]
    G = rgb[:, :, 1]
    B = rgb[:, :, 2]
    I = (R + G + B) / 3
    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (min_rgb / (I + 1e-8))
    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G) ** 2 + (R - B) * (G - B)) + 1e-8
    theta = np.arccos(num / den)
    H = np.zeros_like(I)
    H[B <= G] = theta[B <= G]
    H[B > G] = 2 * np.pi - theta[B > G]
    H = H / (2 * np.pi)
    HSI = np.stack((H, S, I), axis=-1)
    return HSI

img = imageio.imread('Enter your image path here')
hsi = rgb2hsi(img)
hsi_uint8 = (hsi * 255).astype(np.uint8)

plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.imshow(img)
plt.title('Original RGB Image', fontsize=12)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(hsi[:, :, 0], cmap='hsv')
plt.title('Hue', fontsize=12)
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(hsi[:, :, 1], cmap='gray')
plt.title('Saturation', fontsize=12)
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(hsi[:, :, 2], cmap='gray')
plt.title('Intensity', fontsize=12)
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(hsi_uint8)
plt.title('Combined HSI', fontsize=12)
plt.axis('off')

plt.subplot(2, 3, 6)
plt.axis('off')

plt.tight_layout()
plt.show()
