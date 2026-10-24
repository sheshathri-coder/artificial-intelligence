import cv2
import numpy as np
img=np.zeros((100,100,3),dtype=np.uint8)
mask=cv2.inRange(img,np.array([0,0,0]),np.array([0,0,0]))
print('Segmented pixels:',cv2.countNonZero(mask))
# Output: Segmented pixels: 10000