import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('Enter your image path here')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.astype(np.float64) / 255.0

# Add Gaussian noise
gaussian_variance = 0.5
mean = 0
gaussian_noise = np.random.normal(mean, np.sqrt(gaussian_variance), image.shape)
noisy_image = image + gaussian_noise
noisy_image = np.clip(noisy_image, 0, 1)

# Display the images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(noisy_image)
plt.title('Image with Gaussian Noise')
plt.axis('off')

plt.tight_layout()
plt.show()
