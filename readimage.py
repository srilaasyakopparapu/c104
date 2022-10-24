import cv2
img=cv2.imread("images/images/butterfly.jpg")
cv2.imshow("display image",img)
#print(img)
grayimg=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("display grayscale image", grayimg)
cv2.waitKey(3000)
print(grayimg)