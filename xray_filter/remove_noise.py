import cv2

# Load the X-ray image
img_path = "image_file/xray.jpg"
image = cv2.imread(img_path)

# Check if image loaded successfully
if image is None:
    print("❌ Image not found! Check the path and file name.")
    exit()

# Apply median filter to remove noise
filtered_image = cv2.medianBlur(image, 5)

# Display both images
cv2.imshow("Original X-Ray", image)
cv2.imshow("Filtered X-Ray (Median Filter Applied)", filtered_image)

# Save filtered image
cv2.imwrite("filtered_xray.jpg", filtered_image)
print("✅ Noise removed and filtered image saved as 'filtered_xray.jpg'.")

cv2.waitKey(0)
cv2.destroyAllWindows()
