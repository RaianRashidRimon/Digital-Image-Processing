import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Enter your image path here')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.astype(np.float64) / 255.0
rayleigh_scale = 0.5
rayleigh_noise_image = np.empty_like(image)
for i in range(3):
    rayleigh_noise = np.random.rayleigh(scale=rayleigh_scale, size=image[:, :, i].shape)
    rayleigh_noise_image[:, :, i] = image[:, :, i] + rayleigh_noise
rayleigh_noise_image = np.clip(rayleigh_noise_image, 0, 1)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(rayleigh_noise_image)
plt.title('Image with Rayleigh Noise')
plt.axis('off')
plt.tight_layout()
plt.show()
