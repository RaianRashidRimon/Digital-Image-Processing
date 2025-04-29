import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, img_as_float
from skimage.util import random_noise
from skimage.exposure import rescale_intensity

img = io.imread('Enter your image path here')
gray = color.rgb2gray(img)
gray = img_as_float(gray)

noise_level = 0.2
noisy = gray + noise_level * np.random.randn(*gray.shape)

log_image = np.log1p(noisy)
fft_image = np.fft.fft2(log_image)
fft_shifted = np.fft.fftshift(fft_image)

rows, cols = gray.shape
x, y = np.meshgrid(np.arange(cols), np.arange(rows))
center_x, center_y = cols // 2, rows // 2
sigma = 1
high_pass_filter = 1 - np.exp(-((x - center_x) ** 2 + (y - center_y) ** 2) / (2 * sigma ** 2))

filtered_fft = fft_shifted * high_pass_filter
filtered_image = np.fft.ifft2(np.fft.ifftshift(filtered_fft))
output = np.expm1(np.real(filtered_image))

noisy = rescale_intensity(noisy, in_range=(noisy.min(), noisy.max()))
output = rescale_intensity(output, in_range=(output.min(), output.max()))

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noisy, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(output, cmap='gray')
plt.title('Homomorphic Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()
