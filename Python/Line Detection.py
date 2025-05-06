import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'Enter your image path here')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
edges_r = cv2.Canny(img[:,:,2], 100, 200)
edges_g = cv2.Canny(img[:,:,1], 100, 200)  
edges_b = cv2.Canny(img[:,:,0], 100, 200)  
edges = edges_r | edges_g | edges_b
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, 
                        minLineLength=7, maxLineGap=5)
result = img_rgb.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(result, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.drawMarker(result, (x1, y1), (255, 255, 0), markerType=cv2.MARKER_CROSS, 
                      markerSize=10, thickness=2)
        cv2.drawMarker(result, (x2, y2), (255, 0, 0), markerType=cv2.MARKER_CROSS, 
                      markerSize=10, thickness=2)
plt.figure(figsize=(10, 8))
plt.imshow(result)
plt.title('Detected Lines')
plt.axis('off')
plt.show()
