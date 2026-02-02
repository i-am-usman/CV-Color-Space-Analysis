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

# 4. Show the results
cv2.imshow("Original", image)
cv2.imshow("Red Channel (Grayscale)", r)
cv2.imshow("Red Channel (Color)", red_only)
cv2.imshow("Blue Channel (Color)", blue_only)
cv2.imshow("Green Channel (Color)", green_only)     

cv2.waitKey(0)