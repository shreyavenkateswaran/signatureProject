import cv2
import numpy as np

path = '/Users/poojaraghuram/Desktop/signature.jpeg'
image = cv2.imread(path, 0)
ret, threshold = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
transparent_image = cv2.cvtColor(threshold, cv2.COLOR_BGR2RGBA)
transparent_image[np.where((transparent_image == [255, 255, 255, 255]).all(axis=2))] = [0, 0, 0, 0]

cv2.imshow('transparent_image', transparent_image)
cv2.imwrite('transparent_image.png', transparent_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
