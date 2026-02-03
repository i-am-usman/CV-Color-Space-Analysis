import cv2
import numpy as np

# Load images
img1_raw = cv2.imread('WhatsApp Image 2026-02-01 at 11.42.52 PM.jpeg')
img2_raw = cv2.imread('2.jpeg')

# Resize for math (must be identical)
size = (500, 500)
img1 = cv2.resize(img1_raw, size)
img2 = cv2.resize(img2_raw, size)

def remove_brightness_lab(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(lab)
    l.fill(128) # Neutralizing the 'L' channel
    normalized_lab = cv2.merge([l, a, b])
    return cv2.cvtColor(normalized_lab, cv2.COLOR_Lab2BGR)

def remove_brightness_hsv(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v.fill(128) # Neutralizing the 'V' channel
    normalized_hsv = cv2.merge([h, s, v])
    return cv2.cvtColor(normalized_hsv, cv2.COLOR_HSV2BGR)

# Generate Normalized Versions
img1_lab_norm = remove_brightness_lab(img1)
img2_lab_norm = remove_brightness_lab(img2)

img1_hsv_norm = remove_brightness_hsv(img1)
img2_hsv_norm = remove_brightness_hsv(img2)

# Show images for Part 3 visualization
# cv2.imshow("1PM Normalized (Lab)", img1_lab_norm)
# cv2.imshow("5PM Normalized (Lab)", img2_lab_norm)
# cv2.imshow("1PM Normalized (HSV)", img1_hsv_norm)
# cv2.imshow("5PM Normalized (HSV)", img2_hsv_norm)
# # cv2.waitKey(0)


def get_dist(a, b):
    return np.sqrt(np.sum((a.astype("float") - b.astype("float")) ** 2))

# --- PART 2: Raw Comparison ---
dist_rgb = get_dist(img1, img2)

# Visualizing the difference (Where the sun changed things)
diff_map_rgb = cv2.absdiff(img1, img2)

# --- PART 3: Normalized Comparison ---
# Compare using only 'a' and 'b' channels of Lab
lab1 = cv2.cvtColor(img1, cv2.COLOR_BGR2Lab)
lab2 = cv2.cvtColor(img2, cv2.COLOR_BGR2Lab)
dist_lab_normalized = get_dist(lab1[:,:,1:], lab2[:,:,1:])

# Visualizing the difference after normalization
diff_map_lab = cv2.absdiff(img1_lab_norm, img2_lab_norm)

# Print Results
print(f"Distance RGB (Original): {dist_rgb:,.0f}")
print(f"Distance Lab (Normalized): {dist_lab_normalized:,.0f}")

# Show Difference Maps
cv2.imshow("Difference Before (RGB)", diff_map_rgb)
cv2.imshow("Difference After (Lab Normalized)", diff_map_lab)
cv2.waitKey(0)
cv2.destroyAllWindows()