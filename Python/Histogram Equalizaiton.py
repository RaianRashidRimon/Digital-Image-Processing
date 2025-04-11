import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
input_image = cv2.imread('Enter the path to the image here')


# Convert to grayscale if it's a color image
if input_image.ndim == 3:
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
else:
    gray_image = input_image

# Apply histogram equalization
equalized_image = cv2.equalizeHist(gray_image)

# Plotting
plt.figure(figsize=(12, 8))

# Original Grayscale Image
plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

# Histogram of Original Image
plt.subplot(2, 2, 2)
plt.hist(gray_image.ravel(), bins=256, range=[0, 256], color='gray')
plt.title('Histogram of Original Image')
plt.xlabel('Gray Level')
plt.ylabel('Frequency')

# Histogram Equalized Image
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Histogram Equalized Image')
plt.axis('off')

# Histogram of Equalized Image
plt.subplot(2, 2, 4)
plt.hist(equalized_image.ravel(), bins=256, range=[0, 256], color='gray')
plt.title('Histogram of Equalized Image')
plt.xlabel('Gray Level')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
