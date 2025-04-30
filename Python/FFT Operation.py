import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.exposure import rescale_intensity

original_image = io.imread('Enter your image path here')
if original_image.ndim == 3:
    gray_image = color.rgb2gray(original_image)
else:
    gray_image = original_image
gray_image = gray_image.astype(float)

fft_image = np.fft.fft2(gray_image)
fft_shifted = np.fft.fftshift(fft_image)
magnitude_spectrum = np.log1p(np.abs(fft_shifted))
magnitude_spectrum = rescale_intensity(magnitude_spectrum, in_range=(0, np.max(magnitude_spectrum)))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.axis('off')

plt.tight_layout()
plt.show()
