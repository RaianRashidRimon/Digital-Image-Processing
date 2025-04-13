import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread('D:/Academics/Semesters/4-1/Lab/Digital Image Processing Laboratory/Programs/1Github/Lab4/noisy_image.jpg')  
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    

# Define filter parameters
filter_size = 11
sigma = 15

# Apply Gaussian filter
filtered_img = np.zeros_like(img)
for channel in range(img.shape[2]):
    filtered_img[:, :, channel] = cv2.GaussianBlur(img[:, :, channel], (filter_size, filter_size), sigma)

# Display original and filtered images
plt.figure(figsize=(6, 8))

plt.subplot(2, 1, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.imshow(filtered_img)
plt.title('Filtered Image with Gaussian Filter')
plt.axis('off')

plt.tight_layout()
plt.show()
