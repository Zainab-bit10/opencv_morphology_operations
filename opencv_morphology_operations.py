import cv2
import numpy as np 
img=cv2.imread("New folder/img2.png")
img=cv2.resize(img,(500,500))
n=np.ones((3,3),np.int8)   # for tophant ones(30,30)
er=cv2.erode(img,n,iterations=1)
et=cv2.dilate(img,n,iterations=1)
#op=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel=n,iterations=1)
#op=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel=n,iterations=1)
#op=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel=n,iterations=1)
 #op=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel=n,iterations=1)
op=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel=n,iterations=1)
cv2.imshow('t',op)
cv2.imshow("s",img)
cv2.imshow('f',er)
cv2.imshow('k',et)

cv2.waitKey(0)
cv2.destroyAllWindows()