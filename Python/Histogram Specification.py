import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load input and reference images
input_image = cv2.imread('Enter the path to the image here')
reference_image = cv2.imread('Enter the path to the reference image here')



# Convert to grayscale if needed
if input_image.ndim == 3:
    input_gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
else:
    input_gray = input_image

if reference_image.ndim == 3:
    reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
else:
    reference_gray = reference_image

# Calculate histograms and CDFs
input_hist, input_bins = np.histogram(input_gray.flatten(), 256, [0, 256])
reference_hist, reference_bins = np.histogram(reference_gray.flatten(), 256, [0, 256])

input_cdf = np.cumsum(input_hist).astype(np.float64)
input_cdf /= input_cdf[-1]  # Normalize to [0,1]

reference_cdf = np.cumsum(reference_hist).astype(np.float64)
reference_cdf /= reference_cdf[-1]

# Create the mapping
mapping = np.zeros(256, dtype=np.uint8)
for i in range(256):
    diff = np.abs(input_cdf[i] - reference_cdf)
    mapping[i] = np.argmin(diff)

# Apply the mapping to get the specified image
specified_image = mapping[input_gray]

# Calculate histogram of specified image
specified_hist, _ = np.histogram(specified_image.flatten(), 256, [0, 256])

# Plotting
plt.figure(figsize=(12, 8))

# Input Image and Histogram
plt.subplot(2, 2, 1)
plt.imshow(input_gray, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.bar(np.arange(256), input_hist, width=1)
plt.title('Histogram of Original Image')
plt.xlabel('Gray Level')
plt.ylabel('Frequency')

# Reference Image and Histogram
plt.subplot(2, 2, 3)
plt.imshow(reference_gray, cmap='gray')
plt.title('Reference Grayscale Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.bar(np.arange(256), reference_hist, width=1)
plt.title('Histogram of Reference Image')
plt.xlabel('Gray Level')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Plot the Histogram Specified Image and its Histogram
plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.imshow(specified_image, cmap='gray')
plt.title('Histogram Specified Image')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.bar(np.arange(256), specified_hist, width=1)
plt.title('Histogram of Specified Image')
plt.xlabel('Gray Level')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
