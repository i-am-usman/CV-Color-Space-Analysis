import cv2
import numpy as np

# 1. Load and normalize image to 0-1 range
img = cv2.imread('WhatsApp Image 2026-02-01 at 11.42.52 PM.jpeg').astype(float) / 255.0
size = (500, 500)
img = cv2.resize(img, size)
b, g, r = cv2.split(img)

# 2. Calculate the 'Black' (K) channel
# Black is 1 minus the maximum of R, G, or B
k = 1 - np.max(img, axis=2)

# 3. Calculate C, M, Y channels
# We add a tiny value (1e-10) to avoid "division by zero" errors
c = (1 - r - k) / (1 - k + 1e-10)
m = (1 - g - k) / (1 - k + 1e-10)
y = (1 - b - k) / (1 - k + 1e-10)

# 4. Convert back to 0-255 scale for visualization
c = (c * 255).astype(np.uint8)
m = (m * 255).astype(np.uint8)
y = (y * 255).astype(np.uint8)
k = (k * 255).astype(np.uint8)

# Results
cv2.imshow("Cyan", c)
cv2.imshow("Magenta", m)
cv2.imshow("Yellow", y)
cv2.imshow("Black (Key)", k)
cv2.waitKey(0)
