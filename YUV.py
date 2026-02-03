import cv2

# 1. Load your image
image = cv2.imread('WhatsApp Image 2026-02-01 at 11.42.52 PM.jpeg')
size = (500, 500)
image = cv2.resize(image, size)
# 2. Convert from BGR to YUV
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

# 3. Split into Y, U, and V
y, u, v = cv2.split(yuv_image)

# 4. Show the results
# Y will look like a perfect black and white photo
cv2.imshow("Y (Luma/Brightness)", y)

# U and V will look like strange, gray, ghostly images
cv2.imshow("U (Chroma Blue)", u)
cv2.imshow("V (Chroma Red)", v)

cv2.waitKey(0)