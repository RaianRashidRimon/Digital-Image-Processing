import cv2
import numpy as np
import matplotlib.pyplot as plt

# Kernel size
kernel_size = 3

# Create Laplacian kernel
laplacian_kernel = -4 * np.ones((kernel_size, kernel_size))
laplacian_kernel += np.eye(kernel_size) * (kernel_size**2 - 1)

# Read the image
input_image = cv2.imread('D:\\Academics\Semesters\\4-1\\Lab\\Digital Image Processing Laboratory\\Programs\\Lab4\\stray.jpg', cv2.IMREAD_GRAYSCALE)

# Apply convolution
filtered_image = cv2.filter2D(src=input_image.astype(np.float32), ddepth=-1, kernel=laplacian_kernel)

# Normalize the result to 0-1 range
filtered_image = cv2.normalize(filtered_image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

# Plot the results
plt.figure(figsize=(6, 8))
plt.subplot(2, 1, 1)
plt.imshow(input_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Laplacian Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()
