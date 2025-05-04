import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
original_image = cv2.imread(r'Enter your image path here')
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
original_image = original_image.astype(np.float32) / 255.0
def add_salt_and_pepper_noise(image, amount=0.2):
    noisy = np.copy(image)
    total_pixels = image.shape[0] * image.shape[1]
    num_salt = int(total_pixels * amount / 2)
    num_pepper = int(total_pixels * amount / 2)
    for _ in range(num_salt):
        i = random.randint(0, image.shape[0] - 1)
        j = random.randint(0, image.shape[1] - 1)
        noisy[i, j] = 1.0
    for _ in range(num_pepper):
        i = random.randint(0, image.shape[0] - 1)
        j = random.randint(0, image.shape[1] - 1)
        noisy[i, j] = 0.0

    return noisy
noisy_image = add_salt_and_pepper_noise(original_image, amount=0.5)
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(noisy_image)
plt.title('Salt & Pepper Noise Image')
plt.axis('off')
plt.tight_layout()
plt.show()
