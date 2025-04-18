import cv2
import numpy as np
import matplotlib.pyplot as plt

input_image = cv2.imread('D:\\Academics\\Semesters\\4-1\\Lab\\Digital Image Processing Laboratory\\Programs\\Lab4\\noisy_image.jpg')
input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

filter_size = 3
filtered_image = cv2.medianBlur(input_image, filter_size)
filtered_image_rgb = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(input_image_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image_rgb)
plt.title('Filtered Image (Median Filter)')
plt.axis('off')

plt.tight_layout()
plt.show()

cv2.imwrite('filtered_image.jpg', filtered_image)
