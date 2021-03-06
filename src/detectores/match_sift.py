import cv2
import numpy as np

img1 = cv2.imread("img/picadef1.png")
img2 = cv2.imread("img/picadef5.png")

#SIFT Detector
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

#Brute Force Matching
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

good = []
#0.48 para figura inclinada
#0.45 girada en 180°
#0.12 ampliada
for m,n in matches:
    if m.distance < 0.12*n.distance:
        good.append([m])

print(len(good))


res = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow("Detector SIFT",res)
cv2.waitKey(0)
cv2.destroyAllWindows()