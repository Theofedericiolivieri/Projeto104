import numpy as np
import cv2
black = np.zeros([600,600])
black[300:400,200:400] = 255
print(black)
cv2.imshow("Preto",black)
cv2.waitKey(0)