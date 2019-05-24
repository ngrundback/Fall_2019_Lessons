import cv2
import numpy as np

img = cv2.imread('mta.jpeg')

print(img.shape)
print(img.size)
print(img.dtype)
# access pixel
px = img[100,100]
print(px)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
