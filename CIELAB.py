import cv2

# 1. Load image
image = cv2.imread('WhatsApp Image 2026-02-01 at 11.42.52 PM.jpeg')
size = (500, 500)
img = cv2.resize(image, size)
# 2. Convert to Lab
lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

# 3. Split channels into l a b
l, a, b_channel = cv2.split(lab_image)

# 4. Show results
cv2.imshow("L - Lightness", l)
cv2.imshow("a - Green to Red", a)
cv2.imshow("b - Blue to Yellow", b_channel)

cv2.waitKey(0)
