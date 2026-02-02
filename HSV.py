import cv2
import numpy as np

# 1. Load the image
image = cv2.imread('WhatsApp Image 2026-02-01 at 11.42.52 PM.jpeg')

# 2. Split into Blue, Green, and Red channels
# Remember: OpenCV uses BGR order!
b, g, r = cv2.split(image)

# 3. Create a "Red-only" version (keep Red, set Blue/Green to 0)
zeros = np.zeros(image.shape[:2], dtype="uint8")
red_only = cv2.merge([zeros, zeros, r])
blue_only = cv2.merge([b, zeros, zeros])
green_only = cv2.merge([zeros, g, zeros])

# # 4. Show the results
cv2.imshow("Original", image)

# 1. Convert BGR (Standard OpenCV) to HSV

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 2. Split into H, S, and V channels
h, s, v = cv2.split(hsv_image)

# # 3. Show the results
# Note: These will appear as grayscale. 
# Bright areas in 'H' represent specific colors on the spectrum.
# Bright areas in 'S' represent very vivid colors.
# Bright areas in 'V' represent the brightest parts of the original photo.
cv2.imshow("Hue Channel", h)
cv2.imshow("Saturation Channel", s)
cv2.imshow("Value (Brightness) Channel", v)
cv2.waitKey(0)


# Increase brightness by 50 units (clamped at 255)
v_bright = cv2.add(v, 50)

# Merge back and convert to BGR to see the result
hsv_modified = cv2.merge([h, s, v_bright])
img_bright = cv2.cvtColor(hsv_modified, cv2.COLOR_HSV2BGR)
cv2.imshow("Brightened Image", img_bright)
cv2.waitKey(0)