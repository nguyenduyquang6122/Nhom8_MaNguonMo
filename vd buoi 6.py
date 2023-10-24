import cv2
a=cv2.imread('C:/Users/LAN/Pictures/Screenshots/a.jfif',cv2.IMREAD_GRAYSCALE)
cv2.imshow('anh',a)
cv2.imwrite('anhxinh.png',a)
