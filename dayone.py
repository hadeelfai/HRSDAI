import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('img.jpg')

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('window')
plt.axis('off')
plt.show()