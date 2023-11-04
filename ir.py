import cv2
import numpy as np

frame = cv2.imread("/Users/sunilsavanur/Documents/ir_original_weather.jpg")
frame = cv2.resize(frame,(720,512))
gray1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
ret, gray1 = cv2.threshold(gray1,155,255,0)

gray2 = gray1.copy()

contours, hier = cv2.findContours(gray1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if 500 < cv2.contourArea(cnt) < 3000:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(gray2,(x,y),(x+w,y+h),0,-1)
cv2.imshow("Gray Image",gray2)
cv2.imwrite("/Users/sunilsavanur/Documents/ir_bright.jpg", gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()

