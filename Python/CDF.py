import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
input_image = cv2.imread('Enter the path to the image here', cv2.IMREAD_GRAYSCALE)

# Calculate histogram
counts, gray_levels = np.histogram(input_image.flatten(), bins=256, range=[0,256])

# Calculate CDF
cdf = np.cumsum(counts) / np.sum(counts)

# Plotting
plt.figure(figsize=(12, 8))

# Original grayscale image
plt.subplot(2, 2, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Histogram
plt.subplot(2, 2, 2)
plt.bar(gray_levels[:-1], counts, width=1.0)
plt.title('Histogram of Grayscale Image')
plt.xlabel('Gray Level')
plt.ylabel('Frequency')

# CDF
plt.subplot(2, 2, 3)
plt.plot(gray_levels[:-1], cdf, 'b-')
plt.title('CDF of Grayscale Image')
plt.xlabel('Gray Level')
plt.ylabel('Cumulative Probability')

# Original grayscale image again
plt.subplot(2, 2, 4)
plt.imshow(input_image, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

plt.tight_layout()
plt.show()
