import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Enter your image path here')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = image.astype(np.float64) / 255.0

erlang_shape = 2
erlang_scale = 0.2   

erlang_noise_image = np.empty_like(image)
for i in range(3):
    erlang_noise = np.random.gamma(erlang_shape, erlang_scale, image[:, :, i].shape)
    erlang_noise_image[:, :, i] = image[:, :, i] + erlang_noise
erlang_noise_image = np.clip(erlang_noise_image, 0, 1)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(erlang_noise_image)
plt.title('Image with Erlang Noise')
plt.axis('off')

plt.tight_layout()
plt.show()
