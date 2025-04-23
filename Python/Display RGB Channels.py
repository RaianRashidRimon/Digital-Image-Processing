import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

img = imageio.imread('Enter your image path here')

R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

zero_channel = np.zeros_like(R)

red_channel_img = np.stack((R, zero_channel, zero_channel), axis=2)
green_channel_img = np.stack((zero_channel, G, zero_channel), axis=2)
blue_channel_img = np.stack((zero_channel, zero_channel, B), axis=2)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title('Original RGB Image', fontsize=12)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(red_channel_img)
plt.title('Red Channel', fontsize=12)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(green_channel_img)
plt.title('Green Channel', fontsize=12)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(blue_channel_img)
plt.title('Blue Channel', fontsize=12)
plt.axis('off')

plt.tight_layout()
plt.show()
