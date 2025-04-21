import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from scipy.ndimage import gaussian_filter

def sobel_detection(img):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    grad_x = convolve2d(img, sobel_x, mode='same', boundary='symm')
    grad_y = convolve2d(img, sobel_y, mode='same', boundary='symm')
    return np.sqrt(grad_x**2 + grad_y**2)

def prewitt_detection(img):
    prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    grad_x = convolve2d(img, prewitt_x, mode='same', boundary='symm')
    grad_y = convolve2d(img, prewitt_y, mode='same', boundary='symm')
    return np.sqrt(grad_x**2 + grad_y**2)

def isotropic_detection(img):
    sigma = 1
    smoothed_img = gaussian_filter(img, sigma)
    laplacian_filter = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    edge_img = convolve2d(smoothed_img, laplacian_filter, mode='same', boundary='symm')
    return np.abs(edge_img)

def roberts_detection(img):
    roberts_x = np.array([[1, 0], [0, -1]])
    roberts_y = np.array([[0, 1], [-1, 0]])
    grad_x = convolve2d(img, roberts_x, mode='same', boundary='symm')
    grad_y = convolve2d(img, roberts_y, mode='same', boundary='symm')
    return np.sqrt(grad_x**2 + grad_y**2)

def show_all_edge_detections(image_path):
    rgb_img = cv2.imread(image_path)
    rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
    gray_img = gray_img.astype(np.float32) / 255.0

    sobel_edge = sobel_detection(gray_img)
    prewitt_edge = prewitt_detection(gray_img)
    isotropic_edge = isotropic_detection(gray_img)
    roberts_edge = roberts_detection(gray_img)

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 3, 1), plt.imshow(rgb_img), plt.title('Original RGB Image'), plt.axis('off')
    plt.subplot(2, 3, 2), plt.imshow(gray_img, cmap='gray'), plt.title('Grayscale Image'), plt.axis('off')
    plt.subplot(2, 3, 3), plt.imshow(sobel_edge, cmap='gray'), plt.title('Sobel Edge Detection'), plt.axis('off')
    plt.subplot(2, 3, 4), plt.imshow(prewitt_edge, cmap='gray'), plt.title('Prewitt Edge Detection'), plt.axis('off')
    plt.subplot(2, 3, 5), plt.imshow(isotropic_edge, cmap='gray'), plt.title('Isotropic Edge Detection'), plt.axis('off')
    plt.subplot(2, 3, 6), plt.imshow(roberts_edge, cmap='gray'), plt.title('Roberts Edge Detection'), plt.axis('off')
    plt.tight_layout()
    plt.show()
    
show_all_edge_detections('Enter your image path here')
