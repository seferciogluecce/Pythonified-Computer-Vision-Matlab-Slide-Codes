import numpy as np
import cv2

img = cv2.imread('road_sky.jpg')
cv2.imshow('Original' ,img)

Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)


K = 3
attemps=3
ret,label,center=cv2.kmeans(Z,K,None,criteria,attemps,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('K = ' + str(K),res2)


cv2.waitKey(0)
cv2.destroyAllWindows()