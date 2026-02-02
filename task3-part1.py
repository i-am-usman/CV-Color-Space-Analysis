import cv2
import numpy as np

# Load your image
img = cv2.imread('WhatsApp Image 2026-02-01 at 11.42.52 PM.jpeg')

# --- 1. HSV Brightness Removal ---
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v.fill(128) # Set brightness to a neutral constant
hsv_no_bright = cv2.merge([h, s, v])
result_hsv = cv2.cvtColor(hsv_no_bright, cv2.COLOR_HSV2BGR)

# --- 2. Lab Brightness Removal ---
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
l, a, b = cv2.split(lab)
l.fill(128) # Set lightness to a neutral constant
lab_no_bright = cv2.merge([l, a, b])
result_lab = cv2.cvtColor(lab_no_bright, cv2.COLOR_Lab2BGR)

cv2.imshow("Original", img)
cv2.imshow("HSV - No Brightness", result_hsv)
cv2.imshow("Lab - No Brightness", result_lab)
cv2.waitKey(0)