import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'Enter your image path here')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
circles1 = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=200, param2=30, minRadius=20, maxRadius=60)
circles2 = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=200, param2=30, minRadius=61, maxRadius=100)
centers = []
radii = []
if circles1 is not None:
    circles1 = np.round(circles1[0, :]).astype("int")
    for (x, y, r) in circles1:
        centers.append([x, y])
        radii.append(r)
if circles2 is not None:
    circles2 = np.round(circles2[0, :]).astype("int")
    for (x, y, r) in circles2:
        centers.append([x, y])
        radii.append(r)
centers = np.array(centers, dtype="float32")
radii = np.array(radii, dtype="float32")
result = img_rgb.copy()
if len(centers) > 0:
    for i in range(len(centers)):
        cv2.circle(result, (int(centers[i, 0]), int(centers[i, 1])), int(radii[i]), 
                   (255,255,0), 2)
plt.figure(figsize=(10, 8))
plt.imshow(result)
plt.title('Detected Circles')
plt.axis('off')
plt.show()
