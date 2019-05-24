import cv2
import numpy as np

# img = cv2.imread('park.png')
# grayscale
img = cv2.imread('park.png',0)
#gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(img.shape)
print(img[95,144])
print(img[88,176])
print(img[31,207])
#result = cv2.fastNlMeansDenoising(img)
cv2.circle(img, (31, 207), 15, (0, 0, 101), 2)
cv2.circle(img, (377, 521), 15, (0,0,101), 2 )


# find edges
# edge_img = cv2.Canny(img,20,200)
cv2.imshow('dst_rt', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
