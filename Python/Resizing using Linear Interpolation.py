import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator
import imageio.v2 as imageio

# Read the image
img = imageio.imread('Enter the path to the image here')  # Replace with your actual image path

scale_x = 6
scale_y = 4

original_rows, original_cols, num_channels = img.shape
new_rows = int(round(original_rows * scale_y))
new_cols = int(round(original_cols * scale_x))

# Generate grid for new image
x_new, y_new = np.meshgrid(np.arange(new_cols), np.arange(new_rows))
orig_x = (x_new - 0.5) / scale_x + 0.5
orig_y = (y_new - 0.5) / scale_y + 0.5

# Clip coordinates to be within image bounds
orig_x = np.clip(orig_x, 0, original_cols - 1)
orig_y = np.clip(orig_y, 0, original_rows - 1)

# Prepare output image
resized_img = np.zeros((new_rows, new_cols, num_channels), dtype=np.uint8)

# Interpolate each channel
for c in range(num_channels):
    channel_data = img[:, :, c].astype(np.float32)
    interpolator = RegularGridInterpolator(
        (np.arange(original_rows), np.arange(original_cols)),
        channel_data,
        method='linear',
        bounds_error=False,
        fill_value=0
    )
    
    coords = np.stack((orig_y.ravel(), orig_x.ravel()), axis=-1)
    interpolated_values = interpolator(coords).reshape((new_rows, new_cols))
    resized_img[:, :, c] = np.clip(interpolated_values, 0, 255).astype(np.uint8)

# Display the original and resized images
plt.figure(figsize=(6, 8))
plt.subplot(2, 1, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 1, 2)
plt.imshow(resized_img)
plt.title("Resized Image with Linear Interpolation")
plt.axis("off")

plt.tight_layout()
plt.show()
