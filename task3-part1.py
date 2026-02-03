import cv2
import numpy as np

img = cv2.imread('WhatsApp Image 2026-02-01 at 11.42.52 PM.jpeg')
size = (500, 500)
img = cv2.resize(img, size)
# 1. HSV Removal
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v.fill(128) # Fill with neutral brightness
hsv_no_v = cv2.merge([h, s, v])
res_hsv = cv2.cvtColor(hsv_no_v, cv2.COLOR_HSV2BGR)

# 2. Lab Removal
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
l, a, b = cv2.split(lab)
l.fill(128) # Fill with neutral lightness
lab_no_l = cv2.merge([l, a, b])
res_lab = cv2.cvtColor(lab_no_l, cv2.COLOR_Lab2BGR)

cv2.imshow("Original", img)
cv2.imshow("HSV No Brightness", res_hsv)
cv2.imshow("Lab No Lightness", res_lab)
cv2.waitKey(0)