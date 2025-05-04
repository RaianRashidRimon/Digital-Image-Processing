import numpy as np
import cv2
import matplotlib.pyplot as plt
original_image = cv2.imread(r'Enter your image path here')
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
original_image = original_image.astype(np.float32) / 255.0

rows, cols, channels = original_image.shape
x, y = np.meshgrid(np.arange(cols), np.arange(rows))
frequency = 20
periodic_noise = 0.1 * np.sin(2 * np.pi * frequency * x / cols) + \
                 0.1 * np.sin(2 * np.pi * frequency * y / rows)
noisy_image = np.zeros_like(original_image)
for c in range(channels):
    noisy_image[:, :, c] = original_image[:, :, c] + periodic_noise
noisy_image = np.clip(noisy_image, 0, 1)
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original RGB Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(noisy_image)
plt.title('Image with Periodic Noise')
plt.axis('off')
plt.tight_layout()
plt.show()
