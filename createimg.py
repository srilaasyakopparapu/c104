import numpy as np
import cv2
black=np.zeros([600,600])
black[20:100,100:100]=255
cv2.imshow("blackimg", black)
print(black)
cv2.waitKey(0)

